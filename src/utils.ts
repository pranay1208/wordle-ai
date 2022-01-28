import { LetterResult } from "./interface";
import letterWeight from "./letterWeights";

export function getWordWeightage(word: string): number {
  let wordPopularity = 0;
  for (let i = 0; i < word.length; i++) {
    const letter = word[i];
    const numDuplicates = (
      word.slice(0, i).match(new RegExp(letter, "g")) || []
    ).length;
    wordPopularity += letterWeight[letter] / Math.pow(10, numDuplicates);
  }
  return Math.round(wordPopularity * 1000) / 10000;
}

export function parseGuessResult(
  word: string,
  result: string
): Record<string, LetterResult> {
  const resultMap: Record<string, LetterResult> = {};
  for (let i = 0; i < word.length; i++) {
    const letter = word[i];
    const res = result[i];

    if (letter in resultMap) {
      if (res === "1") {
        if (resultMap[letter].status === "CORRECT") {
          resultMap[letter].correctPositions.push(i);
        } else if (
          resultMap[letter].status === "PARTIAL" ||
          resultMap[letter].status === "MULTI_INSTANCE"
        ) {
          resultMap[letter].status = "MULTI_INSTANCE";
          resultMap[letter].correctPositions.push(i);
        } else {
          resultMap[letter] = getCorrectResult(i);
          resultMap[letter].incorrectPositions = [0, 1, 2, 3, 4].filter(
            (n) => n !== i
          );
        }
      } else if (res === "0") {
        if (resultMap[letter].status === "CORRECT") {
          resultMap[letter].status = "MULTI_INSTANCE";
          resultMap[letter].incorrectPositions = [i];
        } else if (
          resultMap[letter].status === "PARTIAL" ||
          resultMap[letter].status === "MULTI_INSTANCE"
        ) {
          resultMap[letter].incorrectPositions.push(i);
        } else {
          console.log(
            "This is an unseen case where there was an incorrect option before the partial option!!!"
          );
          throw new Error("INCORRECT BEFORE PARTIAL");
        }
      } else {
        if (
          resultMap[letter].status === "PARTIAL" ||
          resultMap[letter].status === "MULTI_INSTANCE"
        ) {
          resultMap[letter].incorrectPositions.push(i);
        } else if (resultMap[letter].status === "CORRECT") {
          resultMap[letter].incorrectPositions = [0, 1, 2, 3, 4].filter(
            (n) => !resultMap[letter].correctPositions.includes(n)
          );
        }
      }
      continue;
    }

    if (res === "1") {
      resultMap[letter] = getCorrectResult(i);
    } else if (res === "0") {
      resultMap[letter] = getPartialResult(i);
    } else {
      resultMap[letter] = getIncorrectResult();
    }
  }
  return resultMap;
}

const getCorrectResult = (position: number): LetterResult => ({
  status: "CORRECT",
  correctPositions: [position],
  incorrectPositions: [],
});

const getPartialResult = (position: number): LetterResult => ({
  status: "PARTIAL",
  correctPositions: [],
  incorrectPositions: [position],
});

const getIncorrectResult = (): LetterResult => ({
  status: "INCORRECT",
  correctPositions: [],
  incorrectPositions: [0, 1, 2, 3, 4],
});

export function combinePositionValues(info: number[], res: number[]): number[] {
  return [...info, ...res].reduce(
    (prev, curr) => (prev.includes(curr) ? prev : [...prev, curr]),
    []
  );
}

//Resolve these guesses
// Object.keys(guessResult).forEach((letter) => {
//   const res = guessResult[letter];
//   if (!(letter in this.letterInformation)) {
//     this.letterInformation[letter] = guessResult[letter];
//     return;
//   }
//   const info = this.letterInformation[letter];
//   // We can go from partial/multi-instance to correct, else the state is expected to stay the same
//   this.letterInformation[letter].correctPositions = combinePositionValues(
//     info.correctPositions,
//     res.correctPositions
//   );
//   this.letterInformation[letter].incorrectPositions = combinePositionValues(
//     info.incorrectPositions,
//     res.incorrectPositions
//   );
//   if (info.status === "CORRECT" || info.status === "INCORRECT") {
//     // if info status is incorrect, then this letter can never be in this block, if it is correct, then we gucci
//     return;
//   }
//   if (
//     (info.status === "PARTIAL" || info.status === "MULTI_INSTANCE") &&
//     res.status === "CORRECT"
//   ) {
//     this.letterInformation[letter].status = "CORRECT"
//   }
// });
