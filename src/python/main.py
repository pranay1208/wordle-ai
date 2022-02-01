from engine import Engine


engine = Engine()
result: str = ''
numGuesses: int = 0

while result != '11111' or numGuesses >= 6:
    numGuesses += 1
    guess = engine.getGuess()
    result = input(f"Engine guesses {guess.upper()}: ")
    if len(result) != 5:
        print('Result not sized correctly')
        raise Exception('IMPROPER RESULT')
    engine.handleGuessResult(guess, result)

if numGuesses <= 6:
    print(f"Correctly guessed in {numGuesses} tries!")
else:
    print("Could not guess the word correctly")