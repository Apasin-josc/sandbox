# Roadmap — 10 sessions × 2h (20h)

Weighted to React + full-stack wiring (Express/TS already known). Each session ends with a 1-page summary + a 10-question scored quiz.

Build tool throughout: **Vite** (fast, TS-native). Frontend language: **TSX**.

---

## Session 1 — TypeScript for the frontend (the 20% React needs)
- Types vs interfaces, unions + narrowing, `type` for props/objects, generics (just enough), key utility types (`Partial`, `Pick`, `Omit`, `Record`), typing functions.
- *Build:* small typed exercises; set up a Vite + React + TS project.
- *Resources:* Total TypeScript (Matt Pocock, free beginners), TS Handbook "Everyday Types".

## Session 2 — React mental model & components
- Components = functions returning JSX; TSX; props (typed with a `type`); composition; one-way data flow; rendering.
- *Build:* first components of the app (static UI from typed props).
- *Resources:* react.dev "Describing the UI".

## Session 3 — State & interactivity
- `useState`, events, controlled inputs, conditional rendering, lists + `key`.
- *Build:* make the UI interactive (add/toggle items, a form).
- *Resources:* react.dev "Adding Interactivity".

## Session 4 — Side effects & data fetching
- `useEffect` (and when NOT to use it), fetch, async in React, loading/error/empty states, cleanup.
- *Build:* pull real data from a public API into the app.
- *Resources:* react.dev "Synchronizing with Effects", "You Might Not Need an Effect".

## Session 5 — Thinking in React
- Lifting state up, prop drilling, deriving state (don't duplicate), when to split components, composition over config.
- *Build:* refactor the app so state lives in the right place.
- *Resources:* react.dev "Managing State" + "Thinking in React".

## Session 6 — Routing & app structure
- React Router: routes, `useParams`, navigation, nested layouts, 404s; sensible folder structure.
- *Build:* multiple pages (list → detail), shared layout.
- *Resources:* React Router docs (tutorial).

## Session 7 — Full-stack wiring (React ↔ Express+TS)
- Point React at our own Express+TS API; CORS; request/response types shared front↔back; env-based API base URL.
- *Build:* swap the public API for our own backend (reuse habit-tracker patterns).
- *Resources:* MDN CORS; Express docs (known).

## Session 8 — Data fetching done right: TanStack Query
- The biggest real-world React 80/20: caching, `useQuery`/`useMutation`, invalidation, loading/error handled for you. Replaces most manual `useEffect` fetching.
- *Build:* migrate the app's data layer to TanStack Query.
- *Resources:* TanStack Query docs "Quick Start" + "Mutations".

## Session 9 — Auth on the frontend
- Login form → receive JWT → store it → attach `Authorization: Bearer` → protected routes + redirects; logout. (Connects to the backend auth I built.)
- *Build:* real login/logout + gated pages.
- *Resources:* react.dev forms; our own `phase_2` auth as the backend.

## Session 10 — Ship it
- Vite build, env vars, deploy frontend (Vercel/Netlify) + backend (Railway/Render), CORS in prod. Review the whole arc; what to learn next.
- *Build:* deploy the app live.
- *Resources:* Vite "Building for Production"; host docs.

---

## The app: 💪 Workout Tracker ("Fitness Quest" — theme optional)
A Hevy-style gym tracker: create **routines**, log **workouts** (exercises → sets: reps + weight), see **history + streaks**. Full-stack: React (TS) frontend ↔ our own Express+TS+Prisma backend with **auth** (reuses the habit-tracker patterns + streak logic).

**Stretch / fun (later):** a cute avatar that "levels up" with workouts, exercise images/GIFs, light gamification. Not required for the core learning.

**Rough data model:** `User` → has many `Routine` → has many `Exercise`; a `Workout` (a session) → has many `SetLog` (reps + weight). Start simple; grow it.

