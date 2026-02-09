import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowano jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()
    print(f'Wiadomość od {message.author}: {message.content}')

    if content in ['hej', 'elo', 'siema', 'witam']:
        await message.channel.send(
            f'Hejka {message.author.display_name}, jak się masz!')

    elif "dobrze" in content:
        await message.channel.send('Ooooo to super 😄')
        await message.add_reaction('❤️')

    elif "źle" in content:
        await message.channel.send('O nie 😥')
        await message.author.send('Jeśli źle się czujesz, zadbaj o siebie i odpocznij ')

client.run(TOKEN)
