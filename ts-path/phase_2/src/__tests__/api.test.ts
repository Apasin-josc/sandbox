import { describe, it, expect } from "vitest";
import request from "supertest";
import { app } from "../app.ts";

// describe = a group of related tests
describe("auth guard & validation", () => {
  // it = one test case. "async" because supertest requests are async.
  it("returns 401 on GET /habits without a token", async () => {
    // ARRANGE + ACT: fire a request at the app (no real server/port)
    const res = await request(app).get("/habits");
    // ASSERT: check what came back
    expect(res.status).toBe(401);
  });

  it("returns 400 when registering with an invalid email", async () => {
    const res = await request(app)
      .post("/auth/register")
      .send({ email: "not-an-email", password: "short", username: "x" });
    expect(res.status).toBe(400);
  });
});
