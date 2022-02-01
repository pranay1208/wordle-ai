import datetime
from worldList import LIST_OF_ANSWERS
from interface import LetterResult
from utils import *

class Engine:
    def __init__(self) -> None:
        self.filteredWordList = LIST_OF_ANSWERS
    
    def getCorrectGuessOfDay() -> str:
        start_day = datetime.date(2021, 6, 19)
        today = datetime.date.today()
        index = (today - start_day).days
        return LIST_OF_ANSWERS[index % len(LIST_OF_ANSWERS)]

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
            res : LetterResult = guessResult[letter]

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
