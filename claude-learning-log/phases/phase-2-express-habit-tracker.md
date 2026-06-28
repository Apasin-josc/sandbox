# Phase 2 — Express + the habit-tracker API

**Goal:** Build the real thing. This is the portfolio piece and where everything connects.

**Done when:** The habit-tracker API runs locally, persists to Postgres, and has working CRUD + a streak endpoint.

## Lessons
1. **Express basics** ⬜
   - Routing, middleware, `req`/`res`. Concepts I know from Laravel/FastAPI — just new syntax. Map them mentally.
2. **Database: PostgreSQL + Prisma** ⬜
   - Prisma is the closest thing to Laravel's Eloquent. Schema, migrations, queries.
   - Why Postgres over SQLite for a portfolio piece (real-world signal).
3. **Project structure** ⬜
   - Routes / controllers / services split. Env vars with `.env` + `dotenv` (or Node's built-in `--env-file`).
4. **Validation & errors** ⬜
   - `Zod` for input validation. Centralized error handling middleware.

## Build target — the habit tracker
- `POST /habits` — create a habit
- `GET /habits` — list habits
- `GET /habits/:id` — one habit
- `PATCH /habits/:id` / `DELETE /habits/:id`
- `POST /habits/:id/checkins` — log a daily check-in
- `GET /habits/:id/streak` — compute current streak (a little logic — good challenge)

## Stretch
Seed script, pagination on the list endpoint.
