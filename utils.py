from Wordle.Heuristics import LETTER_FREQUENCIES
from Classes.Interface import ConstraintHeuristic

def getWordWeightage(word: str) -> int:
    popularity: int = 0
    for i in range(len(word)):
        letter = word[i]
        numDuplicates = word[0:i].count(letter)
        popularity += LETTER_FREQUENCIES[letter.lower()] / pow(10, numDuplicates)
    return popularity 

def getWordEliminationScore(word: str, heuristic: dict[str, ConstraintHeuristic]) -> int:
    elimScore: int = 0
    for i in range(len(word)):
        letter = word[i]
        numDuplicates = word[0:i].count(letter)
        elimScore += heuristic[letter].getPositionScore(i)
        if numDuplicates == 0:
            elimScore += heuristic[letter].getEliminationScore()

    return elimScore

def filterWord(letter: str, word: str, correct: 'list[int]', incorrect: 'list[int]') -> bool:
    if not letter in word: 
        return False
    for pos in correct:
        if word[pos] != letter:
            return False
    for pos in incorrect:
        if word[pos] == letter:
            return False
    return True