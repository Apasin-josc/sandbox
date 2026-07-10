/* 
type Exercise = { id: number; name: string; sets: number; muscle: string };

type ExerciseUpdate = Partial<Exercise>;          // every field optional (for PATCH/edits)
type NewExercise    = Omit<Exercise, "id">;       // all fields EXCEPT id (a form before saving)
type ListItem       = Pick<Exercise, "id" | "name">; // ONLY these fields (a compact list row)
type ByMuscle       = Record<string, Exercise[]>; // an object: muscle name → list of exercises 
 

Partial<T> → all fields optional. (This is literally what Zod's .partial() did for your PATCH — same idea, in pure types.)
Omit<T, keys> → T without those fields. (New item has no id yet.)
Pick<T, keys> → only those fields.
Record<K, V> → a dictionary/map type: keys of type K, values of type V.
*/



type Workout = {id: number, date: string; notes: string; done: boolean};

type WorkoutUpdate = Partial<Workout>;
type NewWorkout = Omit<Workout, "id">;
type WorkoutCard = Pick<Workout, "id" | "date">