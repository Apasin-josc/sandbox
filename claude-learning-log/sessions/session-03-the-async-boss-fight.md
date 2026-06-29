# Session 03 — The Async Boss Fight

**Date:** 2026-06-29
**Phase:** 0 — JavaScript the language (COMPLETED this session)

## What we covered
- **The event loop, proven empirically** with `setTimeout`:
  - `console.log("1"); setTimeout(()=>log("2"),1000); console.log("3")` → prints `1 3 2`. Node hands the timer to the kitchen and keeps going.
  - **The killer detail:** even `setTimeout(fn, 0)` still prints `1 3 2`. `0` doesn't mean "now" — it means "as soon as possible, but *after* the current synchronous code finishes."
  - **The rule:** synchronous code ALWAYS runs first; a handed-off async callback waits until the current top-to-bottom pass is done.
- **Why you can't write async calls flat (the way FastAPI lets you):** an async call hands off and moves on instantly, so the result is NOT ready on the next line — it only exists later, inside the callback. That's what forces nesting → the "pyramid of doom" / callback hell.
- **Promises** = a kitchen ticket / IOU for a value that isn't ready yet. Three states: **pending → fulfilled (resolved)** or **pending → rejected**.
- **`async`/`await`:**
  - `await` = "pause here until this ticket stops being pending, then give me the value" — while Node keeps serving other work.
  - `await` only works inside an `async` function, because `await` *pauses* the function — a normal function must run start-to-finish. Marking it `async` announces "my answer is coming later."
  - An `async` function ALWAYS returns a Promise.
  - Result: async behavior, flat synchronous-LOOKING code. Pyramid gone.
- **Error handling:**
  - `try/catch` catches *rejected* promises.
  - **Block scope gotcha:** a `const` declared inside `try { }` is only visible inside those braces (same rule as session 1). Fix: put the success `console.log` inside the `try`.
  - **THE #1 fetch gotcha:** `fetch` only rejects on *network* failure — NOT on 404/500. A 404 is a *fulfilled* promise carrying bad news, so `catch` never fires. Must check `res.ok` yourself and `throw new Error(...)` to convert it into a real failure that hits `catch`. Check `res.ok` BEFORE parsing the body.

## What I struggled with
- Predicted `setTimeout(fn, 0)` would print `1 2 3` — thought 0 delay = runs inline. The surprise (`1 3 2`) is what made the event loop click.
- Couldn't initially say *why* async calls can't be written flat — got there by reasoning that the data isn't ready on the next line.
- Mixed up Promise *states* (pending/fulfilled/rejected) with how you *handle* them (`try/catch`).
- Needed help wiring the `res.ok` + `throw` check — built it together.

## What clicked
- The event loop, for real, watching `3` beat `2`.
- The full chain: callback → why nesting → Promise (ticket) → async/await (flat code).
- `async` = "answer coming later"; async functions always return a Promise.
- The fetch 404 gotcha — turned "successful bad news" into a real error via `throw`.

## Build target — DONE
`phase_0/async2.js` fetches a live GitHub user via `fetch` + `async/await`, parses JSON, prints name + repo count, and handles failures with `try/catch` + `res.ok`/`throw`. That WAS the Phase 0 build target.

## Pick up next time — PHASE 1
- Node runtime + npm: `npm init`, `package.json`, `node_modules`, installing packages.
- Modules: `require`/CommonJS vs `import`/ESM.
- Built-ins: `fs`, `http`, `process.env`.
- Build: a raw HTTP server with the built-in `http` module (one route returning JSON) — painful on purpose, to make Express feel earned.
