# Quiz — Session 1 (TS 101 Fundamentals)

**Date:** 2026-07-08 · **Score: 8 / 10**

Format: **Q** = question · **A** = my answer · **✔/✖** = verdict + correction.

---

**Q1.** Difference between a type *annotation* and *inference*? Example of each.
**A:** Annotation is when we put the type of the variable (string, number, boolean); inference is when TS figures out the type without the annotation.
**✔ 1/1** — Correct. Examples: annotation `let x: number = 5`; inference `let x = 5` (TS derives `number`).

**Q2.** Name the primitive types. Why no separate `int`/`float`?
**A:** number, string, boolean — TS doesn't need int/float, all goes in `number`.
**✔ 1/1** — Correct. (Also `null` and `undefined`.) JS has only one numeric type, so TS mirrors it: everything is `number`.

**Q3.** Why annotate parameters but skip the return type?
**A:** TS can infer the return type from the parameters but can't infer the parameters.
**✔ 1/1** — Correct. Params are inputs from outside (unknown until declared); the return is computed inside from the now-typed params, so TS traces it.

**Q4.** When Node runs a `.ts` file, what does it do to the types — does it check them? What checks them?
**A:** Node strips all the annotations and converts to plain JS; `npm run typecheck` checks them.
**✔ 1/1** — Correct. Node = strip + run (no checking). `tsc` (`npm run typecheck`) = check.

**Q5.** `let x = "hi";` then `x = 5;` — error or not? Why?
**A:** No issue, because we didn't use a strict annotation like `let x: string`, so reassigning `x = 5` later is fine.
**✖ 0/1** — **WRONG (key miss).** Inference is NOT "no type." `let x = "hi"` makes TS **infer and lock `x` as `string`**, exactly like annotating it. So `x = 5` **is** an error: `Type 'number' is not assignable to type 'string'`. **Inferred types are enforced just as strictly as annotated ones.**

**Q6.** `any` vs `unknown` — which is safer?
**A:** `any` can be any kind of value (object, array, string...); `unknown` is an unknown variable; I think `any` is safer.
**✖ 0.5/1** — Got `any`'s flexibility, but **safety is backwards.** `unknown` is the **safe** one: it forces you to *check/narrow* the value before using it. `any` is **dangerous** — it turns OFF type-checking entirely. Mnemonic: **`any` = anything goes (danger); `unknown` = prove it first (safe).**

**Q7.** Why is `"easy" | "medium" | "hard"` better than `string`? One thing it prevents.
**A:** So another dev knows Difficulty can only be easy/medium/hard — not hardcore or legendary.
**✔ 1/1** — Correct. Constrains to exactly the valid values + self-documents; rejects typos/invalid strings at compile time.

**Q8.** Enum threw `ERR_UNSUPPORTED_TYPESCRIPT_SYNTAX` in strip-only mode, but `let reps: number` ran fine. Why?
**A:** Node can't turn an enum into strippable code, but removing `: number` leaves plain JS (strippable).
**✔ 1/1** — Correct. Stripping only *removes*; `: number` is removable, an enum must be *generated* (real runtime code), which stripping can't do.

**Q9.** One thing `interface` can do that `type` can't, and vice versa.
**A:** interface can extend its properties; type can use unions.
**✔ 1/1** — Correct. (interface also *merges* — declaration merging; type also does primitives/tuples/intersections.)

**Q10.** For `totalVolume(sets: { reps: number; weight: number }[])`:
(a) inferred return type + how TS knows? (b) `totalVolume([{ reps: 10 }])` — fails? when?
**A:** (a) number. (b) It fails because we're not typing weight too.
**⚠ 0.5/1** — (a) ✅ `number` (TS traces `reduce` starting at `0` + `reps*weight`). (b) The object `{ reps: 10 }` is **missing the required `weight` field** → it fails **at compile-time** (tsc/editor), before running. Missed the *when* (compile-time) — that's the whole point: the bug never reaches runtime.

---

## To re-review next session
1. **Inference still gives a locked, enforced type** (Q5).
2. **`unknown` = safe, `any` = dangerous** (Q6).
3. Type mismatches are caught at **compile-time** (Q10).
