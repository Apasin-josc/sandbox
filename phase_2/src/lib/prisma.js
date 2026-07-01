import { PrismaClient } from "@prisma/client";

// One shared PrismaClient for the whole app.
// Creating a new one per request would open too many DB connections.
export const prisma = new PrismaClient();
