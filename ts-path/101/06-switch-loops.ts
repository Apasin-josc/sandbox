type Status = "todo" | "doing" | "done";

//switch on a literal union (TS narrows each case)
function label(s: Status): string {
    switch(s){
        case "todo": return "Not started";
        case "doing": return "In progress";
        case "done": return "Complete";
    }
}

//array methods (your react bread and butter)
const sets = [
    {reps: 10, weight: 50, done: true},
    {reps: 8, weight: 55, done: false},
    {reps: 6, weight: 60, done: true},
];

const volumes = sets.map((s) => s.reps * s.weight); // -> number[]
const doneSets = sets.filter((s) => s.done);        // -> only done

console.log(label("doing"), volumes, doneSets.length);