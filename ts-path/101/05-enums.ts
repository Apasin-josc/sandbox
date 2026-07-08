/*
enum Difficulty {
  Easy = "easy",
  Medium = "medium",
  Hard = "hard",
}

let d: Difficulty = Difficulty.Easy;  // you reference it as Difficulty.Easy

a literal union is pure type - it vanishes when the code runs (it's just an annotation, stripped away)
a enum generates real runtime javascript (/an actual object exists at runtime)
*/

enum Difficulty {
  Easy = "easy",
  Medium = "medium",
  Hard = "hard",
}

let d: Difficulty = Difficulty.Easy;

/* let reps: number = 5;  it works because if we quit the : number is still valid JS (strippable)*/
