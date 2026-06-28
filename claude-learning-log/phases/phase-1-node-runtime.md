# Phase 1 — Node runtime + npm

**Goal:** Understand what Node *is* as a runtime, how packages work, and the built-in modules — before reaching for frameworks.

**Done when:** I've written a working HTTP server using only the built-in `http` module (no Express), and it feels annoying enough that I *want* Express.

## Lessons
1. **The runtime & project setup** ⬜
   - `node script.js`, the REPL, `npm init -y`, what `package.json` is (like `composer.json` / `requirements.txt`).
   - Installing packages, what `node_modules` and `package-lock.json` are.
2. **Modules** ⬜
   - `require`/`module.exports` (CommonJS) vs `import`/`export` (ES modules). Know both exist; pick ESM (`"type": "module"`).
3. **Built-in modules** ⬜
   - `fs` — reading/writing files (I/O — kitchen work).
   - `http` — the raw server.
   - `path`, `process` (env vars via `process.env`).

## Build target
A raw HTTP server with the `http` module: one route `GET /habits` that returns hardcoded JSON. Notice how much manual work routing/parsing is. That ache is the motivation for Phase 2.
