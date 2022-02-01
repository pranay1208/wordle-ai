# import sys
from Classes.Engine import Engine
from Classes.Validator import Validator

def makeBotGuess(answer: str | None) -> str:
    if(not Validator.isValidAnswer(answer)):
        print(f"'{answer}' is not a recognised answer")
        return f"{answer} is not a recognised word. You can check out legitimate words at <https://github.com/pranay1208/wordle-ai/blob/master/Wordle/WordList.py>"

    engine = Engine()
    validator = Validator(answer)
    result: str = ''
    numGuesses: int = 0
    listOfGuessResults : list[str] = []

    while result != '11111' or numGuesses >= 6:
        numGuesses += 1
        guess = engine.getGuess()
        print(f"Engine guesses {guess.upper()}:", end=' ')
        result = validator.validateGuess(guess)
        print(result)
        listOfGuessResults.append(result)
        print(listOfGuessResults)
        engine.handleGuessResult(guess, result)

    topText = ''
    if numGuesses <= 6:
        print(f"Correctly guessed in {numGuesses} tries!")
        topText = f"Correctly guessed in {numGuesses}/6 tries, suckas"
    else:
        print("Could not guess the word correctly")
        topText = f"I did a fucky wucky and couldn't guess"

    emojiText = ''
    for index in range(len(listOfGuessResults)):
        for char in listOfGuessResults[index]:
            if char == '1':
                emojiText += ':green_square:'
            elif char == '0':
                emojiText += ':yellow_square:'
            else:
                emojiText += ':black_large_square:'
        if(index != len(listOfGuessResults) - 1):
            emojiText += '\n'

    return f"{topText}\n\n{emojiText}"


# answer = None if len(sys.argv) < 2 else sys.argv[1]
# makeBotGuess(answer)