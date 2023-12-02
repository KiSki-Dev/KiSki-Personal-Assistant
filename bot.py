import os
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

env_file_path = "C:\\Users\\kille\\Desktop\\KiSki Personal Assistant/.env"
load_dotenv(dotenv_path=env_file_path)

token = str(os.getenv("TOKEN"))

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    os.system("cls")
    print("\Bot is online!\n")

client.run(token)