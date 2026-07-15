import { Prisma } from "@prisma/client";
import type { Request, Response } from "express";
import dayjs from "dayjs";
import { prisma } from "../lib/prisma.ts";
import {
  createHabitSchema,
  updateHabitSchema,
} from "../schemas/habit.schema.ts";

// `req.user!.id` — the "!" asserts req.user exists. It's guaranteed here because
// the `authenticate` middleware runs before every one of these routes.

// GET /habits
export async function listHabits(req: Request, res: Response) {
  const habits = await prisma.habit.findMany({
    where: { userId: req.user!.id },
  });
  res.json(habits);
}

// GET /habits/:id
export async function getHabit(req: Request, res: Response) {
  const habit = await prisma.habit.findFirst({
    where: { id: Number(req.params.id), userId: req.user!.id },
  });
  if (!habit) return res.status(404).json({ error: "Habit not found" });
  res.json(habit);
}

// POST /habits
export async function createHabit(req: Request, res: Response) {
  const result = createHabitSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ error: result.error.issues });
  }
  const habit = await prisma.habit.create({
    data: { ...result.data, userId: req.user!.id }, // ← stamp the owner
  });
  res.status(201).json(habit);
}

// PATCH /habits/:id
export async function updateHabit(req: Request, res: Response) {
  const result = updateHabitSchema.safeParse(req.body);
  if (!result.success) return res.status(400).json({ error: result.error.issues });

  const id = Number(req.params.id);
  const existing = await prisma.habit.findFirst({ where: { id, userId: req.user!.id } });
  if (!existing) return res.status(404).json({ error: "Habit not found" });

  const habit = await prisma.habit.update({ where: { id }, data: result.data });
  res.json(habit);
}

// DELETE /habits/:id
export async function deleteHabit(req: Request, res: Response) {
  const id = Number(req.params.id);
  const existing = await prisma.habit.findFirst({ where: { id, userId: req.user!.id } });
  if (!existing) return res.status(404).json({ error: "Habit not found" });
  try {
    await prisma.habit.delete({ where: { id } });
    res.status(204).end();
  } catch (error) {
    if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === "P2025") {
      return res.status(404).json({ error: "Habit not found" });
    }
    throw error;
  }
}

// POST /habits/:id/checkins
export async function createCheckin(req: Request, res: Response) {
  const habitId = Number(req.params.id);
  const habit = await prisma.habit.findFirst({ where: { id: habitId, userId: req.user!.id } });
  if (!habit) {
    return res.status(404).json({ error: "Habit not found" });
  }
  const checkin = await prisma.checkin.create({ data: { habitId } });
  res.status(201).json(checkin);
}

// GET /habits/:id/checkins
export async function listHabitsCheckin(req: Request, res: Response) {
  const habitId = Number(req.params.id);
  const habit = await prisma.habit.findFirst({ where: { id: habitId, userId: req.user!.id } });
  if (!habit) {
    return res.status(404).json({ error: "Habit not found" });
  }
  const checkins = await prisma.checkin.findMany({
    where: { habitId },
    orderBy: { createdAt: "desc" },
  });
  res.json(checkins);
}

// GET /habits/:id/streak
export async function getStreak(req: Request, res: Response) {
  const habitId = Number(req.params.id);
  const habit = await prisma.habit.findFirst({ where: { id: habitId, userId: req.user!.id } });
  if (!habit) return res.status(404).json({ error: "Habit not found" });

  const checkins = await prisma.checkin.findMany({ where: { habitId } });
  const days = new Set(
    checkins.map((c) => dayjs(c.createdAt).format("YYYY-MM-DD"))
  );

  let streak = 0;
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
