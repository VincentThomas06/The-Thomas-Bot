#Import Stuff
import discord
import logging
import json
from discord.member import Member
import requests
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions, MissingRole


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='--', intents = intents)

api_key = 'eb9d4b88480f4a672b237fb2b39fb156'
bot.remove_command('help')
reaction_title = ''
reactions = {}
reaction_message_id = ""



# -- + Command Code
@bot.command(name='version')
async def version(context):

    versionEmbed = discord.Embed(title= 'Current Version:', description= 'Early alpha stage', color=0x05cffc)
    versionEmbed.add_field(name='Version Code:', value='v0.0.5', inline=False)
    versionEmbed.add_field(name='Date Released:', value='January 19th, 2021', inline=False)
    versionEmbed.set_footer(text='Created by Vincent aka @LarsOlof1337 (DK)')
    versionEmbed.set_author(name="The Thomas Bot")

    await context.message.channel.send(embed = versionEmbed)
    await context.message.delete()


@bot.command(name='help')
async def help(context):

    helpEmbend = discord.Embed(
        title= 'Here are some Commands\nyou can use with this bot:', 
        description= '--help/--commands (This command)\n--version (gives you the version of this bot)\n--dm (Dm\'s you)\n--(location) (This tells you the weather for your location)\n--ban [@Person] (Only Admins can do this, and you cant ban Admins)\n--kick [@Person] (Only Admins can do this, and you cant kick Admins)\n--ping (Checks how much of a delay the bot has)\nThere is more to come... stay tuned!', color=0x05cffc)
        
    await context.message.channel.send(embed = helpEmbend)
    await context.message.delete()

@bot.command(name = 'commands')
async def commands(context):

    helpEmbend = discord.Embed(
        title= 'Here are some Commands\nyou can use with this bot:', 
        description= '--help/--commands (This command)\n--version (gives you the version of this bot)\n--dm (Dm\'s you)\n--(location) (This tells you the weather for your location)\n--ban [@Person] (Only Admins can do this, and you cant ban Admins)\n--kick [@Person] (Only Admins can do this, and you cant kick Admins)\n--ping (Checks how much of a delay the bot has)\nThere is more to come... stay tuned!', color=0x05cffc)
        
    await context.message.channel.send(embed = helpEmbend)
    await context.message.delete()
@bot.command(name='dm')
async def dm(context):

    await context.message.author.send('This is a DM. Have a good day!')
    await context.message.delete()

@bot.command(aliases=['latency'])
async def ping(ctx):
    await ctx.send(f'The current latency is: {round(bot.latency * 1000)} milliseconds')








@bot.command(name = 'kick', pass_context = True)
@has_permissions(administrator = True)
async def kick(context, member: discord.Member):
    try:
        
        await member.kick()
        await context.send('User ' + member.display_name + ' has been kicked')
        await context.message.delete()
    except:
        CommandInvokeError = ('Whops! Something went wrong... either you\'ve spellt it wrong or you tried to kick a Admin')
        await context.send(CommandInvokeError)

@bot.command(name = 'ban', pass_context = True)
@has_permissions(administrator = True)
async def ban(context, member: discord.Member, *, reason = None):

    await member.ban(reason=reason)
    await context.send('User ' + member.display_name + ' has been banned')


@bot.command(name='reaction_create_post')
async def reaction_create_post(context):

    embed = discord.Embed(title='React Here for Role!', color = 0x05cffc)
    embed.add_field(name='Set Title', value = '--reaction_set_title \"New Title\"', inline = False)
    embed.add_field(name='Add Role', value = '--reaction_add_role @Role EMOJI_HERE', inline = False)
    embed.add_field(name='Remove Role', value = '--reaction_remove_role @Role', inline = False)
    embed.add_field(name='Send Post', value = '--reaction_send_post', inline = False)
    
    await context.send(embed=embed)
    await context.message.delete()

@bot.command(name='reaction_set_title')
async def reaction_set_title(context, new_title):

    global reaction_title
    reaction_title = new_title
#    await context.send('The title for the message is now `' + reaction_title + '`!')
    await context.message.delete()


@bot.command(name='reaction_add_role')
async def reaction_add_role(context, role: discord.Role, reaction):

    if role != None:
        reactions[role.name] = reaction
        await context.send('Role `' + role.name + '` has been added with the emoji ' + reaction)
        await context.message.delete()
    else:
        await context.send('Please try again')

    print(reactions)


@bot.command(name='reaction_remove_role')
async def reaction_remove_role(context, role: discord.Role, reaction):

    if role != None:
        reactions[role.name] == reaction
        del reaction
#        await context.send('Role `' + role.name + '` has been deleted!')
        await context.message.delete()
    else:
        await context.send('That role was not added!')

    print(reactions) 


@bot.command(name='reaction_send_post')
async def reaction_send_post(context):

    description = 'React to add all the roles!\n'
    for role in reactions:
        description += '`' + role + '` - ' + reactions[role] + '\n'

    embed = discord.Embed(title = reaction_title, description=description, color = 0x05cffc)
    embed.set_author(name='The Thomas Bot')

    message = await context.send(embed=embed)

    global reaction_message_id
    reaction_message_id = str(message.id)

    for role in reactions:
        await message.add_reaction(reactions[role])
    
    await context.message.delete()


@bot.command(name='rules')
async def rules(context):
        
    rules_embed = discord.Embed(title = 'Rules:', description = 'test', color = 0x5cffc)
    rules_embed.add_field(name = 'hello', value = 'add field value', inline = False)
    rules_embed.set_author(name = 'The Thomas Bot')
    
    await context.message.delete()
    
    await context.send(embed = rules_embed)
    

            
@bot.event
async def on_reaction_add(reaction, user):

    if not user.bot:

        message = reaction.message

        if str(message.id) == reaction_message_id:
            
            role_to_give = ""

            for role in reactions:
                if reactions[role] == reaction.emoji:
                    role_to_give = role

            role_for_reaction = discord.utils.get(user.guild.roles, name = role_to_give)
            await user.add_roles(role_for_reaction)


@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, name='Member')
    await member.add_roles(role)
    print(f'{member} was given role Member')



@bot.event
async def on_ready():
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'--help'))
    general_channel = bot.get_channel(801062429731323925)
    await general_channel.send('Up\'n\'running boss!')
    print('The Bot is Online!')


#status=discord.Status., 

@bot.event
async def on_disconnect():
    general_channel = bot.get_channel(801062429731323925)
    await general_channel.send('Adding more features to me? You\'ll love my better me!')
    await bot.change_presence(status=discord.Status.online)
    print('The bot is offline!')





bot.run('Nzk5MzM1MDE0MzE0OTM0Mjcy.YACEvg.EFTYzAygVcjt0ccXLgytE-BhoUE')