# Session 07 — Full CRUD on Prisma

**Date:** 2026-07-01
**Phase:** 2 — Express + the habit tracker (in progress)

## What we covered

### Framework landscape (why Express)
- Express = the thinnest useful layer over the raw `node:http` server (routing, middleware, nicer req/res). Chosen because it's the lingua franca (most docs/jobs), teaches transferable fundamentals, and hides nothing while learning.
- **Alternatives mapped to what I know:** Express ≈ Flask (minimal); **Fastify** ≈ FastAPI (minimal + built-in validation, "Express but modern"); **NestJS** ≈ Laravel (opinionated, DI, decorators); **Hono** (edge/serverless, modern); **Koa** (older, fading).
- **Key insight:** concepts (HTTP model, routing, middleware, async handlers) transfer everywhere — ~80%. Only syntax + philosophy differ. Express → Fastify/Koa/Hono = a weekend. Express → NestJS = weeks (different paradigm). Learn the bare framework first; graduate to opinionated ones when you feel the pain.

### Converted all remaining routes to Prisma
- **`GET /habits/:id`** → `prisma.habit.findUnique({ where: { id: Number(req.params.id) } })`. Returns the row **or `null`** if missing → check with `if (!habit) return res.status(404)...`.
  - `Number(...)` still required: `req.params.id` is a string, schema `id` is `Int`, and Prisma is strict about types.
- **`PATCH /habits/:id`** → `prisma.habit.update({ where: { id }, data: req.body })`. No manual spread-merge needed — `update` only touches fields in `data`.
- **`DELETE /habits/:id`** → `prisma.habit.delete({ where: { id } })`, then `res.status(204).end()`.

### The big lesson: findUnique returns null, update/delete THROW
- **`findUnique`** on a missing row → returns `null` (quiet). Handle with `if (!habit)`.
- **`update` / `delete`** on a missing row → **throw** `PrismaClientKnownRequestError` with code **`P2025`**. A `null` check is useless because the throw jumps out of the function before the next line runs — the error escapes the route and Express dumps an ugly HTML 500.
- **Fix = `try/catch`** (the Phase 0 tool, now applied to Prisma):
  ```js
  try {
    const habit = await prisma.habit.update({ where: { id }, data: req.body });
    res.json(habit);
  } catch (error) {
    if (error.code === "P2025") return res.status(404).json({ error: "Habit not found" });
    throw error; // re-throw anything else
  }
  ```
- **Why check `error.code === "P2025"`** and not 404 on *any* error: a dropped DB connection or a bad field shouldn't be mislabeled "Habit not found."
- **Why `throw error` (re-throw)**: it passes unhandled errors up to Express's error handler. **If you removed it**, a non-P2025 error would be caught, skip the 404, and then send NO response → the client hangs forever. Rule: never catch an error just to hide it.

### JS idiom
- `if (!habit)` (idiomatic, catches all falsy) vs `if (habit === null)` (precise, only null). For `findUnique` (object-or-null) both work; `!habit` is conventional. Use `=== null` only when `0`/`""` are legit values to keep.

### Status code polish
- `204 No Content` means the body MUST be empty → use `res.status(204).end()`, NOT `.json(...)`. `204` + a body is a contradiction. To return the deleted object instead, use `res.json(habit)` (200).

## What I struggled with
- Forgot `Number()` on the `findUnique` where clause (string vs Int) — the exact thing flagged a moment earlier.
- Confused why `if (!habit)` didn't catch a missing PATCH row — because `update` throws instead of returning null (the line never runs).
- Didn't understand what `throw error` does — got it via my own `{"progress": 80}` example (a non-P2025 error that should surface, not be hidden).
- Wrote `res.status(204).json(habit)` — a No-Content-with-content contradiction.

## What clicked
- `findUnique` (null) vs `update`/`delete` (throw P2025) — different not-found handling.
- `try/catch` + re-throw as the real error-handling pattern; never swallow errors silently.
- Curl for hitting the API from the terminal ("i feel pro").
- Full CRUD now persistent on Postgres.

## Why Zod (next topic)
- Nothing validates request bodies yet — the API trusts client input (never do that). Zod = schema validation at the boundary → reject bad requests with a clean `400` before they hit Prisma.
- Zod ≈ **Pydantic** (FastAPI) / Form Requests (Laravel). TypeScript-first: one schema = validation + types. My `{"progress": 80}` case is exactly what Zod catches at the door.

## Pick up next time
- **Zod validation**: validate `POST`/`PATCH` bodies (e.g. `name` required, non-empty) → return `400` with clear messages instead of `500`s.
- Then **project structure** (split routes/controllers/services out of one big `server.js`).
- Then the habit-tracker features: daily **check-ins** + a **streak** endpoint.

## Environment reminder
- Start Docker Desktop + `docker start habit-postgres` before coding (container stops when Mac shuts down), else Prisma can't connect.
- Prisma pinned to **v6**.
