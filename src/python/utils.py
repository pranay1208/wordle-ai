from operator import le
from re import L
from heuristics import LETTER_FREQUENCIES
from interface import LetterResult

def getWordWeightage(word: str) -> int:
    popularity: int = 0
    for i in range(len(word)):
        letter = word[i]
        numDuplicates = word[0:i].count(letter)
        popularity += LETTER_FREQUENCIES[letter.lower()] / pow(10, numDuplicates)
    return popularity 


def parseGuessResult(word: str, result: str) -> dict:
    resultMap = {}
    for i in range(len(word)):
        letter = word[i]
        res = result[i]

        if letter in resultMap:
            existingResult : LetterResult = resultMap[letter]
            if res == "1":
                if existingResult.status == "CORRECT":
                    existingResult.correctPositions.append(i)
                elif existingResult.status == "PARTIAL" or existingResult.status == "MULTI_INSTANCE":
                    existingResult.status = "MULTI_INSTANCE"
                    existingResult.correctPositions.append(i)
                else:
                    existingResult = LetterResult.newCorrectResult(i)
                    existingResult.incorrectPositions = [j for j in range(5)]
                    existingResult.incorrectPositions.remove(i)
            elif res == "0":
                if existingResult.status == "CORRECT":
                    existingResult.status = "MULTI_INSTANCE"
                    existingResult.incorrectPositions.append(i)
                elif existingResult.status == "PARTIAL" or existingResult.status == "MULTI_INSTANCE":
                    existingResult.incorrectPositions.append(i)
                else:
                    print("Encountered issue where incorrect before partial")
                    raise Exception("INCORRECT BEFORE PARTIAL")
            else:
                if existingResult.status == "CORRECT":
                    existingResult.incorrectPositions = list(
                            filter(lambda num: not num in existingResult.correctPositions, [j for j in range(5)])
                        )
                elif existingResult.status == "PARTIAL" or existingResult.status == "MULTI_INSTANCE":
                    existingResult.incorrectPositions.append(i)
            continue

        if res == "1":
            resultMap[letter] = LetterResult.newCorrectResult(i)
        elif res == "0":
            resultMap[letter] = LetterResult.newPartialResult(i)
        else:
            resultMap[letter] = LetterResult.newIncorrectResult()
    return resultMap

def filterWord(letter: str, word: str, correct, incorrect) -> bool:
    if not letter in word: 
        return False
    for pos in correct:
        if word[pos] != letter:
            return False
    for pos in incorrect:
        if word[pos] == letter:
            return False
    return True