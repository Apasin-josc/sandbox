# Progress Tracker

**Currently in:** Phase 1 — Node runtime + npm
**Resume at:** Phase 1 → `npm init` / `package.json` / `node_modules`, then modules (CommonJS vs ESM), then built-ins (`fs`, `http`). Build: a raw HTTP server with the `http` module.

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

## Phase 1 — Node runtime + npm ← CURRENT
- [ ] `npm init`, `package.json`, `node_modules`, installing packages
- [ ] Modules: `require`/CommonJS vs `import`/ESM
- [ ] Built-ins: `fs`, `http`, `process.env`
- [ ] Build: raw HTTP server with the `http` module (one JSON route)

## Phase 2 — Express + habit tracker
- [ ] not started

## Phase 3 — Real-world
- [ ] not started

---

## Environment
- Node v26, npm 11
- Working dir: `phase_0/` has `hello.js` (`const`/`let`) and `functions.js` (functions, callbacks, map/filter/reduce)
