/* // ❌ any — works, but throws away the type
function firstAny(arr: any[]): any {
  return arr[0];
}
const x = firstAny([1, 2, 3]); // x is `any` — TS now knows NOTHING about x

// ✅ generic — one function, keeps the type
<T> as "this function has a type parameter T; the array is T[], and it returns a T."
function first<T>(arr: T[]): T {
  return arr[0];
}
const n = first([1, 2, 3]);        // T = number  → n is number
const s = first(["a", "b", "c"]);  // T = string  → s is string

useState<number>(0) — "state holding a number"
useState<Set[]>([]) — "state holding an array of Sets"
Array<T>, Promise<T> — you've already been using generics without naming them.

 */

function first<T>(arr: T[]) : T{
    return arr[0]
}

const firstnumber = first([1, 2, 3]);
const firstchar = first(["a", "b", "c"]);

function last<T>(arr: T[]): T{
    return arr[arr.length - 1];
}

const lastnumber = last([1, 2, 3]);
const lastchar = last(["a", "b", "c"]);

console.log(typeof(firstnumber));
console.log(typeof(lastnumber));

console.log(typeof(firstchar));
console.log(typeof(lastchar));