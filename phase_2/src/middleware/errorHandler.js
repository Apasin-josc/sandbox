// Global error handler — 4 args (err, req, res, next) is how Express
// knows this is an error handler. Must be registered LAST.
export function errorHandler(err, req, res, next) {
  // malformed JSON from express.json()
  if (err.type === "entity.parse.failed") {
    return res.status(400).json({ error: "Invalid JSON in request body" });
  }

  // anything else is an unexpected server error
  console.error(err);
  res.status(500).json({ error: "Internal server error" });
}
