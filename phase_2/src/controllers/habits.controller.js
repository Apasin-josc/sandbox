import { prisma } from "../lib/prisma.js";
import {
  createHabitSchema,
  updateHabitSchema,
} from "../schemas/habit.schema.js";
import dayjs from "dayjs";

// GET /habits
export async function listHabits(req, res) {
  const habits = await prisma.habit.findMany();
  res.json(habits);
}

// GET /habits/:id
export async function getHabit(req, res) {
  const habit = await prisma.habit.findUnique({
    where: { id: Number(req.params.id) },
  });
  if (!habit) return res.status(404).json({ error: "Habit not found" });
  res.json(habit);
}

// POST /habits
export async function createHabit(req, res) {
  const result = createHabitSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ error: result.error.issues });
  }
  const habit = await prisma.habit.create({ data: result.data });
  res.status(201).json(habit);
}

// PATCH /habits/:id
export async function updateHabit(req, res) {
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
    if (error.code === "P2025") {
      return res.status(404).json({ error: "Habit not found" });
    }
    throw error;
  }
}

// DELETE /habits/:id
export async function deleteHabit(req, res) {
  try {
    await prisma.habit.delete({ where: { id: Number(req.params.id) } });
    res.status(204).end();
  } catch (error) {
    if (error.code === "P2025") {
      return res.status(404).json({ error: "Habit not found" });
    }
    throw error;
  }
}


export async function createCheckin(req, res) {
  const habitId = Number(req.params.id);                              // the NUMBER
  const habit = await prisma.habit.findUnique({ where: { id: habitId } }); // the OBJECT
  if (!habit) {
    return res.status(404).json({ error: "Habit not found" });
  }
  const checkin = await prisma.checkin.create({ data: { habitId } }); // await!
  res.status(201).json(checkin);
}



export async function listHabitsCheckin(req, res) {
  const habitId = Number(req.params.id);
  const habit = await prisma.habit.findUnique({ where: { id: habitId } });
  if (!habit) {
    return res.status(404).json({ error: "Habit not found" });
  }
  const checkins = await prisma.checkin.findMany({
    where: { habitId },
    orderBy: { createdAt: "desc" },
  });
  res.json(checkins);
}

export async function getStreak(req, res) {
  const habitId = Number(req.params.id);
  const habit = await prisma.habit.findUnique({ where: { id: habitId } });
  if (!habit) return res.status(404).json({ error: "Habit not found" });
  const checkins = await prisma.checkin.findMany({ where: { habitId } });
  const days = new Set(
    checkins.map((c) => dayjs(c.createdAt).format("YYYY-MM-DD"))
  );

  let streak = 0
  let cursor = dayjs();

  if (!days.has(cursor.format("YYYY-MM-DD"))) {
    cursor = cursor.subtract(1, "day");
  }

  while (days.has(cursor.format("YYYY-MM-DD"))) {
    streak++;
    cursor = cursor.subtract(1, "day");
  }

  res.json({ habitId, streak });
}