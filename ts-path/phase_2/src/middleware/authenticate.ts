import jwt from "jsonwebtoken";
import type { Request, Response, NextFunction } from "express";

export function authenticate(req: Request, res: Response, next: NextFunction) {
  const header = req.headers.authorization; // e.g. "Bearer eyJ..."

  if (!header || !header.startsWith("Bearer ")) {
    return res.status(401).json({ error: "Missing or invalid Authorization header" });
  }

  const token = header.split(" ")[1]; // ["Bearer", "eyJ..."] → take the token

  try {
    // jwt.verify returns `string | JwtPayload`; we know our payload's shape, so assert it
    const payload = jwt.verify(token, process.env.JWT_SECRET!) as { userId: number };
    req.user = { id: payload.userId }; // attach who they are for the route to use
    next(); // hand off to the actual route handler
  } catch (error) {
    return res.status(401).json({ error: "Invalid or expired token" });
  }
}
