// function declaration
function addOld(a, b) {
    return a + b
}

// arrow function stored in a const
const addNew = (a, b) => {
    return a + b
};

console.log(addOld(2, 3));
console.log(addNew(2, 3));


function doMath(a, b, operation) {
  return operation(a, b);
}


console.log(doMath(10, 5, addOld));
console.log(doMath(10, 5, (a, b) => a - b));


const habits = [
  { name: "read", done: true },
  { name: "run", done: false },
  { name: "meditate", done: true },
];

//using an arrowfunction for using the .map method
const shouted = habits.map((habit) => habit.name.toUpperCase());
const finished = habits.filter((habit) => habit.done);
console.log(shouted);
console.log(habits);
console.log(finished);

const numbers = [10, 20, 30];
const total = numbers.reduce((acc, current) => {
    return acc + current;
}, 0);

console.log(total);