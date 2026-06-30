# Session 04 — npm, Modules, and a Raw Server

**Date:** 2026-06-29
**Phase:** 1 — Node runtime + npm (COMPLETED this session)

## What we covered

### npm & dependency files
- `npm init -y` → creates `package.json`. Same *job* as Laravel's `composer.json` / Python's `requirements.txt`: declares the libraries the project depends on.
- `npm install dayjs` → created `node_modules/` (the actual downloaded code, like `vendor/` / `venv/`) and `package-lock.json`.
- **`package.json` vs `package-lock.json`:**
  - `package.json` = human-authored **intent**, with flexible version *ranges* (`^1.11.21` = "1.x, any newer minor/patch"). Also holds scripts, metadata, `"type"`.
  - `package-lock.json` = machine-generated **exact snapshot**: pinned version + `resolved` (download URL) + `integrity` (sha512 hash → byte-for-byte verification). Never hand-edit it.
  - Analogy: package.json = shopping list ("eggs, any brand"); lock = receipt ("Eggland, lot #1234").
- **Cross-machine rule:** commit `package.json` + `package-lock.json`; do NOT commit `node_modules` (it's in `.gitignore`). On another laptop: `npm install` rebuilds `node_modules` identically from the lock.

### Modules (CommonJS vs ESM)
- Two systems exist. **CommonJS** (`require`/`module.exports`) is Node's default for `.js` — that's why `import` first threw `Cannot use import statement outside a module` (note the `cjs/loader` in the stack).
- **ESM** (`import`/`export`) is the modern standard. Enable it with `"type": "module"` in `package.json` (or `.mjs`).
- ESM is **strict about file extensions**: `import { x } from "./math.js"` works; `"./math"` fails.
- `export` is the gatekeeper — only exported things are importable; un-exported = private to the file.
- **We use ESM going forward.**

### Built-in modules + the raw HTTP server (the boss)
- Built-in modules (e.g. `http`) ship inside Node — no `npm install`, no `node_modules`. The `node:` prefix (`import http from "node:http"`) marks them as built-in.
- `http.createServer((req, res) => {...})` — the handler is a **callback** that runs **once per incoming request** (proven by logging + refreshing).
- `server.listen(3000, ...)` keeps the process alive forever (waiting for requests) — unlike scripts that exit.
- **No auto-reload:** editing the file does nothing until you restart. Fix = `node --watch server.js`.
- **Client/server split:** server-side `console.log` → the **terminal**; `res.end(...)` → what the **browser** shows; browser DevTools console = client-side JS only. Different worlds.
- `req.method` (GET) + `req.url` (the path) = the basis of **routing**. (Discovered the browser also auto-requests `/favicon.ico` — the mysterious "2nd request".)
- Built a real route: `GET /habits` → `res.writeHead(200, {"Content-Type": "application/json"})` + `res.end(JSON.stringify(habits))`; everything else → 404.
- **`JSON.stringify`:** the network can only carry **text**, not live JS objects. `stringify` flattens an object (in memory) into a JSON text string that can travel; the receiver reassembles it. `typeof obj` = "object" → `typeof JSON.stringify(obj)` = "string". (Mailing furniture: flat-pack the couch to ship it.)
- **Content-Type** = the label telling the receiver how to interpret the bytes (`application/json` = "parse as data" vs `text/html` = "render as page").

## What I struggled with
- Thought `setTimeout`-style "runs once" applied to the server handler — guessed the request callback runs once at startup; corrected to **per request** by testing.
- Edited the file but saw no change — didn't realize **Node has no auto-reload** (needed restart / `--watch`).
- Looked for server `console.log` output in the **browser** console instead of the terminal — client/server confusion.
- `JSON.stringify` didn't click at first ("do we put everything as JSON in the browser?") — landed via the object-vs-text / `typeof` demo and the mailing-furniture analogy.

## What clicked
- package.json (intent) vs package-lock.json (exact, hashed snapshot), and which to commit.
- A web server = **a function that runs once per request**. Frameworks are wrappers around that.
- Why raw `http` doesn't scale: manual `if/else` routing, repeated `writeHead`/`stringify`, hand-parsing params and request bodies. → the reason Express exists.

## Pick up next time — PHASE 2 begins
- Install **Express**; rebuild the `/habits` route the clean way (`app.get("/habits", ...)`, `res.json(...)`). Watch the raw-server pain collapse.
- Then: project structure, **PostgreSQL + Prisma**, env vars, validation (Zod) — building toward the habit-tracker API.
