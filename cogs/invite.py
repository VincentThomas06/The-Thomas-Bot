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


    @commands.command(name='invitebot')
    async def invitebot(self, ctx):
        embed = discord.Embed(title='**Invite Link:**', brief="Invites the bot in your servers!", description='**[Invite Me!](https://discord.com/api/oauth2/authorize?client_id=799335014314934272&permissions=8&scope=bot)**')

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Invite(bot))
