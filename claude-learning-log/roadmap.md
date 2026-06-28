# Node.js Roadmap (calibrated for someone who already knows backend)

Built around: knows Laravel + FastAPI, ~4 hrs/week, goal = habit-tracker API + employability.
Principle: **skip "what is a backend" — attack what Node does *differently*.**

Detailed lesson notes + build tasks live in `phases/`.

---

## Phase 0 — JavaScript the language (~2–3 weeks)
The runtime is Node; the language is JavaScript. Can't skip it.
- `const`/`let`, objects, arrays, destructuring, arrow functions, template literals
- Array methods: `.map`, `.filter`, `.reduce`
- **The boss fight: callbacks → Promises → `async`/`await`.** This is the whole game.
- **Noise to ignore for now:** deep `this`, prototypes, classes philosophy, TypeScript.
- *Build:* small single-file scripts (`node script.js`). One that fetches a public API and prints results (forces real `async/await`).

## Phase 1 — Node runtime + npm (~1 week)
- `node`, `npm init`, `package.json`, installing packages, `node_modules`
- Built-ins: `fs` (files), `http` (raw server)
- `import`/`require` (ES modules vs CommonJS — know the difference)
- *Build:* a raw HTTP server with the built-in `http` module, one endpoint. Painful on purpose — to appreciate Express.

## Phase 2 — Express + the habit tracker (~3–4 weeks)
- Express: routing, middleware, req/res (concepts known — just new syntax)
- DB: **PostgreSQL + Prisma** (closest to Laravel's ORM comfort)
- Env vars, project structure, error handling, validation (Zod)
- *Build:* **the habit-tracker API** — CRUD for habits, daily check-ins, a "streak" endpoint. Portfolio piece.

## Phase 3 — Real-world (ongoing)
- Auth (JWT), one round of tests, deploy (Railway/Render), Docker basics
- *Then* consider TypeScript — by now he'll feel why people want it.

## Hard "not yet" list
Microservices, GraphQL, Nest.js, Kubernetes, "Node design patterns" — none until Phase 2 ships. They're real but not the bottleneck. The bottleneck is the async model + JS muscle memory.
