# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.command(name='Inscrybe')
async def start_match(ctx, oponent='bot'):
    guild = ctx.guild
    channel = client.get_channel(channel_id) #  Gets channel from internal cache
    await channel.send("hello "+message.author+" and "+oponent+"!") #  Sends message to channel

bot.run(TOKEN)
