import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is起動しました！")

@bot.command()
async def ping(ctx):
    await ctx.send("puni Bot 起動中！")

bot.run(os.environ["DISCORD_TOKEN"])
