# Session 05 — Express and Full CRUD

**Date:** 2026-06-30
**Phase:** 2 — Express + the habit tracker (in progress)

## What we covered
- Set up `phase_2/`: `npm init -y`, `"type": "module"`, `npm install express`.
- **Express collapses the raw-`http` pain:**
  - `app.get("/habits", ...)` encodes BOTH the method (the verb is the method name — `app.get` / `app.post`) AND the path (the argument). Replaces the whole `if (req.method && req.url)` check.
  - `res.json(data)` does TWO jobs: sets `Content-Type: application/json` AND `JSON.stringify`s the data. Replaces `writeHead` + `end(JSON.stringify())`.
  - Express has a built-in default 404 (`Cannot GET /xxx`) — no hand-written `else` needed.
- **Middleware:** `app.use(express.json())` — a function that runs between request arrival and the route handler. It reads + parses the JSON body and attaches it to `req.body`.
  - Without it, `req.body` is `undefined` (Express doesn't parse bodies by default — same as raw `http` needing manual chunk collection).
  - It's **opt-in** because not every request has a JSON body (GET has none) and bodies aren't always JSON (forms, files). `app.use` with no path = runs for every route; can also attach per-route.
- **Route params vs query params** (important distinction):
  - Route/path param: `/habits/:id` → `req.params.id` — identifies *which* resource.
  - Query param: `/habits?done=true` → `req.query.done` — filter/sort/paginate.
- **Anything from a URL is a string** → must `Number(req.params.id)` before comparing with `===` (Phase 0 strictness: `"2" === 2` is false).
- **Status codes:** 200 OK, 201 Created (POST), 204 No Content (DELETE), 404 Not Found.
- Built **full CRUD** on an in-memory `habits` array:
  - `GET /habits` (list), `GET /habits/:id` (one), `POST /habits` (create, 201), `PATCH /habits/:id` (partial update), `DELETE /habits/:id` (204).
- **`.find` vs `.findIndex`** (the big stumbling block): `.find` returns the *item* (or `undefined`); `.findIndex` returns the *position* (or `-1`). `.splice(index, count)` needs a position → use `findIndex`.
- **`.splice(startIndex, howMany)`**: omitting `howMany` deletes everything from index to the end; pass `1` to remove just one.
- **PATCH merge with spread:** `habits[index] = { ...habits[index], ...req.body }` — existing fields first, then `req.body` overrides only the sent fields (partial update). **Order matters**: body must come last or updates get thrown away.
- **Error handling in routes:** prefer `return res.status(404).json({error})` over `throw` — and the `return` stops the handler so you don't send two responses.

## What I struggled with
- `req.body` was `undefined` until adding `app.use(express.json())`.
- Called `:id` a "query param" — it's a route/path param.
- DELETE bugs: used `.find` instead of `.findIndex`; passed a callback to `.splice` (it takes numbers, not a predicate); `.splice(index)` with no count; variable name mismatch (`findId` vs `index`).
- Switched to "just give me the answer" twice near the end — a fatigue signal. Noted: the `find`/`findIndex` bug only sticks by fighting it, not by copying.

## What clicked
- Express = a thin, convenient wrapper over the raw `http` server I built in Phase 1.
- Middleware as a "prep station" every request passes through.
- `.find` (item) vs `.findIndex` (position), and why splice needs the index.
- Spread-merge for partial updates, and why order matters.

## Pick up next time — PERSISTENCE
- The `habits` array **resets on every server restart** (it's in memory). That's the motivation for a real database.
- Next: **PostgreSQL + Prisma** — schema, migrations, swap the in-memory array for real DB queries.
- Then: project structure (routes/controllers/services), env vars (`.env`), validation (Zod).

## Current file
`phase_2/server.js` — Express app with full in-memory CRUD for `/habits`.
