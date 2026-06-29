
//who always runs first, the synchronous code in front of Node right now, or a handed-off async callback?
//synchronous code always runs first
//async callbacks wait their turn until the current synchronous pass is done
console.log("1");
setTimeout(() => {
  console.log("2");
}, 0);
console.log("3");
