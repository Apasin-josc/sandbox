function throwdice() {
    const sides = 6;
    const randomDiceResult = Math.floor(Math.random() * sides) + 1;
    return randomDiceResult;
}
const yourGuess = 3;
const result = throwdice();
console.log(`you guessed: ${yourGuess}. the result is ${result}`);
export {};
//# sourceMappingURL=index.js.map