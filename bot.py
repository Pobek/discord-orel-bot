import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
TARGET_USER = os.getenv("TARGET_USER")

client = discord.Client()

CURSES_EN = []
ANSWERS_EN = []

CURSES_HE = []
ANSWERS_HE = []

@client.event
async def on_ready():
  guild = discord.utils.get(client.guilds, name=GUILD)
  
  try:
    with open("configs/en/curses.txt", "r") as en_curse_stream:
      for line in en_curse_stream:
        CURSES_EN.append(line.strip())
    
    with open("configs/en/answers.txt", "r") as en_answer_stream:
      for line in en_answer_stream:
        ANSWERS_EN.append(line.strip())
    
    with open("configs/he/curses.txt", "r") as he_curse_stream:
      for line in he_curse_stream:
        CURSES_HE.append(line.strip())
    
    with open("configs/he/answers.txt", "r") as he_answer_stream:
      for line in he_answer_stream:
        ANSWERS_HE.append(line.strip())

  except Exception as ex:
    print("Error")

  print(
    f'{client.user} is connected to the following guild:\n'
    f'{guild.name}(id: {guild.id})\n'
  )

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  username = client.get_user(message.author.id)
  if TARGET_USER in username.name.lower():
    if any(curse in message.content for curse in CURSES_EN):
      response = random.choice(ANSWERS_EN)
      await message.channel.send(f'{username.mention} - {response}')
    elif any(curse in message.content for curse in CURSES_HE):
      response = random.choice(ANSWERS_HE)
      await message.channel.send(f'{username.mention} - {response}')
  else:
    print(f'{username} is not {TARGET_USER}')

client.run(TOKEN)