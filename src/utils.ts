import { LetterResult } from "./interface";
import letterWeight from "./letterWeights";

export function getWordWeightage(word: string): number {
  let wordPopularity = 0;
  for (let i = 0; i < word.length; i++) {
    const letter = word[i];
    const firstOccurence = word.indexOf(letter);
    if (firstOccurence !== -1 && firstOccurence < i) {
      //if letter appears multiple times, then we calculate its value as a tenth of what it really is
      wordPopularity += letterWeight[letter] / 10;
    } else {
      wordPopularity += letterWeight[letter];
    }
  }
  //round to a "nice" integral form that is between 1-10
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
        resultMap[letter].status =
          resultMap[letter].status === "PARTIAL" ? "MULTI_INSTANCE" : "CORRECT";
        resultMap[letter].correctPositions.push(i);
        resultMap[letter].incorrectPositions = resultMap[
          letter
        ].incorrectPositions.filter((n) => n !== i);
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
        if (resultMap[letter].status === "PARTIAL") {
          resultMap[letter].incorrectPositions.push(i);
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
  incorrectPositions: [1, 2, 3, 4, 5].filter((n) => n !== position),
});

const getPartialResult = (position: number): LetterResult => ({
  status: "PARTIAL",
  correctPositions: [],
  incorrectPositions: [position],
});

const getIncorrectResult = (): LetterResult => ({
  status: "INCORRECT",
  correctPositions: [],
  incorrectPositions: [1, 2, 3, 4, 5],
});
