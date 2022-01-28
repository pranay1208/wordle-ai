import { LetterResult } from "./interface";
import { getWordWeightage, parseGuessResult } from "./utils";
import listOfWords from "./wordList";

class WordGuessEngine {
  filteredWordList: string[];
  // To add some additional information regarding word picking (so as to add heuristic capabilities)
  letterInformation: Record<string, LetterResult>;

  constructor() {
    this.filteredWordList = listOfWords;
    this.letterInformation = {};
  }

  // uses the reverse engineered assumption as a checker
  static getCorrectGuessOfDay(): string {
    const startDay = new Date(2021, 5, 19, 0, 0, 0, 0);
    const today = new Date();
    const index = Math.round(
      (today.setHours(0, 0, 0, 0) - startDay.setHours(0, 0, 0, 0)) / 864e5
    );
    return listOfWords[index % listOfWords.length];
  }

  getGuess(): string {
    let bestGuess = "";
    let bestGuessWeight = 0;
    this.filteredWordList.forEach((word) => {
      const wordWeight = getWordWeightage(word);
      if (wordWeight > bestGuessWeight) {
        bestGuessWeight = wordWeight;
        bestGuess = word;
      }
    });
    return bestGuess;
  }

  //TODO: Implement weightage based on information in this.letterInformation
  // wordWeightage(word: string): number {
  //   return getWordWeightage(word);
  // }

  handleGuessResult(word: string, result: string): void {
    const guessResult = parseGuessResult(word, result);
    for (const letter of Object.keys(guessResult)) {
      const res = guessResult[letter];

      if (res.status === "INCORRECT") {
        this.filteredWordList = this.filteredWordList.filter(
          (w) => !w.includes(letter)
        );
      } else if (res.status === "CORRECT" || res.status === "MULTI_INSTANCE") {
        this.filteredWordList = this.filteredWordList.filter((w) => {
          for (let pos of res.correctPositions) {
            if (w[pos] !== letter) return false;
          }
          for (let pos of res.incorrectPositions) {
            if (w[pos] === letter) return false;
          }
          return true;
        });
      } else {
        this.filteredWordList = this.filteredWordList.filter((w) => {
          if (!w.includes(letter)) return false;
          for (let pos of res.incorrectPositions) {
            if (w[pos] === letter) return false;
          }
          return true;
        });
      }
    }
  }
}

export default WordGuessEngine;
