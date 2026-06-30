# Progress Tracker

**Currently in:** Phase 2 — Express + the habit tracker
**Resume at:** Phase 2 → install Express, rebuild the `/habits` route the clean way (`app.get`, `res.json`). Then project structure, PostgreSQL + Prisma, env vars, validation (Zod).

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
- [ ] Install Express; rebuild `/habits` route (`app.get`, `res.json`) — see the boilerplate collapse
- [ ] Routing, middleware, req/res in Express
- [ ] PostgreSQL + Prisma (schema, migrations, queries)
- [ ] Project structure, env vars, error handling, validation (Zod)
- [ ] Build the habit-tracker API (CRUD + check-ins + streak endpoint)

## Phase 3 — Real-world
- [ ] not started

---

## Environment
- Node v26, npm 11
- Working dir: `phase_0/` (`hello.js`, `functions.js`, `async1.js`, `async2.js`); `phase_1/` (`package.json` + dayjs, `math.js`/`app.js` ESM, `server.js` raw HTTP server)
