from Wordle.WorldList import LIST_OF_ANSWERS
from utils import *

class Engine:
    def __init__(self) -> None:
        self.filteredWordList = LIST_OF_ANSWERS

    def getGuess(self) -> str :
        bestGuess: str = ''
        bestGuessWeight: int = 0
        for word in self.filteredWordList:
            wordWeight = getWordWeightage(word)
            if(wordWeight > bestGuessWeight):
                bestGuess = word
                bestGuessWeight = wordWeight
        return bestGuess

    def handleGuessResult(self, word: str, result:str) -> None:
        guessResult = parseGuessResult(word, result)

        for letter in guessResult.keys():
            res = guessResult[letter]

            if res.status == "INCORRECT":
                self.filteredWordList = list(
                    filter(lambda word: not letter in word, self.filteredWordList)
                )
            else:
                self.filteredWordList = list(
                    filter(
                        lambda word: filterWord(letter, word, res.correctPositions, res.incorrectPositions),
                        self.filteredWordList 
                    )
                )
        return
