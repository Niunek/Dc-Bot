import discord
from discord.ext import commands
from dotenv import load_dotenv 
import os 
import json
from easy_pil import Editor, Canvas, Font, load_image
import io

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

def zaladuj_wyniki():
    if os.path.exists("wyniki.txt"):
        try:
            with open("wyniki.txt", "r") as f:
                return json.load(f)
        except (json.JSONDecodeError,ValueError):
            return {}
    return {}
def zapisz_wyniki():
    with open("wyniki.txt", "w") as f:
        json.dump(lista, f, indent = 4)

lista = zaladuj_wyniki()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hej(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    user_id = str(message.author.id)
    if user_id in lista:
        lista[user_id] += 1
    else:
        lista[user_id] = 1

    print(f"używkownik {message.author} ma teraz {lista[user_id]} punktów!")
    await bot.process_commands(message)


@bot.command()
async def lvl(ctx):
    user_id = str(ctx.author.id)
    xp_usera =lista[user_id]
    name_usera = ctx.author.nick
    avatar_img = load_image(ctx.author.display_avatar.url)
    avatar = Editor(avatar_img).resize((150,150)).circle_image()
    tlo = Editor("buckground.png")
    tlo.paste(avatar, (200, 500))

    profil_czcionki_1 = Font.poppins(size = 50, variant = "regular")
    profil_czcionki_2 = Font.poppins(size = 40, variant = "light")
    tekst_poziomu = f"lvl: {xp_usera}"
    tlo.text((210, 660), str(name_usera),font = profil_czcionki_1, color="white")
    tlo.text((210, 720), str(tekst_poziomu),font = profil_czcionki_2, color="red")

    plik = discord.File(fp=tlo.image_bytes,filename="poziom.png")
    await ctx.send(file=plik)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

try:
    bot.run(TOKEN)
finally:
    zapisz_wyniki()