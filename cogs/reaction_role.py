import discord
from discord.ext import commands
from discord.utils import get, find
import os
import time

class ReactionRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Reaction Role Commands | Cog Loaded')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 813022659675684935:
            guild_id = payload.guild_id
            guild = find(lambda g : g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == 'pt':
                role = get(guild.roles, name='pt')

            elif payload.emoji.name == '🐀':
                role = get(guild.roles, name='Pungråtta')

            elif payload.emoji.name == 'micecraft_block':
                role = get(guild.roles, name='Minecraft')

            elif payload.emoji.name == 'AssettoCorsa':
                role = get(guild.roles, name='AssettoCorsa')

            elif payload.emoji.name == 'Member':
                role = get(guild.roles, name='Member')
            else:
                role = get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print('done')
                else:
                    print('Member not found')
            else:
                print('Role not found')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 813022659675684935:
            guild_id = payload.guild_id
            guild = find(lambda g : g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == 'pt':
                role = get(guild.roles, name='pt')

            elif payload.emoji.name == '🐀':
                role = get(guild.roles, name='Pungråtta')

            elif payload.emoji.name == 'micecraft_block':
                role = get(guild.roles, name='Minecraft')

            elif payload.emoji.name == 'AssettoCorsa':
                role = get(guild.roles, name='AssettoCorsa')

            elif payload.emoji.name == 'Member':
                role = get(guild.roles, name='Member')
            else:
                role = get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print('done')
                else:
                    print('Member not found')
            else:
                print('Role not found')

def setup(bot):
    bot.add_cog(Reaction_role(bot))
