// Declaration merging: tell TypeScript that our authenticate middleware
// adds `user` onto Express's Request object. Without this, `req.user` is a type error.
declare global {
  namespace Express {
    interface Request {
      user?: { id: number };
    }
  }
}

export {}; // makes this file a module so `declare global` works
