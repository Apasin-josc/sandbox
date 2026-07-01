# Session 08 — Zod Validation

**Date:** 2026-07-01
**Phase:** 2 — Express + the habit tracker (in progress)

## What we covered

### Why Zod (and why TS doesn't replace it)
- The API was trusting raw client input — no gatekeeper. Rule: **never trust client input.**
- Zod = runtime schema validation at the boundary → reject bad requests with a clean `400` before they hit Prisma. ≈ **Pydantic** (FastAPI) / Form Requests (Laravel).
- **TS ≠ Zod — different problems:**
  - TypeScript is **compile-time**, then erased. It checks *your code*, can't see runtime data. `req.body as {name: string}` is a *promise to the compiler* the client can break.
  - Zod is **runtime**. It validates *unknown data from the outside world*.
  - Analogy: TS = spell-check (your typos); Zod = security guard checking IDs (strangers at the door).
  - Bonus synergy: `z.infer<typeof schema>` generates the TS type from the schema → one source of truth for validation + types. That's why TS projects love Zod.

### Zod vs Prisma schema (two layers, defense in depth)
- **Prisma schema** guards the **database** (data at rest): column types, `NOT NULL`, `@unique`. Fires late, throws ugly `500`s, can't express rich rules.
- **Zod** guards the **incoming request** (data at the door): min/max length, formats, ranges. Fires early, clean `400`s.
- Different shapes for different jobs: DB says "what a Habit IS"; Zod says "what a client may SEND" (client sends `name`, never `id`/`createdAt`).

### Writing schemas
```js
import { z } from "zod";
const createHabitSchema = z.object({ name: z.string().min(1) });
```
- `z.object({...})` = expect an object; `name: z.string()` = must be a string; `.min(1)` = **at least 1 character** (rejects `""`). For strings `.min(n)` = length; for numbers it's the value.
- **Unknown keys: default = STRIP + pass** (extra fields silently dropped — `{name, progress}` → `{name}`). Opt into rejection with `.strict()`.
- **`.partial()`** makes every field optional (for PATCH). Fields are still type-checked when present — `.partial()` only makes them optional, not typeless.

### Wiring into routes (safeParse pattern)
- `schema.parse(data)` → returns clean data but **throws** on invalid.
- `schema.safeParse(data)` → returns `{ success: true, data }` or `{ success: false, error }` (no throw). Preferred for validation.
```js
const result = createHabitSchema.safeParse(req.body);
if (!result.success) return res.status(400).json({ error: result.error.issues });
const habit = await prisma.habit.create({ data: result.data });
```
- **Pass `result.data`, NOT `req.body`, to Prisma** — `result.data` is validated + stripped; `req.body` is raw untrusted input. Using `req.body` would bypass Zod entirely.
- Applied to both `POST` (create schema, `name` required) and `PATCH` (`.partial()` schema).

### Status codes: 4xx vs 5xx
- **`4xx` = client error** (their fault): `400` bad input, `404` not found, `401` unauthenticated.
- **`5xx` = server error** (my code broke): `500`.
- Validation failure = `400`. Using `500` there would falsely blame the server for the client's bad input.

### Middleware pipeline gotcha (found by accident)
- Sent `{"done": yes}` (unquoted `yes` = **invalid JSON**). It died at **`express.json()`** (JSON.parse) *before* reaching the route/Zod → ugly HTML `500`.
- Lesson: the pipeline is `express.json()` → route → Zod. Malformed JSON fails at stage 1.
- **Known gap (polish list, not urgent):** add error-handling middleware to catch body-parser errors → return `400 "Invalid JSON"` instead of a `500`.
- To test Zod's *type* check, send valid JSON with a wrong type: `{"done": "yes"}` → reaches Zod → `400 "expected boolean, received string"`. ✓

### Empty PATCH body `{}`
- Passes: `.partial()` makes empty valid → Prisma runs `update` with empty `data` → changes nothing, returns the row unchanged. Not "ignored" — a real no-op update.
- Optional: reject empty updates with `.refine()` ("at least one field"). Nice-to-have.

## What I struggled with
- Thought TS would remove the need for Zod (compile-time vs runtime confusion).
- Didn't get `.min(1)` at first (= minimum 1 character).
- Thought validations should live in `schema.prisma` (DB layer vs request layer confusion).
- Predicted `{name, progress:80}` would FAIL — actually Zod strips extras and passes by default.
- Tested with `{"done": yes}` (invalid JSON) and got a 500 — the request never reached Zod.

## What clicked
- TS guards *your code*, Zod guards *your data* — different jobs.
- Default strip vs `.strict()`; `.partial()` for PATCH.
- `safeParse` → pass `result.data` (validated) to the DB, never raw `req.body`.
- 4xx (client) vs 5xx (server), and why validation = 400.
- The middleware order (json parse → route → validation).

## Pick up next time
- **Project structure:** `server.js` is getting long — split into routes / controllers / (services) and move the Zod schemas out. Understand the separation-of-concerns layout.
- Optional polish: JSON-error middleware (→400), `.refine()` for empty PATCH.
- Then the habit-tracker features: daily **check-ins** + **streak** endpoint.

## Environment reminder
- Start Docker Desktop + `docker start habit-postgres` before coding.
- Prisma pinned to **v6**. `zod` installed.
- `phase_2/server.js` now has full CRUD on Prisma + Zod validation on POST/PATCH.
