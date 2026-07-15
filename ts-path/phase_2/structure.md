# Project Structure & Request Flow

How this Express + Prisma app is organized, why, and exactly how a request travels through it.

---

## 1. The folder layout

```
phase_2/
├── .env                     # secrets (DATABASE_URL) — gitignored
├── package.json             # deps + scripts ("dev": node --watch src/server.js)
├── prisma/
│   ├── schema.prisma        # DB models (source of truth for the database)
│   └── migrations/          # generated SQL history
└── src/
    ├── server.js            # ENTRY POINT — wires everything, starts the server
    ├── lib/
    │   └── prisma.js        # the single shared PrismaClient
    ├── routes/
    │   └── habits.routes.js # URL + verb  →  which controller function
    ├── controllers/
    │   └── habits.controller.js # the actual handler logic (validate, query, respond)
    ├── schemas/
    │   └── habit.schema.js  # Zod validation shapes
    └── middleware/
        └── errorHandler.js  # global error handler (runs last)
```

**Guiding principle — separation of concerns:** each file has *one reason to change*.
Change validation rules → touch only `schemas/`. Add a route → touch only `routes/`.
Change how errors are formatted → touch only `middleware/`. Nothing bleeds into anything else.

---

## 2. The dependency direction (who imports whom)

Imports flow in ONE direction. Nothing lower ever imports something higher.

```
server.js
   │  imports
   ├──────────────▶ routes/habits.routes.js
   │                      │ imports
   │                      ▼
   │                controllers/habits.controller.js
   │                      │ imports
   │                      ├──────────────▶ lib/prisma.js      (DB access)
   │                      └──────────────▶ schemas/habit.schema.js  (validation)
   │  imports
   └──────────────▶ middleware/errorHandler.js
```

