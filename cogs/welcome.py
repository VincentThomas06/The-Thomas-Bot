from discord.ext import commands
import discord
import datetime



class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        embed = discord.Embed(title=f'Welcome @{member.display_name} {member.guild.name}!',
                    description='Go see #info and #rules to get started',
                    color=0x05cffc,)

        if member.bot != True:
            role = discord.utils.get(member.guild.roles, name="Member")
            await member.add_roles(role)
            embed.set_image(url=member.default_avatar_url)
        elif member.bot == True:
            role = discord.utils.get(member.guild.roles, name="BOT")
            embed.set_image(url=member.default_avatar_url)
            await member.add_roles(role)
        await self.bot.get_channel(692278898037096448).send(embed=embed)


def setup(bot):
    bot.add_cog(Welcome(bot))
