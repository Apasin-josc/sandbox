//object shape, two ways
interface   ExerciseI {name: string; sets: number}
type        ExerciseT = {name: string; sets: number}

//interface superpower: extend
interface CardioI extends ExerciseI { durationMin: number}

//type superpower: unions (interfaces CAN'T do this)
type Weight = number | "bodyweight";


for(let i = 0; i < 10; i++){
    console.log(i)
}