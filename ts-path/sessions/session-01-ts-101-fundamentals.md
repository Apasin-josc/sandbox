# Session 01 — TS 101 Fundamentals (5-min review)

**Date:** 2026-07-08 · **Folder:** `ts-path/101/`

## The one big idea
```
        YOUR .ts FILE
        /           \
   node file.ts     tsc --noEmit  (npm run typecheck)
   = RUN            = CHECK
   strips types,    reads types,
   NO checking      reports errors
```
- **Node runs** by *stripping* type annotations then executing the JS. It NEVER checks types.
- **`tsc` (the `typescript` package) checks** types. That checking is the entire point of TS.
- Types are "decoration" that only *mean* something because `tsc` (and your editor's live squiggles) enforce them.

## Concepts
- **Annotation vs inference** — annotation = you write the type (`let x: number`). Inference = TS figures it out from the value (`let x = 5` → number). Annotate where TS can't guess (mainly function **params**); let inference handle the rest. Over-annotating is a smell.
- **Primitives:** `string`, `number` (no int/float split), `boolean`, `null`, `undefined`.
- **`any` vs `unknown`:** `any` = turn OFF checking (avoid). `unknown` = "must narrow before use" (safe any).
- **Functions:** must annotate **params** (inputs from outside — TS can't know them); **return type is inferable** (TS traces the body). `?` = optional param, `= x` = default. `void` = returns nothing (usually inferred, annotate only for clarity).
- **Objects & arrays:** `{ reps: number; weight: number }`, arrays as `X[]`. Typos on fields (`.rep`) are caught at compile time → saves you from silent `undefined`/`NaN` at runtime.
- **Union & literal types:** `number | string` (one of several). Literals constrain to exact values: `"easy" | "medium" | "hard"` — better than `string` because typos/invalid values are rejected and it self-documents. **Narrowing:** `if (typeof x === "string")` → TS knows the type inside.
- **Enums:** named constant set that emits **real runtime code** (not just types) → fails in Node **strip-only mode** (`ERR_UNSUPPORTED_TYPESCRIPT_SYNTAX`); needs a build/transform (`node --experimental-transform-types`). Prefer **literal unions** (or `as const` objects) in modern TS; use enums for runtime iteration or in codebases/frameworks (NestJS) that use them.
- **`interface` vs `type`:** both describe object shapes. `type` also does unions/primitives/tuples; `interface` can `extends` and **merge** (declaration merging — used to add `req.user` to Express). Default to `type`; use `interface` when you need extend/merge.

## Examples
```ts
let reps = 10;                       // inferred number
let status: "todo" | "done" = "todo"; // literal union
function volume(reps: number, weight: number) { return reps * weight; } // params annotated, return inferred (number)
const sets = [{ reps: 10, weight: 50 }];
const volumes = sets.map((s) => s.reps * s.weight); // s typed automatically → number[]
```

## Next
- Bridge concepts: **generics** + **utility types** (`Partial`/`Pick`/`Omit`/`Record`) → then start React.
- **Quiz score: 8 / 10.** Missed: (Q5) thought an *inferred* variable has "no type" and can be reassigned freely — WRONG, inference locks the type just like annotation (`let x = "hi"; x = 5` errors). (Q6) had it backwards — **`unknown` is the safe one, `any` is dangerous**. (Q10) forgot the miss is caught at **compile-time**. Re-review these next session.
