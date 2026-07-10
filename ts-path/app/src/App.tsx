import { WorkoutCard } from "./components/WorkoutCard";

function App() {
  const appName = "Workout Tracker";
  const workoutsThisWeek = 3;

  return (
    <div>
      <h1> {appName} </h1>
      <p>You've trained {workoutsThisWeek} times this week.</p>
      <WorkoutCard name="bench press" done={false} />
      <WorkoutCard name="squad" done={false} />
      <WorkoutCard name="shoulder press" done={false} />
    </div>
  )
}

export default App;