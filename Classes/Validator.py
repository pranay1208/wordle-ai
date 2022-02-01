import datetime
from Wordle.WordList import LIST_OF_ANSWERS   

def getCorrectGuessOfDay() -> str:
    start_day = datetime.date(2021, 6, 19)
    today = datetime.date.today()
    index = (today - start_day).days
    return LIST_OF_ANSWERS[index % len(LIST_OF_ANSWERS)]


class Validator:
    def __init__(self, word: str = None) -> None:
        if(word == None):
            word = getCorrectGuessOfDay()

        self.answer = word.lower()

    def isValidAnswer(word: str | None) -> bool:
        return word == None or (len(word) == 5 and word.lower() in LIST_OF_ANSWERS)

    def validateGuess(self, guessStr: str) -> str:
        result = ['_'] * 5
        copyOfAnswer = [char for char in self.answer]
        guess = [char for char in guessStr]

        # First we check for correct word in correct position
        for i in range(5):
            if copyOfAnswer[i] == guess[i]:
                # If it is correct and in correct position, we change it to '*'
                result[i] = '1'
                copyOfAnswer[i] = '*'
                guess[i] = '*'

        # Next, we look for partials
        for i in range(5):
            if guess[i] == '*' or guess[i] not in copyOfAnswer:
                # We have already marked this as correct so do not recheck
                continue
            actualPosition = copyOfAnswer.index(guess[i])
            copyOfAnswer[actualPosition] = '*'
            result[i] = '0'

        return ''.join(result)
