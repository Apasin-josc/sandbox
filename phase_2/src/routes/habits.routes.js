import { Router } from "express";
import {
  listHabits,
  getHabit,
  createHabit,
  updateHabit,
  deleteHabit,
  createCheckin,
  listHabitsCheckin,
  getStreak
} from "../controllers/habits.controller.js";

// A Router = a mini-app for one group of routes.
// Paths here are RELATIVE — they get prefixed when mounted in server.js.
export const habitsRouter = Router();

habitsRouter.get("/", listHabits); // GET    /habits
habitsRouter.get("/:id", getHabit); // GET    /habits/:id
habitsRouter.post("/", createHabit); // POST   /habits
habitsRouter.patch("/:id", updateHabit); // PATCH  /habits/:id
habitsRouter.delete("/:id", deleteHabit); // DELETE /habits/:id

habitsRouter.post("/:id/checkins", createCheckin);
habitsRouter.get("/:id/checkins", listHabitsCheckin);

habitsRouter.get("/:id/streak", getStreak);

