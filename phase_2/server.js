import express from "express";
import { PrismaClient } from "@prisma/client";

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
  const habit = await prisma.habit.create({
    data: { name: req.body.name },
  });
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
  try {
    const habit = await prisma.habit.update({
      where: { id: Number(req.params.id) },
      data: req.body,
    });
    res.json(habit);
  } catch (error) {
    //error.code === "P2025" — that's Prisma's specific code for "record not found." 
    if (error.code === "P2025") {
      return res.status(404).json({ error: "Habit not found" });
    }
    throw error; // anything else is a real bug — let it bubble up
  }
});

app.listen(3000, () => {
  console.log("server running on http://localhost:3000");
});;