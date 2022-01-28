import { LetterResult } from "./interface";
import { getWordWeightage } from "./utils";
import listOfWords from "./wordList";

class WordGuessEngine {
  filteredWordList: string[];
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
      const wordWeight = this.wordWeightage(word);
      if (wordWeight > bestGuessWeight) {
        bestGuessWeight = wordWeight;
        bestGuess = word;
      }
    });
    console.log(`Guessing ${bestGuess} with a weightage of ${bestGuessWeight}`);
    return bestGuess;
  }

  //TODO: Implement weightage based on information in this.letterInformation
  wordWeightage(word: string): number {
    return getWordWeightage(word);
  }
}

export default WordGuessEngine;
