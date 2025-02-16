import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from a .env file (you’ll create this later)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I'm your bot!")

bot.run(TOKEN)
