# wordle-ai

A discord bot that makes an attempt to solve a wordle puzzle using constraint satisfaction.

## Usage

Simply clone and run `python main.py [arg]` locally to start the program.

You can pass in an optional command line argument to make it guess that word. If no arguemnt is passed, it will guess Wordle's word of the day

Note: The passed in argument must be a valid word in the given [list of words](./Wordle/WordList.py)

```
-- With Argument
$ python main.py light
Engine guesses ATONE: _0___
Engine guesses SHIRT: _00_1
Engine guesses LIGHT: 11111
Correctly guessed in 3 tries!

-- Without Argument, guesses word of the day
$ python main.py
Engine guesses ATONE: _01_1
Engine guesses THOSE: 11111
Correctly guessed in 2 tries!
```

## Future Work

1. Integrate with Discord
2. Update constraint satisfaction heuristics to pick the word that eliminates most options
3. Include the 'non-answer' words from Wordle into engine
