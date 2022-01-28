import * as readline from "readline-sync";
import listOfWords from "./wordList";

async function main() {
  const answer = readline.question("Enter a word: ");
  console.log(
    `${answer} is ${listOfWords.includes(answer) ? "" : "not "}a valid word`
  );
}

main();
