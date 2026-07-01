# Session 09 — Project Structure, REST Client, and Relations

**Date:** 2026-07-01
**Phase:** 2 — Express + the habit tracker (nearly complete — only streaks left)

## What we covered

### Framework landscape recap
- Express = thin layer over raw `http`; lingua franca (docs/jobs). Alternatives: Fastify (≈FastAPI, modern), NestJS (≈Laravel, opinionated/DI/decorators), Hono (edge), Koa (fading).
- Concepts (HTTP model, routing, middleware, async) transfer ~80% everywhere. Express→Fastify/Koa/Hono = a weekend; Express→NestJS = weeks (different paradigm). Learn the bare one first.

### Project structure (split the monolith)
- Refactored one 109-line `server.js` into `src/` with **separation of concerns** (each file has one reason to change):
  ```
  src/
    server.js                     # entry point: create app, mount middleware/routes, listen
    lib/prisma.js                 # the ONE shared PrismaClient (never new-per-request)
    schemas/habit.schema.js       # Zod schemas
    controllers/habits.controller.js  # handler logic (validate → query → respond)
    routes/habits.routes.js       # URL+verb → controller (express.Router())
    middleware/errorHandler.js    # global error handler
  ```
- **Dependency flows ONE way:** server → routes → controllers → (lib/prisma + schemas). Leaves import nothing of ours. Prevents circular messes.
- **`express.Router()`** = a mini-app grouping routes. Mounted with `app.use("/habits", habitsRouter)`; paths inside are RELATIVE (`/`, `/:id`) and the `/habits` prefix is added once at mount. Adding a resource later = one `app.use("/x", xRouter)` line, no rewrites.
- `import`/`export` across files (Phase 1's `math.js`/`app.js` for real): relative paths + `.js` extensions (ESM strict).
- Added `"dev": "node --watch src/server.js"` script → `npm run dev`. Deleted old root `server.js`.
- Wrote a detailed `phase_2/structure.md` (folder layout, dependency diagram, per-file exports, full request-lifecycle trace, feature-location table, how-to-add-a-resource).

### REST Client (goodbye long curl commands)
- Installed VS Code **REST Client** (`humao.rest-client`). Created `phase_2/requests.http` — click "Send Request" above each block; responses open in a pane. Requests separated by `###`, `@baseUrl` variable.
- Doubles as living API documentation (every endpoint + expected status codes in one file). The "graduate from curl" step. (Bruno/Postman = standalone-app versions.)

### Relations — one-to-many (the big new concept)
- A **Habit has many Checkins**. Modeled with a foreign key.
- **The foreign key lives on the "many" side.** `Checkin` gets a `habitId Int` column holding the parent habit's `id` (referenced by id because id is unique, name isn't).
- Prisma schema (only `habitId` is a real column; the other two are navigation sugar):
  ```prisma
  model Habit   { ... checkins Checkin[] }              // virtual back-reference (NOT a column)
  model Checkin {
    id Int @id @default(autoincrement())
    createdAt DateTime @default(now())
    habitId Int                                          // the FK column (real)
    habit Habit @relation(fields: [habitId], references: [id])  // relation def (NOT a column)
  }
  ```
- Migration (`add_checkins`) generated `CREATE TABLE "Checkin"` + a **FOREIGN KEY** constraint:
  `FOREIGN KEY ("habitId") REFERENCES "Habit"("id") ON DELETE RESTRICT ON UPDATE CASCADE`
  - **Referential integrity:** Postgres rejects a check-in whose `habitId` has no matching habit.
  - **`ON DELETE RESTRICT`:** can't delete a habit that still has check-ins (gotcha — switch to `ON DELETE CASCADE` if we want deleting a habit to remove its check-ins).
- **Migrations = per `migrate dev` run**, not per model. Each run = one timestamped folder = a snapshot of changes since the last one. They stack like git commits; replaying them rebuilds the DB (how another machine gets an identical DB).

### Check-in endpoints (built on the relation)
- `POST /habits/:id/checkins` and `GET /habits/:id/checkins` — added to `habitsRouter` (paths must be **consistent plural** — caught a singular/plural mismatch).
- **`habitId` comes from the URL param, not the body.** `const habitId = Number(req.params.id)`.
- Guard both with an existence check (`findUnique` → 404) so you get a clean 404 instead of a DB foreign-key throw.
- `prisma.checkin.create({ data: { habitId } })` (create); `prisma.checkin.findMany({ where: { habitId }, orderBy: { createdAt: "desc" } })` (list newest-first).
- Verified end to end: POST piles up check-ins, GET lists them, missing habit → 404.

## What I struggled with
- Relations felt abstract from the schema syntax — clicked only after seeing the two tables drawn with actual rows (`habitId` as a plain number pointing at a Habit's id).
- `createCheckin` bugs: named the `findUnique` result `habitId` (it's the whole habit OBJECT, not the id) then referenced a non-existent `habit`; also forgot `await` on `create`. Fixed by keeping TWO variables: `habitId` (number) and `habit` (object).
- `listHabitsCheckin` queried the wrong model (`prisma.habit.findMany({ where: { habitId } })`) — Habit has no `habitId` column. Fixed to `prisma.checkin.findMany`.
- Singular/plural route mismatch (`/checkin` vs `/checkins`).

## What clicked
- Separation of concerns + one-way imports; Router mounting with a prefix.
- REST Client >> curl for iterating.
- **The whole one-to-many mental model:** FK on the many side, only `habitId` is a real column, Prisma's relation fields are code-navigation sugar.
- Migrations as a git-like history of the schema.

## Pick up next time — FINISH PHASE 2
- **Streak endpoint** `GET /habits/:id/streak` — the last core feature. Logic problem (not CRUD): walk the check-in dates, count consecutive days. This is where `dayjs` (installed in Phase 1) earns its place.
- Optional polish: `.refine()` for empty PATCH; switch FK to `ON DELETE CASCADE` if we want to delete habits with check-ins.

## Then Phase 3 (important framing)
- **No new `phase_3/` folder.** Phases 0–1 were throwaway sandboxes; the habit tracker is a REAL app. Phase 3 (auth/JWT, tests, deploy to Railway/Render, Dockerfile, TypeScript) all happens **inside this same codebase**.
- Consider graduating `phase_2/` into its own real project folder (e.g. `habit-tracker/`) with its own git repo — "phases" are learning stages, not folders.

## Environment reminder
- `docker start habit-postgres` before coding. Prisma pinned to **v6**. `zod` installed.
- Run with `npm run dev`. Endpoints: `/habits`, `/habits/:id`, `/habits/:id/checkins`.
