#Import Stuff
import discord
import json
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingRole


api_key = 'eb9d4b88480f4a672b237fb2b39fb156'
#Client
client = commands.Bot(command_prefix='--')
client.remove_command('help')
reaction_title = ''
reactions = {}



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
        description= '--help/--commands (This command)\n--version (gives you the version of this bot)\n--dm (Dm\'s you)\n--(location) (This tells you the weather for your location)\nThere is more to come... stay tuned!', color=0x05cffc)
        
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
@has_permissions(administrator = True)
async def kick(context, member: discord.Member):
    try:
        CommandInvokeError = ('Whops! Something went wrong... either you\'ve spellt it wrong or you tried to kick a Admin')
        await member.kick()
        await context.send('User ' + member.display_name + ' has been kicked')
    except:
        await context.send(CommandInvokeError)

@client.command(name = 'ban', pass_context = True)
@has_permissions(administrator = True)
async def ban(context, member: discord.Member, *, reason = None):

    await member.ban(reason=reason)
    await context.send('User ' + member.display_name + ' has been banned')


@client.command(name='reaction_create_post')
async def reaction_create_post(context):

    embed = discord.Embed(title='React Here for Role!', color = 0x05cffc)
    embed.add_field(name='Set Title', value = '--reaction_set_title \'New Title\'', inline = False)
    embed.add_field(name='Add Role', value = '--reaction_add_role @Role EMOJI_HERE', inline = False)
    embed.add_field(name='Remove Role', value = '--reaction_remove_role @Role', inline = False)
    
    await context.send(embed=embed)
    await context.message.delete()

@client.command(name='reaction_set_title')
async def reaction_set_title(context, new_title):

    global reaction_title
    reaction_title = new_title
    await context.send('The title for the message is now `' + reaction_title + '`!')
    await context.message.delete()


@client.command(name='reaction_add_role')
async def reaction_add_role(context, role: discord.Role, reaction):

    if role != None:
        reactions[role.name] = reaction
        await context.send('Role `' + role.name + '` has been added with the emoji ' + reaction)
        await context.message.delete()
    else:
        await context.send('Please try again')

    print(reactions)


@client.command(name='reaction_remove_role')
async def reaction_remove_role(context, role: discord.Role):

    if role.name in reactions:
        del reactions[role.name]
        await context.send('Role `' + role.name + '` has been deleted!')
        await context.message.delete()
    else:
        await context.send('That role was not added!')

    print(reactions) 


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