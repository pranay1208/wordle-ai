# wordle-ai

A simple program that solves the Wordle puzzle by process of elimination. Currently, it uses up ~5 moves to correctly guess each word.

## Usage

Simply clone and run `npm run start` locally to start the program. After each guess, the script requires an input that validates its guess.

'1' -> Correct letter in right position

'0' -> Incorrect position but letter in word

'-' -> Letter not in word (any character instead of 0 or 1 will satisfy this constraint)

```
--- The correct word is "happy"
Engine guesses APPLE: -01--
```

## Future Improvements

1. Integrate with puppeteer so it can guess on browser (maintaining the browser's LocalState)
2. Write word-structure heuristics to maintain previous guess results and make vowel-consonant connections
