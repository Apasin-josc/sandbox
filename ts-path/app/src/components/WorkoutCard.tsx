import { useState } from "react";

type WorkoutCardProps = {
  name: string;
  done: boolean;
};

export function WorkoutCard({ name, done }: WorkoutCardProps) {
  const [completedSets, setCompletedSets] = useState(0);
  //       current.       changing            initial
  return (
    <div>
      <h3>{name}</h3>
      <p>{done ? "✅ done" : "⬜ todo"}</p>
      <button onClick={() => setCompletedSets(completedSets + 1)}> + {completedSets} </button>
    </div>
  );
}
