# wordle-ai

A simple program that solves the Wordle puzzle by process of elimination. Currently, it uses up ~5 moves to correctly guess each word.

## Usage

Simply clone and run `npm run start` locally to start the program.

Since currently there are issues pertaining to shadow-roots on the wordle website, there is a need for manual assistance. On load, there is usually a popup that needs to be closed; do so and hit enter in the console (against the 'Ready?' prompt). Then, once a word is typed, wait for the verification animation to end before clicking ready again.

Do this until the Engine correctly guesses the word or fails to guess, and then hit enter (against the 'Cleanup?' prompt) to tell the program to close the browser and perform clean up actions

```

## Future Improvements

1. Integrate with puppeteer so it can guess on browser (maintaining the browser's LocalState)
2. Write word-structure heuristics to maintain previous guess results and make vowel-consonant connections
```
