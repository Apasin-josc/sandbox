"""
npm install express
"""

"""
docker run --name habit-postgres \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=habits \
  -p 5432:5432 \
  -d postgres:16
"""


"""
npm install prisma --save-dev
npm install @prisma/client
"""

prisma (dev dependency) = the CLI tool you run to manage migrations/schema. --save-dev because it's a build-time tool, not something your running app needs.
@prisma/client = the actual query client your app code imports at runtime.


"""
npx prisma init
"""
prisma/schema.prisma — where you define your data models (like Laravel migrations + models combined).
.env — with a placeholder DATABASE_URL.
protocol://user:password@host:port/database?options

postgresql://	(protocol)	The scheme — tells the client "this is a PostgreSQL connection." Like https:// for a website. Prisma reads this to know which kind of DB.

postgres	(username)	The database user. postgres is the default superuser Postgres creates.

:secret	(password)	The password — matches your -e POSTGRES_PASSWORD=secret Docker flag.

@	(separator)	Divides the credentials (user:password) from the location. Read it as "user:pass at host."

localhost	(host)	Where the DB lives. It's localhost (your Mac) because -p 5432:5432 exposed the container there.

:5432	(port)	The port — Postgres's default, the same one you mapped with -p. Same idea as localhost:3000 for your Express server.

/habits	(database)	Which database to use — matches -e POSTGRES_DB=habits.

?schema=public	(option)	A query parameter

So the whole string reads: "Connect using PostgreSQL, as user postgres with password secret, to the server at localhost:5432, use the habits database, in the public schema."

### vainilla prisma
"""
>prisma>schema.prisma
// This is your Prisma schema file,
// learn more about it in the docs: https://pris.ly/d/prisma-schema

// Get a free hosted Postgres database in seconds: `npx create-db`

generator client {
  provider = "prisma-client"
  output   = "../generated/prisma"
}

datasource db {
  provider = "postgresql"
}
"""


### patched prisma schema
"""
// This is your Prisma schema file,
// learn more about it in the docs: https://pris.ly/d/prisma-schema

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model Habit {
  id        Int      @id @default(autoincrement())
  name      String
  done      Boolean  @default(false)
  createdAt DateTime @default(now())
}
"""

to turn this schcema into an actual table npx prisma migrate dev --name init

#CRUD METHODS IN PRISMA
"""
app.get("/habits", async (req, res) => {
  const habits = await prisma.habit.findMany();

app.get("/habits/:id", async (req, res) => {
  const habit = await prisma.habit.findUnique({ where: { id: Number(req.params.id) } });

app.post("/habits", async (req, res) => {
  const habit = await prisma.habit.create({
    data: { name: req.body.name },
  });

app.patch("/habits/:id", async (req, res) => {
  try {
    const habit = await prisma.habit.update({
      where: { id: Number(req.params.id) },
      data: req.body,
    });
    res.json(habit);
  } catch (error) {
    //error.code === "P2025" — that's Prisma's specific code for "record not found." 
    if (error.code === "P2025") {
      return res.status(404).json({ error: "Habit not found" });
    }
    throw error; // anything else is a real bug — let it bubble up
  }
});

app.delete("/habits/:id", async (req, res) => {
  try {
    const habit = await prisma.habit.delete({
      where: { id: Number(req.params.id) }
    });
    res.status(204).end()
  } catch (error) {
    if (error.code === "P2025") {
      return res.status(404).json({ error: "Habit not found" });
    }
    throw error;
  }
});

"""


Zod schema is a description of the shape you expect
"""
npm install zod
"""


"""
import { z } from "zod";

const createHabitSchema = z.object({
  name: z.string().min(1),
});

z.object({ ... }) → "the thing I'm validating is an object with these keys."
name: → I expect a key called name.
z.string() → its value must be a string (so 123 — a number — fails).
.min(1) → a chained rule on that string: it must be at least 1 character long.
"""

https://zod.dev/api


"""
npx prisma migrate reset
npx prisma migrate dev --name add_users
"""



installing bcrypt for hashing and jsonwebtoken for sending tokens
"""
npm install bcrypt jsonwebtoken
"""

how it works the middleware for authentication
"""
So the middleware's job, in order:

Read the Authorization header.
Pull the token out (strip the "Bearer " prefix).
Verify it with jwt.verify(token, JWT_SECRET) — this checks the signature and expiry. If the token was forged or expired, it throws.
If valid → attach the user to the request (req.user) and call next() to continue to the route.
If missing/invalid → 401, stop.
"""