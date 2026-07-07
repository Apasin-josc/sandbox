import type { Request, Response, NextFunction } from "express";

// Global error handler — 4 args (err, req, res, next) is how Express
// knows this is an error handler. Must be registered LAST.
// `err` is typed `any` here (matches Express's own ErrorRequestHandler) since a
// thrown value can be literally anything.
export function errorHandler(err: any, req: Request, res: Response, next: NextFunction) {
  // malformed JSON from express.json()
  if (err?.type === "entity.parse.failed") {
    return res.status(400).json({ error: "Invalid JSON in request body" });
  }

  // anything else is an unexpected server error
  console.error(err);
  res.status(500).json({ error: "Internal server error" });
}
