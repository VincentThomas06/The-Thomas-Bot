from discord.ext import commands
import discord
import time



class Basic_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.4)
        print('Misc Commands | Cog Loaded')



    @commands.command(name='version', brief='Shows what version the bot is')
    async def version(self, ctx):
        versionEmbed = discord.Embed(title= 'Current Version:', description= 'Alpha stage', color=0x05cffc)
        versionEmbed.add_field(name='Version Code:', value='v0.1', inline=False)
        versionEmbed.add_field(name='Date Released:', value='January 19th, 2021', inline=False)
        versionEmbed.set_footer(text='Created by Vincent aka @LarsOlof1337 (DK)')
        versionEmbed.set_author(name="The Thomas Bot")
        await ctx.send(embed = versionEmbed)
        print(ctx.command.name.capitalize() + ' was executed successfully')



def setup(bot):
    bot.add_cog(Basic_Commands(bot))