- **server.js** knows about routes + middleware, but NOT about controllers or Prisma directly.
- **routes** know about controllers, but not about Prisma or Zod.
- **controllers** are where the real work happens — they pull in the DB client and the schemas.
- **lib/prisma.js** and **schemas/** are "leaves" — they import nothing from our own code.

This one-way flow is what keeps it untangled. If `lib/prisma.js` tried to import a controller, you'd have a circular mess.

---

## 3. What each file CREATES and EXPORTS

### `src/lib/prisma.js` — the database client
```js
import { PrismaClient } from "@prisma/client";
export const prisma = new PrismaClient();
```
- **Creates:** ONE `PrismaClient` instance for the entire app.
- **Exports:** `prisma`.
- **Why one instance?** Each `new PrismaClient()` opens its own pool of DB connections. Making one per request would exhaust the database. So we create it once here and everyone imports the same one.

### `src/schemas/habit.schema.js` — validation shapes
```js
import { z } from "zod";
export const createHabitSchema = z.object({ name: z.string().min(1) });
export const updateHabitSchema = z.object({ name: z.string().min(1), done: z.boolean() }).partial();
```
- **Creates:** two Zod schemas (the "shapes" a client is allowed to send).
- **Exports:** `createHabitSchema` (POST — `name` required), `updateHabitSchema` (PATCH — all optional).
- **Uses feature:** Zod. Nothing else depends on it except the controller.

### `src/controllers/habits.controller.js` — the logic
```js
import { prisma } from "../lib/prisma.js";
import { createHabitSchema, updateHabitSchema } from "../schemas/habit.schema.js";

export async function listHabits(req, res) { ... }
export async function getHabit(req, res) { ... }
export async function createHabit(req, res) { ... }
export async function updateHabit(req, res) { ... }
export async function deleteHabit(req, res) { ... }
```
- **Creates:** one `async` function per operation. Each does: (optionally) validate with a schema → query with `prisma` → send a response.
- **Exports:** the five handler functions.
- **Imports/uses:** `prisma` (DB) + the schemas (validation). This is the ONLY file that talks to the database.
- **Note:** these are the exact same handler bodies that used to live inline in the old `server.js` — just lifted out and named.

### `src/routes/habits.routes.js` — the URL map
```js
import { Router } from "express";
import { listHabits, getHabit, createHabit, updateHabit, deleteHabit } from "../controllers/habits.controller.js";

export const habitsRouter = Router();

habitsRouter.get("/", listHabits);     // GET    /habits
habitsRouter.get("/:id", getHabit);    // GET    /habits/:id
habitsRouter.post("/", createHabit);   // POST   /habits
habitsRouter.patch("/:id", updateHabit); // PATCH /habits/:id
habitsRouter.delete("/:id", deleteHabit); // DELETE /habits/:id
```
- **Creates:** an Express `Router` — a mini-app that groups all `/habits` routes.
- **Exports:** `habitsRouter`.
- **Key idea:** paths here are RELATIVE (`/`, `/:id`). The `/habits` prefix is added ONCE when this router is mounted in `server.js`. So `"/:id"` here becomes `/habits/:id` at runtime.
- It maps *verb + path* → *which controller function to run*. No logic lives here — it's a table of contents.

### `src/middleware/errorHandler.js` — the safety net
```js
export function errorHandler(err, req, res, next) {
  if (err.type === "entity.parse.failed") return res.status(400).json({ error: "Invalid JSON in request body" });
  console.error(err);
  res.status(500).json({ error: "Internal server error" });
}
```
- **Creates/Exports:** the error-handling middleware.
- **The 4 arguments `(err, req, res, next)` are the signal** — that's how Express recognizes an error handler (normal middleware has 3 args).
- Catches malformed JSON (→ clean 400) and any other thrown error (→ generic 500, with the real error logged server-side only).

### `src/server.js` — the entry point (assembles everything)
```js
import express from "express";
import { habitsRouter } from "./routes/habits.routes.js";
import { errorHandler } from "./middleware/errorHandler.js";

const app = express();

app.use(express.json());          // 1. parse JSON bodies
app.use("/habits", habitsRouter); // 2. mount the habits routes under /habits
app.use(errorHandler);            // 3. error handler LAST

app.listen(3000, () => console.log("server running on http://localhost:3000"));
```
- **Creates:** the Express `app` and starts the HTTP server.
- **The ORDER of `app.use(...)` matters** — Express runs middleware top-to-bottom (see next section).

---

## 4. The request lifecycle (trace `GET /habits/5`)

A request travels through the app like a pipeline. Follow the numbers:

```
   Client:  curl localhost:3000/habits/5
       │
       ▼
┌─────────────────────────────────────────────────────────────┐
│ src/server.js                                                 │
│   1. express.json()   → parses body (none here) and continues │
│   2. app.use("/habits", habitsRouter)                         │
│      → the URL starts with /habits, so hand off to the router │
└─────────────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────┐
│ src/routes/habits.routes.js                                   │
│   3. matches GET "/:id"  (because /habits was stripped)       │
│      → run the getHabit controller, with req.params.id = "5"  │
└─────────────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────┐
│ src/controllers/habits.controller.js  → getHabit()            │
│   4. const habit = await prisma.habit.findUnique({            │
│        where: { id: Number(req.params.id) } })  ← "5" → 5     │
│         │                                                     │
│         ▼ (uses lib/prisma.js — the shared client)            │
│   5. Prisma sends SQL to Postgres, awaits the row (I/O)       │
│   6a. found     → res.json(habit)         (200)               │
│   6b. not found → res.status(404).json(...)                   │
└─────────────────────────────────────────────────────────────┘
       │
       ▼
   Response goes back to the client.

   If ANY step throws (e.g. update/delete on a missing row, or bad JSON),
   Express skips ahead to  →  src/middleware/errorHandler.js  (runs last).
```

### The middleware pipeline in words
1. **`express.json()`** runs first on *every* request — turns the raw body into `req.body`. (Bad JSON dies here → error handler → 400.)
2. **`habitsRouter`** runs if the path matches `/habits*`. Inside, it finds the matching verb+path and calls the controller.
3. **The controller** validates (Zod), queries (Prisma), and responds.
4. **`errorHandler`** only runs if something threw. It's registered LAST so it can catch errors from everything above it (the "net under the trapeze").

---

## 5. Where each concept/feature lives

| Feature | File | Role |
|---|---|---|
| **Express app + wiring** | `src/server.js` | create app, mount middleware/routes, `listen` |
| **express.json() middleware** | `src/server.js` | parse request bodies into `req.body` |
| **Router** | `src/routes/habits.routes.js` | group + map `/habits` routes to controllers |
| **Controllers (handlers)** | `src/controllers/habits.controller.js` | the request→response logic |
| **Prisma (DB access)** | `src/lib/prisma.js` (client) + used in controllers | query Postgres |
| **Prisma models/migrations** | `prisma/schema.prisma`, `prisma/migrations/` | define + version the DB tables |
| **Zod (validation)** | `src/schemas/habit.schema.js` (defined) + used in controllers | reject bad input → 400 |
| **Error handling** | `src/middleware/errorHandler.js` | bad JSON → 400, unexpected → 500 |
| **Secrets/config** | `.env` | `DATABASE_URL` |

---

## 6. How to run it

```bash
# make sure Postgres is up (Docker)
docker start habit-postgres

# start the app with auto-reload
npm run dev            # = node --watch src/server.js
```

The server listens on http://localhost:3000, routes live under `/habits`.

---

## 7. Adding a new resource later (the payoff of this structure)

Say you add "check-ins". You'd create, in parallel to habits:
1. `prisma/schema.prisma` → add a `Checkin` model, then `npx prisma migrate dev`.
2. `src/schemas/checkin.schema.js` → its Zod shapes.
3. `src/controllers/checkins.controller.js` → its handler functions.
4. `src/routes/checkins.routes.js` → its Router.
5. `src/server.js` → ONE new line: `app.use("/checkins", checkinsRouter)`.

No existing file gets rewritten — you only *add*. That is what "separation of concerns" buys you.
