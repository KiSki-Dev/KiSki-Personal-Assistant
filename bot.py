import os
import discord
from discord.ext import commands
from discord.utils import get
from discord import app_commands

from dotenv import load_dotenv

env_file_path = r"C:\Users\kille\Desktop\KiSki Personal Assistant\KiSki-Personal-Assistant\.env"
load_dotenv(dotenv_path=env_file_path)

token = str(os.getenv("TOKEN"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
guildID = 1171187810162716673


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="KiSki-Systems"))
    await tree.sync(guild=discord.Object(id=guildID))
    print("Bot is online!")

@tree.command(name="ping", description = "Check the currents Bot Ping", guild=discord.Object(id=guildID))
async def first_command(interaction,):
    await interaction.response.send_message('Pong! My current Ping is: {0}'.format(round(client.latency, 5)))

@tree.command(name="echo", description = "Repeats your Message", guild=discord.Object(id=guildID))
async def first_command(interaction, message: str):
    await interaction.response.send_message(message)



client.run(token)