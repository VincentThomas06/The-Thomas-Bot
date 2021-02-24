import discord
from discord.ext import commands
from pretty_help import PrettyHelp, Navigation
from discord.utils import get
from dotenv import load_dotenv
import time
load_dotenv()
import json
import os



def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


log_channel_id = 812780688881221633
total_time = time.gmtime()

nav = Navigation("⬅️", "➡️", "🛑")
color = 0x05cffc


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=get_prefix, intents = intents, description = 'A Bot that does everything! By: DK', case_insensitive=True, help_command = PrettyHelp(navigation=nav, color=color, active_time=30))

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)



@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.command(name='changeprefix')
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix = {prefix}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=prefix + 'help'))


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='prefix + help'))
    print(f'{bot.user.name} is Ready!')




for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')




bot.run(os.getenv('TOKEN'))
