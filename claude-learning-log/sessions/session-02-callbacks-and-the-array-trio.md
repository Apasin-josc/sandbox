# Session 02 — Callbacks and the Array Trio

**Date:** 2026-06-29
**Phase:** 0 — JavaScript the language

## What we covered
- **Functions two ways:** declaration (`function add(){}`) vs arrow stored in a const (`const add = () => {}`). Syntax only — concept already known from PHP/Python.
- **Functions are first-class values:** a function can be stored in a variable, passed as an argument, and returned — just like a number or string.
- **Callbacks:** a function you hand to another function to run *later*. Built `doMath(a, b, operation)` to see it: `doMath(10, 5, addOld)`.
- **The key distinction:** `addOld` (hand over the recipe) vs `addOld()` (cook it now and hand over the result). Passing ≠ running. The callback runs only when the receiving function invokes it. → maps to `fs.readFile('f', done)` ✅ vs `fs.readFile('f', done())` ❌.
- **The array trio**, all powered by callbacks:
  - `.map` — transform every item → new array (does NOT mutate original).
  - `.filter` — keep items where the callback returns `true`.
  - `.reduce` — collapse an array to a single value via an accumulator + initial value.

## What I struggled with
- My phrasing "what else can you do with a function like a number/string" was unclear at first — clicked once reframed as "pass it as an argument."
- Kept describing the *result/flow* correctly but skipped saying the word **callback** out loud. Recognized the pattern faster than I verbalized it.

## What clicked
- The `addOld` vs `addOld()` distinction — passing vs running.
- **Traced `.reduce` by hand on the first try:** `[10,20,30]` with init `0` → acc 0+10=10, 10+20=30, 30+30=60. The method that usually gets cargo-culted — I understood it.
- `.map`/`.filter` return new arrays, don't mutate — connects to clean backend code.

## English notes
- "habits" not "habitats" (habitats = where animals live).

## Pick up next time — THE BOSS FIGHT
- **Async: callbacks → Promises → `async`/`await`.**
- Bridge from here: a Promise is what a callback becomes when the operation is *slow* (the kitchen bell from session 1). `await` = "wait for the kitchen but let other tables be served."
- Then the Phase 0 build target: a script that `fetch`es a public API and prints results using `async/await`.
