import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "$")
@bot.event
async def on_ready():
    print("=====|BOT_CONNECTED|=====")
@bot.command(pass_context=True)
async def information(ctx):
   await ctx.send("Made by W3Bches")
bot.run("NzczNTk3MzQ5NTg2OTI3NjE2.X6LirA.3DTzVjkOmXZm2otLsF_Gx0KvzeA")