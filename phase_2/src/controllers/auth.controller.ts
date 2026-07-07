import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import { Prisma } from "@prisma/client";
import type { Request, Response } from "express";
import { prisma } from "../lib/prisma.ts";
import { registerSchema, loginSchema } from "../schemas/auth.schema.ts";

export async function register(req: Request, res: Response) {
  const result = registerSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ error: result.error.issues });
  }
  const { email, password, username } = result.data;
  const passwordHash = await bcrypt.hash(password, 10);
  try {
    const user = await prisma.user.create({ data: { email, username, password: passwordHash } });
    res.status(201).json({ message: "User created successfully", user: { id: user.id, email: user.email, username: user.username } });
  } catch (error) {
    // P2002 = unique constraint failed (e.g. duplicate email). Narrow the unknown
    // error to Prisma's known-error type so TS lets us read `.code`.
    if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === "P2002") {
      return res.status(409).json({ error: "Email already in use" });
    }
    throw error; // anything else → let the error handler deal with it
  }
}

export async function login(req: Request, res: Response) {
  const result = loginSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ error: result.error.issues });
  }
  const { email, password } = result.data;

  // 1. find the user by email
  const user = await prisma.user.findUnique({ where: { email } });

  // 2. verify: no such user OR wrong password → SAME generic 401
  if (!user || !(await bcrypt.compare(password, user.password))) {
    return res.status(401).json({ error: "Invalid credentials" });
  }

  // 3. issue a signed JWT — the payload identifies who this is (userId)
  const token = jwt.sign(
    { userId: user.id },
    process.env.JWT_SECRET!, // "!" = we assert it's set (see note: validate env at startup in prod)
    { expiresIn: "7d" }
  );

  res.json({ token });
}
