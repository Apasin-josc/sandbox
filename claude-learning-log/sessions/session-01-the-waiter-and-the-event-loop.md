# Session 01 — The Waiter and the Event Loop

**Date:** 2026-06-28
**Phase:** 0 — JavaScript the language

## What we covered
- Framed the real starting point: I already know Laravel + FastAPI, so the gap isn't "backend" — it's JavaScript, Node's async model, and npm.
- **The event loop via the restaurant analogy:**
  - Node = one waiter (single thread).
  - **Non-blocking** = the waiter takes the order, hands it to the kitchen, and serves other tables instead of standing around.
  - **I/O** (database, network, files) = "kitchen work" — handed off, non-blocking, Node's sweet spot.
  - **CPU work** (big loops, hashing, image resizing) = "waiter work" — the waiter does it himself; heavy CPU work *freezes the whole server for all users*.
  - Key contrast with FastAPI: there, one slow CPU task ties up one worker; in Node it can freeze the entire server.
- **`const` vs `let`** — proved by breaking it (`TypeError: Assignment to constant variable.`).
- **Reference semantics:** `const` locks the *binding* (can't point the variable at a new thing), NOT the contents. So `habit.streak = 5` and `habits.push(...)` work fine on a `const` object/array. Reassigning the whole variable crashes. This matters because DB records come back as objects.

## What I struggled with
- Initially thought Node was multi-threaded / everything runs simultaneously.
- Got the habit-tracker fit **backwards** at first: said "waiter work / bad fit." Walked it back myself by remembering a DB query is handed off (I/O) → it's actually a great fit.
- Didn't know what I/O meant (Input/Output — anytime the program waits on something outside itself).

## What clicked
- The waiter analogy — I can now reason about new cases with it (kitchen = I/O, waiter = CPU).
- *Why* companies want Node: most CRUD APIs are I/O-heavy = Node's strength.
- `const` = "can't repoint the variable," not "value never changes."

## English notes
- "future side project" (not "fute"), "simultaneously", "neither of those examples crashes" / "doesn't crash *either* of those."

## Pick up next time
- Phase 0 continues: **functions + arrow functions**, then **array methods** (`.map`/`.filter`/`.reduce`), then the boss fight: **callbacks → Promises → `async`/`await`**.
- First real build target: a script that fetches a public API and prints results (forces real async/await).
