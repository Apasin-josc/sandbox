import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import { prisma } from "../lib/prisma.js";
import { registerSchema, loginSchema } from "../schemas/auth.schema.js";

export async function register(req, res) {
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
    /* P2002 = "unique constraint failed." Thrown by create / update when you violate a @unique field — like registering an email that already exists. */
    if (error.code === "P2002") {
      return res.status(409).json({ error: "Email already in use" });
    }
    throw error; // anything else → let the error handler deal with it
  }
}

export async function login(req, res) {
  const result = loginSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ error: result.error.issues });
  }
  const { email, password } = result.data;

  // 1. find the user by email
  const user = await prisma.user.findUnique({ where: { email } });

  // 2. verify: no such user OR wrong password → SAME generic 401
  //    bcrypt.compare re-hashes the typed password and checks it against the stored hash
  if (!user || !(await bcrypt.compare(password, user.password))) {
    return res.status(401).json({ error: "Invalid credentials" });
  }

  // 3. issue a signed JWT — the payload identifies who this is (userId)
  const token = jwt.sign(
    { userId: user.id },
    process.env.JWT_SECRET,
    { expiresIn: "7d" }
  );

  res.json({ token });
}
