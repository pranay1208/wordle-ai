# wordle-ai

A discord bot that makes an attempt to solve a wordle puzzle using constraint satisfaction.

## Usage

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

### As discord bot

Since currently this bot has not been deployed to production, you would have to run this yourself and create your own bot.

1. Install discord.py and python-dotenv as dependencies (using pip)
2. Set up a .env file and add your bot's token to it against the key DISCORD_TOKEN
3. Run `python discordBot.py`
4. The bot will respond to all messages starting with '!owl' on your discord server.

## Future Work

1. Update constraint satisfaction heuristics to pick the word that eliminates most options
2. Deploy to production
3. Include the 'non-answer' words from Wordle into engine
