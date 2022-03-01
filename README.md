# wordle-ai

A discord bot that makes an attempt to solve a wordle puzzle using constraint satisfaction.

Add `Word Owl` to your server by clicking [here](https://discord.com/api/oauth2/authorize?client_id=937395636507144202&permissions=3072&scope=bot)!

Additionally, you can copy the following link to your browser:

```
https://discord.com/api/oauth2/authorize?client_id=937395636507144202&permissions=3072&scope=bot
```

This algorithm runs in linear time [O(n)] and uses largest elimination heuristic till the valid answer list is smaller than 10 elements, then picks by letter popularity.

## Usage

### As discord bot

Use the links at the top of this README to add the bot to your own discord server.

1. Guess word of day by typing `!owl`
2. Guess a specific word by typing `!owl <word>`
3. Guess a specific wordle by number by typing `!owl <number>`

```
!owl
!owl brine
!owl 233
```

### Local (without discord)

Uncomment the first and the last 2 lines in main.py. Then, simply run `python main.py [arg]` locally to start the program.

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

1. More QOL changes.
