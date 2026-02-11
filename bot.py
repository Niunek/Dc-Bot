import random
import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
emotki = [
    "😀","😃","😄","😁","😆","😅","😂","🤣","😊","😇",
    "🙂","🙃","😉","😌","😍","🥰","😘","😗","😙","😚",
    "😋","😛","😝","😜","🤪","🤨","🧐","🤓","😎","🥳",
    "😏","😒","😞","😔","😟","😕","🙁","☹️","😣","😖",
    "😫","😩","🥺","😢","😭","😤","😠","😡","🤬","🤯",
    "😳","🥵","🥶","😱","😨","😰","😥","😓","🤗","🤔",
    "🤭","🤫","🤥","😶","😐","😑","😬","🙄","😯","😦",
    "😧","😮","😲","🥱","😴","🤤","😪","😵","🤐","🥴",
    "🤢","🤮","🤧","😷","🤒","🤕","🤑","🤠","😈","👿",
    "👹","👺","💀","☠️","👻","👽","👾","🤖","🎃","😺",
    "😸","😹","😻","😼","😽","🙀","😿","😾","🐶","🐱",
    "🐭","🐹","🐰","🦊","🐻","🐼","🐨","🐯","🦁","🐮",
    "🐷","🐽","🐸","🐵","🙈","🙉","🙊","🐒","🐔","🐧",
    "🐦","🐤","🐣","🐥","🦆","🦅","🦉","🦇","🐺","🐗",
    "🐴","🦄","🐝","🐛","🦋","🐌","🐞","🐜","🪲","🐢",
    "🐍","🦎","🐙","🦑","🦐","🦞","🦀","🐡","🐠","🐟",
    "🐬","🐳","🐋","🦈","🐊","🐅","🐆","🦓","🦍","🐘",
    "🦏","🦛","🐪","🐫","🦙","🦒","🐃","🐂","🐄","🐎",
    "🐖","🐏","🐑","🐐","🦌","🐕","🐩","🦮","🐕‍🦺","🐈",
    "🐓","🦃","🕊️","🦢","🦜","🦚","🦩","🦤","🪶","🐇",
    "🐁","🐀","🐿️","🦔","🦇","🐉","🐲","🌵","🎄","🌲",
    "🌳","🌴","🪴","🌱","🌿","☘️","🍀","🎍","🎋","🍃",
    "🍂","🍁","🍄","🌾","💐","🌷","🌹","🥀","🌺","🌸",
    "🌼","🌻","🌞","🌝","🌛","🌜","🌚","🌕","🌖","🌗",
    "🌘","🌑","🌒","🌓","🌔","🌙","🌎","🌍","🌏","💫",
    "⭐","🌟","✨","⚡","☄️","🔥","💥","❄️","☃️","⛄",
    "💨","☁️","🌧️","⛈️","🌩️","🌨️","🌦️","🌈","☂️","☔"
]


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
    elif content.startswith('usmiech'):
        await message.channel.send('😊')
    elif "moneta" in content:
        wynik = random.choice(["Orzeł ", "Reszka "])
        await message.channel.send(f"Wynik rzutu monetą: {wynik}")
    elif content.startswith('gramy monete andrzej'):
        await message.channel.send("Okej ja jestem reszką 🪙")
        wynik = random.choice(["Orzeł", "Reszka"])
        await message.channel.send(f"Wynik rzutu monetą: {wynik}")
        if wynik == "Reszka":
            await message.channel.send("Jeeeej wygrałem 👑")
        else:
            await message.channel.send("O nie, wygrałeś! Gratulacje 👑")
    elif "emotka" in content:
        await message.channel.send("Podam ci jedną z moich 200 emotek")
        emoij = random.choice(emotki)
        await message.channel.send(emoij)
client.run(TOKEN)
