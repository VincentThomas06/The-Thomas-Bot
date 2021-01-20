#Import Stuff
import discord
import json
import requests
from discord.ext import commands

api_key = 'eb9d4b88480f4a672b237fb2b39fb156'
#Client
client = commands.Bot(command_prefix='--')
client.remove_command('help')

# -- + Command Code
@client.command(name='version')
async def version(context):

    versionEmbend = discord.Embed(title= 'Current Version:', description= 'Early alpha stage', color=0x05cffc)
    versionEmbend.add_field(name='Version Code:', value='v0.1', inline=False)
    versionEmbend.add_field(name='Date Released:', value='January 19th, 2021', inline=False)
    versionEmbend.set_footer(text='Created by Vincent aka @LarsOlof1337 (DK)')

    await context.message.channel.send(embed = versionEmbend)


@client.command(name='help')
async def help(context):

    helpEmbend = discord.Embed(
        title= 'Here are some Commands\nyou can use with this bot:', 
        description= '--help\--commands (This command)\n--version (gives you the version of this bot)\n--dm (Dm\'s you)\n--(location) (This tells you the weather for your location)\nThere is more to come... stay tuned!', color=0x05cffc)
        
    await context.message.channel.send(embed = helpEmbend)

@client.command(name = 'commands')
async def commands(context):

    helpEmbend = discord.Embed(
        title= 'Here are some Commands\nyou can use with this bot:', 
        description= '--help/--commands (This command)\n--version (gives you the version of this bot)\n--dm (Dm\'s you)\n--(location) (This tells you the weather for your location)\nThere is more to come... stay tuned!', color=0x05cffc)
        
    await context.message.channel.send(embed = helpEmbend)

@client.command(name='dm')
async def dm(context):

    await context.message.author.send('This is a DM. Have a good day!')


@client.command(name = 'kick', pass_context = True)
@commands.has_permission(kick_members = True)
async def kick(context, member: discord.Member):
    await member.kick()
    await conxext.send('User ' + member.display_name + 'has been kicked')



@client.event
async def on_ready():
    
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'--help'))
    general_channel = client.get_channel(801062429731323925)
    await general_channel.send('Up\'n\'running boss!')


#status=discord.Status., 

@client.event
async def on_disconnect():
    general_channel = client.get_channel(801062429731323925)
    await general_channel.send('Adding more features to me? You\'ll love my better me!')
    await client.change_presence(status=discord.Status.offline)





client.run('Nzk5MzM1MDE0MzE0OTM0Mjcy.YACEvg.EFTYzAygVcjt0ccXLgytE-BhoUE')