import { z } from "zod";

// Shape a client may send to CREATE a habit.
export const createHabitSchema = z.object({
  name: z.string().min(1),
});

// Shape for a partial UPDATE — every field optional (PATCH),
// but still type-checked when present.
export const updateHabitSchema = z
  .object({
    name: z.string().min(1),
    done: z.boolean(),
  })
  .partial();
