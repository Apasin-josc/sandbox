import express from "express";
import { habitsRouter } from "./routes/habits.routes.ts";
import { authRouter } from "./routes/auth.routes.ts";
import { errorHandler } from "./middleware/errorHandler.ts";
import { authenticate } from "./middleware/authenticate.ts";

// Builds and configures the app, then EXPORTS it — but does NOT start listening.
// Tests import this `app` to fire requests at it (no real port needed).
const app = express();

app.use(express.json());
app.use("/habits", authenticate, habitsRouter); // authenticate runs before habit routes
app.use("/auth", authRouter);
app.use(errorHandler); // error handler LAST

export { app };
