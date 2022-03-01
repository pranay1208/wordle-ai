import discord
import os
from dotenv import load_dotenv
from Classes.Validator import Validator, getDateOffset, getGuessFromOffset, getHongKongDate
from main import makeBotGuess

load_dotenv()

def getFinalText(components: list[str]) -> str:
    guessWord : str | None = None
    if len(components) >= 2:
        if components[1].isnumeric():
            guessWord = getGuessFromOffset(int(components[1]))
        else:
            guessWord = components[1]
    if(not Validator.isValidAnswer(guessWord)):
        print(f"'{guessWord}' is not a recognised answer")
        return f"**{guessWord.upper()}** is not a recognised word. You can check out legitimate words at <https://github.com/pranay1208/wordle-ai/blob/master/Wordle/WordList.py>"
    responseText = makeBotGuess(guessWord)
    infoText = ''
    if guessWord == None:
        hkDate = getHongKongDate()
        infoText += f"WOTD - {str(hkDate)}. Wordle {getDateOffset(hkDate)}"
    elif components[1].isnumeric():
        infoText += f"Wordle {str(components[1])}"
    else:
        infoText += f"WORD - {guessWord}"
    return f"{infoText}\n\n{responseText}"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        content = message.content.strip()
        if content.startswith('!owl'):
            components : list[str] = content.split(' ')
            finalText = getFinalText(components)
            await message.reply(finalText)

                

client = MyClient()
client.run(os.getenv('DISCORD_TOKEN'))