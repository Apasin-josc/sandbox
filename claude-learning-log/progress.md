# Progress Tracker

**Currently in:** Phase 2 — Express + the habit tracker
**Resume at:** Phase 2 → **validation with Zod** (validate POST/PATCH bodies → clean 400s instead of 500s). Then project structure (split up `server.js`), then check-ins + streak endpoint.

---

## Phase 0 — JavaScript ✅ COMPLETE
- [x] Mental model: Node is single-threaded + non-blocking (the waiter analogy)
- [x] I/O vs CPU work — and why a habit tracker (I/O-heavy) fits Node
- [x] `const` vs `let`
- [x] Reference semantics: `const` locks the binding, not the contents (can mutate objects/arrays)
- [x] Functions + arrow functions (declaration vs arrow)
- [x] Functions are first-class values (store / pass / return)
- [x] Callbacks (passing `fn` vs calling `fn()`)
- [x] Array methods: `.map`, `.filter`, `.reduce`
- [x] Event loop proven: `1 3 2`, and `setTimeout(fn,0)` still defers
- [x] Promises (pending → fulfilled / rejected)
- [x] `async` / `await` (flat code; async fns always return a Promise)
- [x] Error handling: `try/catch`, block scope, the `fetch`/`res.ok`/404 gotcha
- [x] Build: `phase_0/async2.js` fetches a public API + prints results

## Phase 1 — Node runtime + npm ✅ COMPLETE
- [x] `npm init`, `package.json`, `node_modules`, installing packages (`dayjs`)
- [x] `package.json` (intent + ranges) vs `package-lock.json` (exact + integrity hash); commit lock, gitignore node_modules
- [x] Modules: CommonJS (default) vs ESM (`"type": "module"`, strict extensions); `export` as gatekeeper
- [x] Built-in `http`; `req.method` + `req.url`; client/server split; `node --watch` (no auto-reload)
- [x] Build: raw HTTP server with `GET /habits` returning JSON (+ 404), `JSON.stringify` / Content-Type
- [x] Felt why raw `http` doesn't scale → motivation for Express

## Phase 2 — Express + habit tracker ← CURRENT
- [x] Install Express; rebuild `/habits` (`app.get`, `res.json`) — boilerplate collapsed
- [x] Routing, middleware (`express.json()`), req/res, route vs query params, status codes
- [x] Full in-memory CRUD: GET list, GET :id, POST (201), PATCH (spread-merge), DELETE (204)
- [x] PostgreSQL + Prisma: Docker Postgres, schema + migration, **full CRUD on Prisma** (findMany/findUnique/create/update/delete), P2025→404 via try/catch, persistence proven
- [ ] Validation with Zod (reject bad POST bodies)
- [ ] Project structure (routes/controllers/services), env vars, error handling
- [ ] Habit-tracker API extras: daily check-ins + streak endpoint

## Phase 3 — Real-world
- [ ] not started

---

## Environment
- Node v26, npm 11
- Working dir: `phase_0/` (JS basics + async); `phase_1/` (raw HTTP server); `phase_2/` (Express + Prisma — `server.js`, `prisma/schema.prisma`, migrations, `.env`)
- **Docker:** container `habit-postgres` (postgres:16) on `localhost:5432`, DB `habits`, pw `secret`. If stopped: start Docker Desktop, then `docker start habit-postgres`.
- **Prisma pinned to v6** — do NOT upgrade to 7 mid-learning (v7 changed config + needs driver adapters, docs haven't caught up).
