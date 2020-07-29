import os
import random
import logging
import sys

import yaml
import discord
from dotenv import load_dotenv

from config import Config

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
TARGET_USER = os.getenv("TARGET_USER")
LOG_LEVEL = os.getenv("LOG_LEVEL")

logger = logging.getLogger("orel-bot")
logger.setLevel(str(LOG_LEVEL))
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(str(LOG_LEVEL))
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

client = discord.Client()
config = Config()

@client.event
async def on_ready():
  guild = discord.utils.get(client.guilds, name=GUILD)
  
  try:
    with open("config.yaml", "r") as c_stream:
      config_data = yaml.safe_load(c_stream)

    config.CURSES_EN = config_data["en"]["curses"]
    config.ANSWERS_EN = config_data["en"]["answers"]
    config.CURSES_HE = list(config_data["he"]["curses"])
    config.ANSWERS_HE = list(config_data["he"]["answers"])

  except Exception as ex:
    logger.error(f'Exception occured trying to load config: {str(ex)}')

  logger.info(f'{client.user} is connected to the following guild \'{guild.name}\'(id: {guild.id})')
  logger.debug(f'Loaded the following configs: {str(config)}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  username = client.get_user(message.author.id)
  if TARGET_USER.lower() in username.name.lower():
    if any(curse in message.content for curse in config.CURSES_EN):
      response = random.choice(config.ANSWERS_EN)
      await message.channel.send(f'{username.mention} - {response}')
    elif any(curse in message.content for curse in config.CURSES_HE):
      response = random.choice(config.ANSWERS_HE)
      await message.channel.send(f'{username.mention} - {response}')
  else:
    logger.debug(f'{username} is not {TARGET_USER}')

client.run(TOKEN)