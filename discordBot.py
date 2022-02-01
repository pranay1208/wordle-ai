import discord
import os
from dotenv import load_dotenv
from main import makeBotGuess

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        content = message.content.strip()
        if content.startswith('!owl'):
            components : list[str] = content.split(' ')
            guessWord : str | None = None
            if len(components) >= 2:
                guessWord = components[1]
            responseText = makeBotGuess(guessWord)
            await message.reply(responseText)

                

client = MyClient()
client.run(os.getenv('DISCORD_TOKEN'))