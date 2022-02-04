import datetime
from Classes.Interface import LetterResult
from Wordle.WordList import LIST_OF_ANSWERS   

def getCorrectGuessOfDay() -> str:
    start_day = datetime.date(2021, 6, 19)
    today = datetime.datetime.utcnow() + datetime.timedelta(hours=8) # HK Time
    index = (today.date() - start_day).days
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

    def parseGuessResult(word: str, result: str) -> dict[str, LetterResult]:
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
                        resultMap[letter] = LetterResult.newCorrectResult(i)
                        existingResult = resultMap[letter]
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
                                filter(lambda num: num not in existingResult.correctPositions, [j for j in range(5)])
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