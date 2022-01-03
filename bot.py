import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from Card import Card
from Gameboard import Gameboard

import sys
from PIL import Image

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
async def test_cards(ctx, card='Stunted_Wolf'):
    """tests printing a game board of multiple cards"""
    print("sending card: "+card)
    card = "Leshy/"+card+".png"
    card2 = "Leshy/Stinkbug.png"
    with open(card, "rb") as fh:
        f = discord.File(fh, filename=card)
    with open(card2, "rb") as fh:
        f2 = discord.File(fh, filename=card2)
    await ctx.send(files=[f,f2])
    
@bot.command(name='test-boardprint')
async def test_boardprint(ctx):
    """tests printing a game board of multiple cards as a composite image"""
    #images = [Image.open(x) for x in ['Leshy/Wolf.png','Leshy/Glitched_Card.gif', 'Leshy/Stunted_Wolf.png']]
    #widths, heights = zip(*(i.size for i in images))
    #total_width = sum(widths)
    #max_height = max(heights)
    #new_im = Image.new('RGB', (total_width, max_height))
    #x_offset = 0
    #for im in images:
        #new_im.paste(im, (x_offset,0))
        #x_offset += im.size[0]
    board=Gameboard()
    new_im=board.testPrintCards()
    new_im.save('temp.png')
    with open("temp.png", "rb") as fh:
        f = discord.File(fh, filename="temp.png")
    await ctx.send(file=f)

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

@bot.command(name='test-cardprint')
async def test_cardprint(ctx):
    """tests printing a custom card image"""
    #create card
    card = Card(image="Leshy/Stinkbug.png")
    #alter card to test alterations
    card.buffCard("hp",2)
    card.buffCard("atk",2)
    card.buffCard("effect","flying")
    card.takeDamage(1)
    #retrieve card image
    cardImage = [Image.open(card.image)]
    #get size of card image
    widths, heights = zip(*(i.size for i in cardImage))
    total_width = sum(widths)
    max_height = max(heights)
    print(str(total_width)+" by "+str(max_height))
    #create matching new image
    new_im = Image.new('RGBA', (total_width, max_height))
    new_im.paste(cardImage[0], (0,0))
    #add sigils
    images = [Image.open(x) for x in ['Sigils/Ability_flying.png','Sigils/Ability_Brittle.png', 'Sigils/Ability_HostageFile.png']]
    y_offset = 0
    for im in images:
        new_im.paste(im, (0,y_offset), im.convert("RGBA"))
        y_offset += im.size[0]
    new_im.save('temp.png')
    with open("temp.png", "rb") as fh:
        f = discord.File(fh, filename="temp.png")
    await ctx.send(content=card,file=f)

bot.run(TOKEN)
