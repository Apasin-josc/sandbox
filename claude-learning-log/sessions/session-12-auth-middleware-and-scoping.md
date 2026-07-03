# Session 12 — Auth Middleware & User-Scoping (Auth COMPLETE)

**Date:** 2026-07-03
**Phase:** 3 — Real-world (auth fully done & verified)

## What we covered

### Auth middleware (`src/middleware/authenticate.js`)
```js
import jwt from "jsonwebtoken";
export function authenticate(req, res, next) {
  const header = req.headers.authorization;              // "Bearer eyJ..."
  if (!header || !header.startsWith("Bearer ")) {
    return res.status(401).json({ error: "Missing or invalid Authorization header" });
  }
  const token = header.split(" ")[1];
  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET); // checks signature + expiry, throws if bad
    req.user = { id: payload.userId };                         // hand identity downstream
    next();                                                    // proceed to the route
  } catch (error) {
    return res.status(401).json({ error: "Invalid or expired token" });
  }
}
```
- Client sends the token each request in the `Authorization: Bearer <token>` header.
- **`next()`** hands control to the route. Forget it on the success path → the request HANGS (verified but never passed on).
- **`req` is a shared "backpack"** through the pipeline: middleware drops `req.user` in, controllers read it. That's how identity travels from middleware → controller.
- Mounted so it runs before all habit routes: `app.use("/habits", authenticate, habitsRouter)`.

### User-scoping (authentication → authorization)
The token was toothless until controllers *used* `req.user.id`:
- **create**: stamp the owner — `data: { ...result.data, userId: req.user.id }`. Client never sends userId (can't be trusted); the token proves who they are, server stamps it.
- **list**: `findMany({ where: { userId: req.user.id } })` — only your habits.
- **getHabit / :id routes**: must match id AND owner. **Prisma wrinkle:** `findUnique`/`update`/`delete` only accept UNIQUE fields in `where` (just `id`) — can't add `userId`. Fix = **`findFirst({ where: { id, userId } })`** (accepts any condition; multiple = AND).
- **update / delete**: verify ownership with `findFirst` first → 404 if missing/not-owned → then act by id. (This ownership check replaces the old P2025 try/catch.)
- **checkin / streak routes**: same fix — swapped `findUnique({where:{id}})` → `findFirst({where:{id, userId}})` so you can't act on someone else's habit.
- Returning **404** (not 403) for another user's habit = don't even leak that it exists.

### Env vars
- Node doesn't auto-load `.env`. Dev script loads it: `node --watch --env-file=.env src/server.js`. `JWT_SECRET` lives in `.env` (gitignored).

## VERIFIED end-to-end (ran against the live server)
- No token → 401 ✓
- Register (201 / 409 duplicate) ✓; wrong password → 401 ✓
- jose: create (userId stamped) / list / checkin / streak all work ✓
- **Isolation:** jose2 sees `[]`, and gets **404** on jose's habit for GET / DELETE / streak ✓
- → Authentication (logged in) AND authorization (only your own data) both proven.

## What clicked
- Middleware verifies token + attaches `req.user`; controllers consume it.
- `findUnique` (unique fields only) vs **`findFirst`** (any condition) — the key to id+owner scoping.
- The difference between authentication and authorization, seen live via the isolation test.

## Pick up next time — rest of Phase 3
- **Tests**: vitest or `node:test` + supertest — automate exactly the flow we just ran by hand.
- **Deploy**: Railway/Render + managed Postgres (graduate `phase_2/` → `habit-tracker/` repo first).
- **Dockerfile** for the app (write our OWN image).
- **TypeScript** migration (Zod `z.infer` gives types for free).

### Optional polish still open
- `.refine()` to reject empty PATCH; FK `ON DELETE CASCADE`; consider scoping `Checkin` by user too (currently reachable only via owned habits, so OK).

## Environment
- `docker start habit-postgres` before coding. Prisma v6. `npm run dev`.
- Auth endpoints: `/auth/register`, `/auth/login`. All `/habits*` routes protected + user-scoped.
