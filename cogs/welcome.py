from discord.ext import commands
import discord



class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_member_join(self, member): #type your server name
        embed = discord.Embed(title=f'Welcome {member.name} {member.guild.name}!',
                    description='Go see #info and #rules to get started',
                    color=0x05cffc)
        await self.bot.get_channel(692278898037096448).send(embed=embed)
        role = discord.utils.get(member.guild.roles, name="Member")
        await member.add_roles(role)



def setup(bot):
    bot.add_cog(Welcome(bot))
