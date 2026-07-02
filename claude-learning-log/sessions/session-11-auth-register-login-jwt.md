# Session 11 — Auth: Register, Login & JWT

**Date:** 2026-07-02
**Phase:** 3 — Real-world (auth foundation; middleware still to come)

## What we covered

### Framing
- **Authentication** = "who are you?" (login). **Authorization** = "what can you do?" (permissions).
- Phase 3 lives INSIDE the same codebase (no new folder). Habits must belong to a user.

### Data model change (relation, one level up)
- **A User has many Habits** → foreign key on the "many" side = `Habit.userId` (same pattern as Checkin/Habit).
- `User` model: `id`, `email @unique`, `password` (stores the HASH), `username`, `createdAt`, `habits Habit[]`.
- `Habit` got `userId Int` + `user User @relation(fields: [userId], references: [id])`.
- **Migration gotcha:** adding a REQUIRED column (`userId`) to a table with existing rows fails ("not possible if the table is not empty" — no value to backfill). 
  - Dev fix (throwaway data): `npx prisma migrate reset` → then `migrate dev`. 
  - **Prod fix (know this):** 3-step — add column optional → backfill → make required. Never drop real data.
- Generated SQL showed `CREATE UNIQUE INDEX "User_email_key"` (the `@unique`) + a second FK `Habit.userId → User.id`.

### Register (`POST /auth/register`)
- Zod `registerSchema`: `email: z.string().email()`, `password: z.string().min(8)`, `username: z.string().min(1)`. (`z.string().email()` = built-in email format check.)
- **Hash the password:** `const passwordHash = await bcrypt.hash(password, 10)` — bcrypt is one-way, slow, salted. `10` = salt rounds (work factor). Store `passwordHash`, NEVER the plaintext.
- **Never return the password** in the response — only safe fields (`id`, `email`, `username`).
- **Duplicate email** → Prisma throws **`P2002`** (unique constraint) → `try/catch` → **`409 Conflict`** "Email already in use" (a client error, NOT a 500).

### Login (`POST /auth/login`)
- Zod `loginSchema`: email + password present.
- **Verify password:** you can't un-hash, so `await bcrypt.compare(typedPassword, user.password)` re-hashes the attempt and checks it → boolean.
- **User-enumeration defense:** "no such user" AND "wrong password" return the SAME generic `401 "Invalid credentials"`. Different messages would let an attacker discover which emails are registered.
- **Issue a JWT:** `jwt.sign({ userId: user.id }, process.env.JWT_SECRET, { expiresIn: "7d" })`. Return `{ token }`.

### JWT internals (decoded my own token live)
- A JWT = `header.payload.signature` (3 base64url parts split by dots).
- Decoded with plain `base64 -d` (no secret!): header `{"alg":"HS256","typ":"JWT"}`, payload `{"userId":1,"iat":...,"exp":...}` (exp − iat = 604800s = 7 days).
- **Readable but NOT tamper-able:** anyone can READ the payload (so never put secrets there) — but they can't FORGE it (change `userId:1`→`2`) without the `JWT_SECRET`, because the signature would break. Signature protects *integrity*, not *secrecy*.

### Env vars
- **Node does NOT auto-load `.env`.** `DATABASE_URL` only worked because Prisma loads `.env` itself. For our own vars (`JWT_SECRET`), we load it explicitly: dev script now `node --watch --env-file=.env src/server.js` (Node 26 built-in flag).
- Added `JWT_SECRET` to `.env` (gitignored). In prod it must be a long random secret.

### Prisma error codes (the two to know cold)
- **P2025** = record not found (update/delete) → 404.
- **P2002** = unique constraint failed (create/update) → 409.
- (P2003 = FK violation, etc. — look them up when they appear.)

## What I struggled with / questions I asked
- Got the User↔Habit relation backwards first (put FK on User) — fixed with the "FK on the many side" rule.
- Bare string in an object literal (`{ email, username, "user created..." }`) = syntax error — needs a key (`message: "..."`).
- Forgot `prisma` in `npx prisma migrate` (ran a random `migrate` package).
- Good conceptual questions: jsonwebtoken vs jose (chose jsonwebtoken for docs/learning; jose is modern/edge); why generic 401; why only `userId` in the JWT.

## What clicked
- bcrypt hashing (store hash) + verify via `bcrypt.compare` (never decrypt).
- JWT = signed, readable-not-forgeable credential; the base64 decode made it concrete.
- P2002/409 for duplicates (mirrors P2025/404).
- How env vars actually reach the app (`--env-file`).

## Pick up next time — FINISH AUTH
- **Auth middleware** `authenticate(req, res, next)`: read `Authorization: Bearer <token>` header → `jwt.verify(token, JWT_SECRET)` → attach `req.user = { id: payload.userId }` → `next()`; on bad/missing token → `401`.
- **Protect the habit routes** with that middleware.
- **Scope habits to the user:** `create` sets `userId: req.user.id`; `findMany`/`findUnique`/`update`/`delete` filter by `userId` so you only touch YOUR habits (authorization, not just authentication).
- REST Client: use the captured `{{token}}` in an `Authorization: Bearer {{token}}` header.

## Environment reminder
- `docker start habit-postgres` before coding. Prisma **v6**. Run: `npm run dev` (now loads `.env`).
- Installed: bcrypt, jsonwebtoken (+ dayjs, zod, express, @prisma/client).
- Endpoints so far: `/habits*`, `/habits/:id/checkins`, `/habits/:id/streak`, `/auth/register`, `/auth/login`.
