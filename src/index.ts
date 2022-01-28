import * as readline from "readline-sync";
import { getWordWeightage, parseGuessResult } from "./utils";
import listOfWords from "./wordList";

async function main() {
  const answer = readline.question("Enter a word: ");
  const includes = listOfWords.includes(answer);
  console.log(`${answer} is ${includes ? "" : "not "}a valid word`);
  if (!includes) {
    return;
  }
  console.log(`${answer} has a word weightage of ${getWordWeightage(answer)}`);
  const guessResult = readline.question("Enter guess result: ");
  console.log(parseGuessResult(answer, guessResult));
}

main();
