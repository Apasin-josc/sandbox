import express from "express";

const app = express();

/**
 * middleware, a function that runs in between the request arriving and your route handler
 * read the raw body, parse the jSON, attach the result to req.body, then it passes it along to the route.
 */
app.use(express.json());

const habits = [
  { id: 1, name: "read", done: true },
];

app.get("/habits", (req, res) => {
    res.json(habits);
});

app.get("/habits/:id", (req, res) => {
  console.log(req.params);
  const habit = habits.find((h) => h.id === Number(req.params.id));
  res.json(habit);
});

/**
 * curl -X POST http://localhost:3000/habits \
  -H "Content-Type: application/json" \
  -d '{"name": "meditate"}'
 */
app.post("/habits", (req, res) => {
  const newHabit = { id: habits.length + 1, name: req.body.name, done: false };
  habits.push(newHabit);
  res.status(201).json(newHabit);
});

app.delete("/habits/:id", (req, res) => {
  const index = habits.findIndex((h) => h.id === Number(req.params.id));
  if (index === -1) return res.status(404).json({ error: "Habit not found" });
  habits.splice(index, 1);
  res.status(204).end();
});


/**
 * curl -X PATCH http://localhost:3000/habits/1 -H "Content-Type: application/json" -d '{"done": false}'
 */
app.patch("/habits/:id", (req, res) => {
  const index = habits.findIndex((h) => h.id === Number(req.params.id));
  if (index === -1) return res.status(404).json({ error: "Habit not found" });
  habits[index] = { ...habits[index], ...req.body };
  res.json(habits[index]);
});


app.listen(3000, () => {
    console.log("server running on http://localhost:3000");
});;