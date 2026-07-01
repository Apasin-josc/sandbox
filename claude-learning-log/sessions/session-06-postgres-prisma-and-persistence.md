# Session 06 — Postgres, Prisma, and Persistence

**Date:** 2026-07-01
**Phase:** 2 — Express + the habit tracker (in progress)

## What we covered

### Why Prisma
- Three ways JS talks to a DB: raw SQL driver (`pg`), query builder (Knex), or **ORM** (Prisma/Drizzle/TypeORM). ORM = the Eloquent-equivalent from Laravel.
- Prisma chosen: closest to Eloquent comfort, auto-generated **type-safe** client, great migrations, huge adoption (employability). **Honest counterpoint:** it hides SQL — still learn SQL underneath eventually. Drizzle is a lighter, SQL-closer alternative.

### Docker Postgres
- Ran Postgres via Docker (no local install): `docker run --name habit-postgres -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=habits -p 5432:5432 -d postgres:16`.
- **Image vs container:** an *image* (`postgres:16`) is a read-only blueprint downloaded from Docker Hub; a *container* (`habit-postgres`) is a running instance of it. The container lives in Docker's own storage (managed globally), NOT in the project folder — that's why there's no file in `phase_2/`.
- **No Dockerfile needed to RUN an existing image.** You write a Dockerfile only to build your OWN app's image (that's Phase 3, for the Express server).
- Interact via commands (`docker ps`, `docker stop/logs`) and the network (`localhost:5432`, thanks to `-p`).

### Connection string (fully broken down)
`postgresql://postgres:secret@localhost:5432/habits?schema=public`
- shape: `protocol://user:password@host:port/database?options`
- `postgresql://` = scheme; `postgres` = user; `secret` = password; `@` = separator; `localhost:5432` = host+port; `habits` = database; `?schema=public` = a **query param** (same `?key=value` shape as `/habits?done=true`). Every part maps back to a `docker run` flag.
- `.env` holds it and is **gitignored** (verified). A Postgres *schema* = a namespace for tables; `public` is the default — leave it (changing it is noise for this project).

### Prisma setup (+ a real-world tooling lesson)
- `npm install prisma --save-dev` (CLI) + `npm install @prisma/client` (runtime), then `npx prisma init`.
- **Hit a version wall:** `prisma init` installed **Prisma 7.8.0**, which moved the datasource `url` out of `schema.prisma` into `prisma.config.ts` and requires a driver adapter. Migration failed with `P1012`.
- **Decision: downgraded to Prisma 6** (`npm install prisma@6 @prisma/client@6`, removed `prisma.config.ts`). **Lesson:** bleeding-edge tooling makes you fight the tool instead of learning the concept; the ORM concepts are identical in v6, and v6 has a decade of docs. Match your tools to your learning resources. (Ignore the "update to 7.8.0" nag.)
- Schema: `generator prisma-client-js` + `datasource db { provider = "postgresql"; url = env("DATABASE_URL") }` + a `Habit` model (`id` autoincrement PK, `name` String, `done` Boolean default false, `createdAt` DateTime default now()).
- `npx prisma migrate dev --name init` → generated a SQL migration, created the `Habit` table, generated the client.

### Reading the generated SQL (learning the "useful hard way")
`CREATE TABLE "Habit"` mapping:
- `id Int @id @default(autoincrement())` → `"id" SERIAL NOT NULL` + `PRIMARY KEY ("id")`
- `name String` → `"name" TEXT NOT NULL`
- `done Boolean @default(false)` → `"done" BOOLEAN NOT NULL DEFAULT false`
- `createdAt DateTime @default(now())` → `"createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP`
- **Primary key is NOT NULL** because a PK must be both unique AND present — a NULL id = a row with no "address" (unreachable by `/habits/:id`; `NULL = NULL` isn't even true in SQL).

### Wiring Prisma into the app
- `import { PrismaClient } from "@prisma/client"; const prisma = new PrismaClient();`
- `GET /habits` → `const habits = await prisma.habit.findMany();` — **async/await is back, and now it's real**: a DB query is I/O ("kitchen work"), so you `await` it. Returned `[]` on the empty table.
- `POST /habits` → `await prisma.habit.create({ data: { name: req.body.name } })` — runs SQL INSERT; `id`/`done`/`createdAt` auto-fill from defaults.
- **PROVED PERSISTENCE:** POSTed "meditate", saw it in GET, restarted the server → data **still there**. (In-memory array would have reset to `[]`.) That's the whole point of a database.

## What I struggled with
- Confused about where the Docker container "lives" (expected a file/Dockerfile in the project) — cleared up with image-vs-container + app-store analogy.
- `.env` had the connection string backwards — the Prisma-Postgres default was active; my Docker URL was commented out.
- Prisma 7 config breakage (not my fault — version churn).
- Mild pushback: "I'd rather learn the hard way." Reframed: the useful hard way = reading the generated SQL & understanding concepts, NOT fighting undocumented tooling.

## What clicked
- Image vs container; why no Dockerfile is needed to run Postgres.
- The connection string, part by part, mapped to Docker flags.
- ORM value in one screen: 4 schema lines → correct, versioned SQL.
- **async/await from Phase 0 is literally the mechanism for every DB call.**
- Persistence across restarts — toy vs. real backend.

## Pick up next time
- **Convert the remaining 3 routes to Prisma:** `GET /habits/:id` → `prisma.habit.findUnique({ where: { id } })`; `PATCH` → `prisma.habit.update`; `DELETE` → `prisma.habit.delete`. (They still use the old in-memory `.find`/`.splice` logic — now inconsistent with the DB.)
- Then **validation with Zod** (e.g. reject a POST with no `name`).
- Later: project structure (routes/controllers/services), then check-ins + streak endpoint.

## Environment notes
- Docker container `habit-postgres` (postgres:16) on `localhost:5432`, DB `habits`. Start Docker Desktop + `docker start habit-postgres` if stopped.
- Prisma pinned to **v6** (do NOT upgrade to 7 mid-learning).
- `phase_2/`: `server.js` (Express, GET+POST on Prisma, other routes still in-memory), `prisma/schema.prisma`, `prisma/migrations/`, `.env` (gitignored).
