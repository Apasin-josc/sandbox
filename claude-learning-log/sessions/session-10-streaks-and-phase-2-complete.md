# Session 10 — Streaks & Phase 2 Complete 🎉

**Date:** 2026-07-02
**Phase:** 2 — Express + the habit tracker (**COMPLETE**)

## What we covered

### Designed the streak algorithm (before coding)
Reasoned through a concrete example — check-ins on Jul 1 (×2), Jul 2, Jul 4 (nothing Jul 3):
- **Two check-ins on the same day count as ONE** → the unit is *days*, not check-ins.
- **A missing day (Jul 3) breaks the streak** → Jul 4 starts a fresh run.
- Streaks count **backwards from today** until the first gap.
- Algorithm: `timestamps → unique days → walk backward from today, counting consecutive days until a gap`.

### Built `GET /habits/:id/streak`
```js
import dayjs from "dayjs"; // DEFAULT import — no braces (vs named { prisma })

export async function getStreak(req, res) {
  const habitId = Number(req.params.id);
  const habit = await prisma.habit.findUnique({ where: { id: habitId } });
  if (!habit) return res.status(404).json({ error: "Habit not found" });

  const checkins = await prisma.checkin.findMany({ where: { habitId } });

  // 1. collapse timestamps → unique day-strings
  const days = new Set(
    checkins.map((c) => dayjs(c.createdAt).format("YYYY-MM-DD"))
  );

  // 2. walk backward from today, counting consecutive days
  let streak = 0;
  let cursor = dayjs();
  // grace rule: no check-in today yet → start from yesterday (forgiving)
  if (!days.has(cursor.format("YYYY-MM-DD"))) {
    cursor = cursor.subtract(1, "day");
  }
  while (days.has(cursor.format("YYYY-MM-DD"))) {
    streak++;
    cursor = cursor.subtract(1, "day");
  }

  res.json({ habitId, streak });
}
```

### Key concepts
- **`Set`** = array-like that auto-drops duplicates + `.has(x)` for fast membership. Perfect for "unique days" and "is this day present?".
- **`.map` → day-strings**: `dayjs(c.createdAt).format("YYYY-MM-DD")` strips the time so same-day check-ins collapse.
- **`dayjs().subtract(1, "day")`** walks dates backward and handles month/year boundaries.
- **Default vs named imports**: `import dayjs from "dayjs"` (default, no braces) vs `import { prisma } from ...` (named, braces). `X is not defined` almost always = missing import.
- **Debug tip**: `console.log(...days)` spreads a Set to print plain values (`Set(n){...}` otherwise). Remove debug logs before finishing.
- **Design decision — grace rule**: forgiving (no check-in today but yes yesterday → streak alive, start from yesterday) vs strict (missing today → 0). Chose forgiving.

### Verified with real data
Streak went 1 → 2 as check-ins spanned two consecutive real days (Jul 1 → Jul 2). Proved BOTH halves: same-day dedup (Set) AND consecutive-day counting (backward walk).

## What clicked
- Turned my own plain-English reasoning into a working algorithm.
- `Set` for dedup + membership; date normalization with dayjs.
- Default vs named imports.

## 🎉 PHASE 2 IS COMPLETE
The habit tracker is a real, working backend:
- Full CRUD on habits (Prisma + Postgres, persistent)
- Zod validation (clean 400s)
- Global error handler (bad JSON → 400, crashes → 500, no leaks)
- One-to-many relation: habits → check-ins (FK, referential integrity)
- Check-in endpoints + a self-designed streak endpoint
- Clean project structure (routes/controllers/schemas/lib/middleware), REST Client, `structure.md`

## Pick up next time — PHASE 3 (the app goes pro)
**No new folder** — Phase 3 happens INSIDE this codebase. Strongly consider graduating `phase_2/` → its own repo named `habit-tracker/`.
- **Auth (JWT)**: register/login, protect routes (habits belong to a user → likely a `User` model + relation).
- **Tests**: vitest or `node:test` + supertest against the controllers.
- **Deploy**: Railway/Render + managed Postgres.
- **Dockerfile** for the app (now write our OWN image — contrast with pulling `postgres:16`).
- **TypeScript**: migrate the codebase (now the "why" is felt; Zod's `z.infer` gives types for free).

### Optional Phase 2 polish (small, not new concepts)
- `.refine()` to reject empty PATCH bodies.
- Switch the FK to `ON DELETE CASCADE` so deleting a habit removes its check-ins (currently `RESTRICT` blocks it).

## Environment reminder
- `docker start habit-postgres` before coding. Prisma **v6**. `dayjs`, `zod` installed. Run: `npm run dev`.
- Endpoints: `/habits`, `/habits/:id`, `/habits/:id/checkins`, `/habits/:id/streak`.
