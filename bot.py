# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from Card import Card

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    """creates a new channel with the provided name if user is admin"""
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.command(name='Inscrybe')
async def start_match(ctx, oponent='bot'):
    """welcomes opponents"""
    await ctx.send("hello "+ctx.author.display_name+" and "+oponent+"!") 

@bot.command(name='test-cards')
async def test_cards(ctx, card='stunted_wolf'):
    """tests printing a game board of multiple cards"""
    print("sending card: "+card)
    card = "Leshy/"+card+".png"
    card2 = "Leshy/stinkbug.png"
    with open(card, "rb") as fh:
        f = discord.File(fh, filename=card)
    with open(card2, "rb") as fh:
        f2 = discord.File(fh, filename=card2)
    await ctx.send(files=[f,f2])

@bot.command(name='test-card-class')
async def test_card_class(ctx):
    """tests the many functions of the card class"""
    card = Card()
    with open(card.image, "rb") as fh:
        f = discord.File(fh, filename=card.image)
    await ctx.send(content=card,file=f)
    card.buffCard("hp",2)
    card.buffCard("atk",2)
    card.buffCard("effect","flying")
    card.takeDamage(1)
    await ctx.send(content=card,file=f)

@bot.command(name='test-glitch')
async def test_glitch(ctx, card='Glitched_Card'):
    """tests sending a single gif of the glitched card"""
    print("sending card: "+card)
    card = "Leshy/"+card+".gif"
    with open(card, "rb") as fh:
        f = discord.File(fh, filename=card)
    await ctx.send(file=f)

bot.run(TOKEN)
