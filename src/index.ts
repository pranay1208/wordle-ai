import puppeteer from "puppeteer";
import readline from "readline-sync";
import { readFileSync, writeFileSync } from "fs";
import { join } from "path";
import WordGuessEngine from "./engine";
import { getResult, typeGuess } from "./utils";

async function main() {
  const statistics = readFileSync(
    join(__dirname, "..", "gameInfo", "statistics.txt"),
    "utf-8"
  ).trim();
  const gameState = readFileSync(
    join(__dirname, "..", "gameInfo", "gameState.txt"),
    "utf-8"
  );
  let browser: puppeteer.Browser;
  try {
    //Instantiating puppeteer
    browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    await page.goto("https://www.powerlanguage.co.uk/wordle/");
    //loading statistics

    if (typeof statistics === "string" && statistics.length > 0) {
      await page.evaluate(
        (oldStats, gameState) => {
          localStorage.setItem("statistics", oldStats);
          localStorage.setItem("gameState", gameState);
        },
        statistics,
        gameState
      );
    }

    //reloading page to
    await page.reload();

    const engine = new WordGuessEngine();
    let result = "",
      numGuesses = 0;

    while (result !== "11111" || numGuesses >= 6) {
      readline.question("Ready?");
      numGuesses++;
      const guess = engine.getGuess();
      await typeGuess(page, guess);
      result = await getResult(page, numGuesses - 1); // subtracting one because index is 0-based
      if (result.length !== 5) {
        console.log(result);
        throw new Error("SMALL RESULT");
      }
      engine.handleGuessResult(guess, result);
      console.log(
        "Reduced sample size to",
        engine.filteredWordList.length,
        "words\n"
      );
    }

    if (numGuesses <= 6) {
      console.log("Correctly guessed in", numGuesses, "tries");
    } else {
      console.log(
        "Could not guess the word correctly... it was",
        WordGuessEngine.getCorrectGuessOfDay().toUpperCase
      );
    }

    readline.question("Cleanup?");

    //save statistics
    const newStatistics = await page.evaluate(() =>
      localStorage.getItem("statistics")
    );
    const newGameState = await page.evaluate(() =>
      localStorage.getItem("gameState")
    );
    writeFileSync(
      join(__dirname, "..", "gameInfo", "statistics.txt"),
      newStatistics
    );
    writeFileSync(
      join(__dirname, "..", "gameInfo", "gameState.txt"),
      newGameState
    );

    //done!
  } catch (err) {
    console.log("Something went wrong!!!!!!!");
    console.log(err);
  } finally {
    if (browser === undefined) {
      console.log("Browser was undefined");
    } else {
      await browser.close();
    }
  }
}

main();
