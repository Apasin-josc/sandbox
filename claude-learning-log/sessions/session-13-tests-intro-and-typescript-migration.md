# Session 13 — Tests (intro) & TypeScript Migration

**Date:** 2026-07-07
**Phase:** 3 — Real-world

## Part A — Automated tests (intro; not finished)

### Why & what
- A test = code that runs your code and **asserts** it behaved right. Codifies the by-hand curl flow; runs in seconds on every change; catches regressions.
- For an API, **integration tests** (fire a request, check status+body) give the most value.
- Tools: **`vitest`** (runner) + **`supertest`** (fires HTTP requests at the app in-process, no real port). Installed as devDeps.

### Prerequisite refactor: split `app.js` / `server.js`
- **`src/app.js`** now builds + `export`s the configured `app` (no `listen`). **`src/server.js`** imports it and calls `app.listen` — the only file that opens a port.
- Why: tests `import { app }` to fire requests at it *without* starting a real server. `server.js` is never imported by tests.

### First tests (`src/__tests__/api.test.ts`)
```js
import { describe, it, expect } from "vitest";
import request from "supertest";
import { app } from "../app.ts";

describe("auth guard & validation", () => {
  it("returns 401 on GET /habits without a token", async () => {
    const res = await request(app).get("/habits");
    expect(res.status).toBe(401);
  });
  it("returns 400 when registering with an invalid email", async () => {
    const res = await request(app).post("/auth/register")
      .send({ email: "not-an-email", password: "short", username: "x" });
    expect(res.status).toBe(400);
  });
});
```
- `describe` groups, `it` = one case, `request(app)` = supertest, `expect().toBe()` = assertion. Rhythm: **Arrange → Act → Assert.**
- Chose **stateless** tests on purpose (rejected before any DB write) so they're repeatable and don't pollute data.
- Scripts: `"test": "vitest run"`, `"test:watch": "vitest"`.

### The unsolved hard part (NEXT TIME)
- Stateful tests (register/login/create/isolation) **write to the DB** → against the dev DB they pollute it and fail on re-run (duplicate email → 409 not 201). Need: a **separate test database** + **reset/clean between tests** (and load `JWT_SECRET` into the test env). This is the crux of API testing — deferred.

## Part B — TypeScript migration (COMPLETE ✅)

### Why TS (felt on our own bugs)
- TS = JS + a type-checker that runs BEFORE the code. Catches at compile time what we hit at runtime: the `habit` vs `habitId` ReferenceError, `findUnique({where:{id,userId}})` (invalid arg), the `dayjs` missing import, `habit.nam` typos.
- Wins: bugs caught early, autocomplete everywhere, fearless refactoring. Cost: type annotations + a build step (but see below — Node skips it). Roadmap put TS LAST so we'd *feel* the hole first.

### How we ran it (key insight)
- **Node 26 runs `.ts` directly** by *stripping* types — no build step for dev. But stripping ≠ checking.
- So: `npm run dev` = `node --watch --env-file=.env src/server.ts` (runs), and `npm run typecheck` = `tsc --noEmit` (VALIDATES). Different jobs.
- When Node runs `.ts`, **imports need the `.ts` extension** (`./app.ts`, not `./app.js`) — confirmed by test (`.js` → MODULE_NOT_FOUND).

### Setup
- Installed: `typescript`, `@types/node`, `@types/express`, `@types/jsonwebtoken`, `@types/bcrypt`, `@types/supertest`. (zod/prisma/dayjs ship their own types.)
- `tsconfig.json`: `module`/`moduleResolution: NodeNext`, `strict: true`, `noEmit: true`, `allowImportingTsExtensions: true` (tsc only checks; Node runs), `esModuleInterop`, `skipLibCheck`.
- Renamed all `src/**/*.js` → `.ts`; rewrote relative import extensions `.js` → `.ts`.

### The type errors TS caught (and fixes)
1. **Implicit `any` on `req`/`res`/`next`/`err`** → annotated with `Request`, `Response`, `NextFunction` from express (`import type { ... } from "express"`).
2. **`'error' is of type 'unknown'`** in `catch` → narrowed with `error instanceof Prisma.PrismaClientKnownRequestError && error.code === "P2002"/"P2025"` (import `{ Prisma } from "@prisma/client"`).
3. **`process.env.JWT_SECRET` is `string | undefined`** (jwt.sign/verify reject undefined) → `process.env.JWT_SECRET!` assertion. (Prod-proper: validate env at startup and export a typed constant.)
4. **`req.user` doesn't exist on `Request`** → **declaration merging** in `src/types/express.d.ts`:
   ```ts
   declare global { namespace Express { interface Request { user?: { id: number } } } }
   export {};
   ```
   Controllers use `req.user!.id` ("!" = guaranteed by the authenticate middleware).

### Verified
- `tsc --noEmit` → **0 errors**. `vitest` → **2/2 pass** on `.ts`. Server boots via `node src/server.ts` and serves (`/habits` → 401). All three green.

## Pick up next time
- **Finish tests:** separate test DB + reset between runs + load `JWT_SECRET` in test env → then write the stateful integration tests (register→login→create→isolation) that mirror the by-hand curl flow.
- Then Phase 3 remainder: **deploy** (Railway/Render; graduate `phase_2/`→`habit-tracker/` repo), **Dockerfile** for the app.
- Optional: validate env properly (a typed `config.ts` that throws on missing vars) instead of `!`.

## Environment
- `docker start habit-postgres` before coding. Prisma v6. Node 26 runs `.ts` natively.
- Scripts: `npm run dev` (run), `npm run typecheck` (tsc --noEmit), `npm test` (vitest run), `npm run test:watch`.
- Files are now `.ts`; imports use `.ts` extensions; `tsconfig.json` + `src/types/express.d.ts` added.
