import sys
from Classes.Engine import Engine
from Classes.Validator import Validator

answer = None if len(sys.argv) < 2 else sys.argv[1]

if(not Validator.isValidAnswer(answer)):
    print(f"'{answer}' is not a recognised answer")
    raise Exception("INVALID ANSWER")


engine = Engine()
validator = Validator(answer)
result: str = ''
numGuesses: int = 0

while result != '11111' or numGuesses >= 6:
    numGuesses += 1
    guess = engine.getGuess()
    print(f"Engine guesses {guess.upper()}:", end=' ')
    result = validator.validateGuess(guess)
    print(result)
    engine.handleGuessResult(guess, result)

if numGuesses <= 6:
    print(f"Correctly guessed in {numGuesses} tries!")
else:
    print("Could not guess the word correctly")