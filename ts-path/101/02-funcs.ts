function addReps(a: number, b: number): number {
    return a + b
}
const addReps_arrowfunc = (a: number, b: number): number => a + b;


function greet(name?: string): void {
    console.log(`hello ${name}`);
}

function totalVolume(reps: number, weight: number): number{
    return reps * weight
}
const totalVolume_arrowFunc = (reps: number, weight: number) => reps * weight;
totalVolume(10, 20)