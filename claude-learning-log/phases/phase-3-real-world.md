# Phase 3 — Real-world

**Goal:** Take the habit tracker from "works on my machine" to "deployed, tested, and employable-looking."

**Done when:** The API is deployed publicly with auth and at least a basic test suite.

## Lessons
1. **Auth** ⬜
   - JWT-based auth. Register/login, protect routes with middleware. (Concept known from other frameworks — new syntax.)
2. **Testing** ⬜
   - One real round: `vitest` or `node --test` + `supertest` for endpoint tests.
3. **Deployment** ⬜
   - Deploy to Railway or Render with a managed Postgres. Real public URL.
4. **Docker basics** ⬜
   - A `Dockerfile` for the app. Understand why, not just how.
5. **THEN: TypeScript** ⬜
   - Only now. By this point I'll *feel* why people want types in JS. Migrate the habit tracker to TS.

## Hard "not yet" list (still)
Microservices, GraphQL, Nest.js, Kubernetes. Revisit only after this phase ships and there's a concrete reason.
