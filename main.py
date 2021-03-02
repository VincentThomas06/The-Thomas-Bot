import discord
from discord.ext import commands
from pretty_help import PrettyHelp, Navigation
import os
import time
import random

reaction = ['Spotify!', '@mention + help', '.help', '.support', 'All the servers', 'All the guilds']
reaction = random.choice(reaction)

intents = discord.Intents.default()
intents.members = True

nav = Navigation("⬅️", "➡️", "🛑")
color = 0x05cffc

bot = commands.Bot(commands.when_mentioned_or('.'), intents = intents, description = 'Prefix = \".\"\n**[Invite Me!](https://discord.com/api/oauth2/authorize?client_id=799335014314934272&permissions=8&scope=bot)**', case_insensitive=True, help_command = PrettyHelp(navigation=nav, color=color, active_time=30))

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=reaction))
    print(f'{bot.user.name} is Ready!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

TOKEN_KEY = os.getenv('TOKEN')
bot.run(TOKEN_KEY)
