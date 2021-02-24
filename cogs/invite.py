import discord
from discord.ext import commands
from discord.utils import get, find
import time

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.3)
        print('Invite Command | Cog Loaded')

    @commands.command(pass_context=True, brief='Creates an Invite with added functionality')
    async def createInvite(self, ctx, time_in_seconds,uses, ):
        invitelink = await discord.abc.GuildChannel.create_invite(ctx.message.channel, max_uses=uses,max_age=time_in_seconds)
        await ctx.send(invitelink)

def setup(bot):
    bot.add_cog(Invite(bot))
