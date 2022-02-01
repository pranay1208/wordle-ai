from string import ascii_lowercase
from Wordle.WordList import LIST_OF_ANSWERS, VALID_GUESSES
from Classes.Interface import ConstraintHeuristic
from Classes.Validator import Validator
from utils import *

class Engine:
    def __init__(self) -> None:
        self.filteredWordList = LIST_OF_ANSWERS
        self.validGuessList = VALID_GUESSES
        self.heuristics : dict[str, ConstraintHeuristic] = {}

    def answerListIsSmall(self) -> bool:
        return len(self.filteredWordList) <= 10


    def getGuess(self) -> str :
        bestGuess: str = ''
        bestGuessWeight: int = 0
        for word in self.filteredWordList:
            # wordWeight = getWordWeightage(word)
            # wordWeight = getWordEliminationScore(word, self.heuristics)
            wordWeight = getWordWeightage(word) if self.answerListIsSmall() else getWordEliminationScore(word, self.heuristics)
            if(wordWeight > bestGuessWeight):
                bestGuess = word
                bestGuessWeight = wordWeight
        if self.answerListIsSmall():
            return bestGuess

        for word in self.validGuessList:
            wordWeight = getWordEliminationScore(word, self.heuristics)
            if(wordWeight > bestGuessWeight):
                bestGuess = word
                bestGuessWeight = wordWeight
        return bestGuess

    def handleGuessResult(self, word: str, result:str) -> None:
        guessResult = Validator.parseGuessResult(word, result)

        for letter in guessResult.keys():
            res = guessResult[letter]

            if res.status == "INCORRECT":
                self.filteredWordList = list(
                    filter(lambda word: not letter in word, self.filteredWordList)
                )
                self.validGuessList = list(
                    filter(lambda word: not letter in word, self.validGuessList)
                )
            else:
                self.filteredWordList = list(
                    filter(
                        lambda word: filterWord(letter, word, res.correctPositions, res.incorrectPositions),
                        self.filteredWordList 
                    )
                )
                self.validGuessList = list(
                    filter(
                        lambda word: filterWord(letter, word, res.correctPositions, res.incorrectPositions),
                        self.validGuessList 
                    )
                )
        return

    def computeHeuristics(self) -> None:
        self.heuristics = {}
        for letter in ascii_lowercase:
            self.heuristics[letter] = ConstraintHeuristic()
        for word in self.filteredWordList:
            for i in range(len(word)):
                letter = word[i]
                self.heuristics[letter].addOccurrence(i)
        return
