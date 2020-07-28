import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()

CURSES_EN = [
  "shutup",
  "cos emek",
]

CURSES_HE = [
  "שתוק",
  "סתום",
  "אמא שלך",
]

ANSWERS_EN = [
  "Ohhhhhhhh, what a dumb thing to say",
  "Thats it? thats your best?",
  "Lame.",
]

ANSWERS_HE = [
  "באמת? זה הכי טוב שלך?",
  "תשמע, אתה גרוע",
  "וואי וואי, איזה אפס אתה תאמין לי",
]

@client.event
async def on_ready():
  guild = discord.utils.get(client.guilds, name=GUILD)
    
  print(
    f'{client.user} is connected to the following guild:\n'
    f'{guild.name}(id: {guild.id})'
  )

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  username = client.get_user(message.author.id)
  if "orel" in username.name.lower():
    if message.content in CURSES_EN:
      response = random.choice(ANSWERS_EN)
      await message.channel.send(f'{username.mention} - {response}')
    if message.content in CURSES_HE:
      response = random.choice(ANSWERS_HE)
      await message.channel.send(f'{username.mention} - {response}')
  else:
    print(f'{username} is not orel')

client.run(TOKEN)