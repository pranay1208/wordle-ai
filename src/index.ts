import * as readline from "readline-sync";
import WordGuessEngine from "./engine";

function main() {
  const engine = new WordGuessEngine();
  let result = "",
    numGuesses = 0;
  while (result !== "11111") {
    numGuesses++;
    const guess = engine.getGuess();
    result = readline.question(`Engine guesses ${guess.toUpperCase()}: `);
    if (result.length !== 5) {
      throw new Error("SMALL RESULT");
    }
    engine.handleGuessResult(guess, result);
  }
  console.log("Correctly guessed in", numGuesses, "tries");
}

main();
