import discord
import time

from discord.ext import commands


class Admin_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot




    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.1)
        print('Admin Commands | Cog Loaded')


    @commands.command(name = 'kick', pass_ctx = True, brief='[Only Admins Can use this]')
    @commands.has_permissions(administrator = True)
    async def kick(self, ctx, member: discord.Member):
        try:

            await member.kick()
            await ctx.send('User ' + member.display_name + ' has been kicked')
            await ctx.message.delete()
            print(ctx.command.name + ' was executed successfully')
        except:
            Error = 'Sorry, that didn\'t! Either you tried to kick an Admin or you spelled the wrong name...'
            ctx.message.send('Error')



    @commands.command(name = 'ban', pass_ctx = True, brief='[Only Admins can use this]')
    @commands.has_permissions(administrator = True)
    async def ban(self, ctx, member: discord.Member, *, reason = None):

        await member.ban(reason=reason, brief='[Only Admins can use this]')
        await ctx.send('User ' + member.display_name + ' has been banned'),
        print(ctx.command.name + ' was executed successfully')



    @commands.command(name='clear', brief='[Only Admins can use this]')
    @commands.has_permissions(administrator = True)
    async def clear(self, ctx, amount = 1):
        await ctx.channel.purge(limit=amount+1)
        print(str(amount) + ' messages deleted')



    @commands.command(name='kill', aliases=['killswitch', 'k', 'RIP'])
    @commands.has_role('Bot-dev')
    async def logout(self, ctx):
        await bot.change_presence(status=discord.Status.offline)
        kill_embed = discord.Embed(title='Killing...', description='I was killed by @' + str(ctx.author), timestamp=ctx.message.created_at)
        channel = ctx.guild.get_channel(812780688881221633)
        await channel.send(embed=kill_embed)
        await commands.logout()



def setup(bot):
    bot.add_cog(Admin_Commands(bot))
