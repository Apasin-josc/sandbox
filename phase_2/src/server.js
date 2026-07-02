import express from "express";
import { habitsRouter } from "./routes/habits.routes.js";
import { authRouter } from "./routes/auth.routes.js";
import { errorHandler } from "./middleware/errorHandler.js";

const app = express();

// 1. parse JSON bodies for every request
app.use(express.json());

// 2. mount the habits routes under the /habits prefix
app.use("/habits", habitsRouter);

app.use("/auth", authRouter);

// 3. error handler LAST, so it catches anything thrown above
app.use(errorHandler);

app.listen(3000, () => {
  console.log("server running on http://localhost:3000");
});
