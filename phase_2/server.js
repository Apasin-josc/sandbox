import express from "express";
import { PrismaClient } from "@prisma/client";
import { z } from "zod";

const createHabitSchema = z.object({
  name: z.string().min(1),
});

const updateHabitSchema = z.object({
  name: z.string().min(1),
  done: z.boolean(),
}).partial();
//.refine() instead of partial can enforce "at least one key present"
//this because when we send a empty {} zod is letting it pass, it doesn't change anything but well just FYI


//const createHabitSchema = z.object({ name: z.string().min(1) }).strict();
// now { name: "read", progress: 80 } → FAILS if i don't type the strict the progress is going to pass but is not going
//to write progress on the database it just passes and thats all, extra fields just vanish.


const prisma = new PrismaClient();
const app = express();

/**
 * middleware, a function that runs in between the request arriving and your route handler
 * read the raw body, parse the jSON, attach the result to req.body, then it passes it along to the route.
 */
app.use(express.json());

const habits = [
  { id: 1, name: "read", done: true },
];

app.get("/habits", async (req, res) => {
  const habits = await prisma.habit.findMany();
  res.json(habits);
});

app.get("/habits/:id", async (req, res) => {
  const habit = await prisma.habit.findUnique({ where: { id: Number(req.params.id) } });
  if (!habit) return res.status(404).json({ error: "Habit not found" });
  res.json(habit);
});

/**
 * curl -X POST http://localhost:3000/habits 
 * -H "Content-Type: application/json" 
 * -d '{"name": "meditate"}'
 */
app.post("/habits", async (req, res) => {
  const result = createHabitSchema.safeParse(req.body);
  //returns { success: true, data } or { success: false, error }
  if (!result.success) {
    return res.status(400).json({ error: result.error.issues });
  }
  const habit = await prisma.habit.create({ data: result.data });
  res.status(201).json(habit);
});

app.delete("/habits/:id", async (req, res) => {
  try {
    const habit = await prisma.habit.delete({
      where: { id: Number(req.params.id) }
    });
    res.status(204).end()
  } catch (error) {
    if (error.code === "P2025") {
      return res.status(404).json({ error: "Habit not found" });
    }
    throw error;
  }
});


/**
 * curl -X PATCH http://localhost:3000/habits/1 -H "Content-Type: application/json" -d '{"done": false}'
 */
app.patch("/habits/:id", async (req, res) => {
  const result = updateHabitSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ error: result.error.issues });
  }
  try {
    const habit = await prisma.habit.update({
      where: { id: Number(req.params.id) },
      data: result.data,
    });
    res.json(habit);
  } catch (error) {
    if (error.code === "P2025") return res.status(404).json({ error: "Habit not found" });
    throw error;
  }
});

app.listen(3000, () => {
  console.log("server running on http://localhost:3000");
});;