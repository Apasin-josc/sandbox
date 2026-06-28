# Phase 0 — JavaScript the language

**Goal:** Get fluent in JS itself before touching servers. The runtime is Node; the language is JavaScript. Most "Node is confusing" pain is actually "JavaScript is new."

**Done when:** I can write a small script that fetches a public API and prints the results using `async/await`, with no copy-paste.

## Lessons
1. **Variables & types** ✅
   - `const` vs `let` (never `var`). `const` locks the binding, not the contents.
2. **Functions** ⬜
   - Regular functions vs arrow functions (`const f = (x) => x + 1`). Where arrow functions matter.
3. **Objects & arrays** ⬜
   - Destructuring (`const { name } = habit`), spread (`...`), template literals.
4. **Array methods** ⬜ — used constantly in real code
   - `.map` (transform each), `.filter` (keep some), `.reduce` (collapse to one value).
   - Coming from Python: like list comprehensions, but methods.
5. **Async — the boss fight** ⬜
   - **Callbacks** (the old way, "callback hell").
   - **Promises** (`.then()`, `.catch()`).
   - **`async`/`await`** (the modern way — looks synchronous, isn't).
   - Connect back to the waiter: `await` = "wait for the kitchen, but let other tables be served meanwhile."

## Noise to ignore for now
Deep `this` rules, prototypes, the class-vs-prototype debate, TypeScript. Real, but not the bottleneck yet.

## Build target
A single `.js` file that uses `fetch` (built into Node 26) to call a free public API (e.g. a jokes or weather API), `await`s the response, and prints a couple of fields. This forces real async — no faking it.
