import { app } from "./app.ts";

// The ONLY place that actually opens the port. This is the file you run.
// Tests import `app` from app.js instead, so they never start a real server.
app.listen(3000, () => {
  console.log("server running on http://localhost:3000");
});
