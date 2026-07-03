import jwt from "jsonwebtoken";

export function authenticate(req, res, next) {
  const header = req.headers.authorization; // e.g. "Bearer eyJ..."

  if (!header || !header.startsWith("Bearer ")) {
    return res.status(401).json({ error: "Missing or invalid Authorization header" });
  }

  const token = header.split(" ")[1]; // ["Bearer", "eyJ..."] → take the token

  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET); // throws if bad/expired
    req.user = { id: payload.userId }; // attach who they are for the route to use
    next(); // hand off to the actual route handler
  } catch (error) {
    return res.status(401).json({ error: "Invalid or expired token" });
  }
}
