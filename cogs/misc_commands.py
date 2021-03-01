from discord.ext import commands
import discord
import time

color = 0x05cffc

class Basic_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.4)
        print('Misc Commands | Cog Loaded')



    @commands.command(name='Info', brief='brief Info about the Bot')
    async def version(self, ctx):
        versionEmbed = discord.Embed(title= 'Current Version:', description= 'Alpha stage', color=0x05cffc)
        versionEmbed.add_field(name='Version Code:', value='v0.1', inline=False)
        versionEmbed.add_field(name='Date Released:', value='January 19th, 2021', inline=False)
        versionEmbed.set_footer(text='Created by Vincent aka @LarsOlof1337')
        versionEmbed.set_author(name="The Thomas Bot")
        await ctx.send(embed = versionEmbed)
        print(ctx.command.name.capitalize() + ' was executed successfully')

    @commands.command(name='Support')
    async def Support(self, ctx):
        supportembed = discord.Embed(title='Thomas Bot help', description='✅ If you are new to the bot type ´.help´\n\n🖱️ [Invite Me!](https://discord.com/api/oauth2/authorize?client_id=799335014314934272&permissions=8&scope=bot)', color=color)
        await ctx.send(embed=supportembed)
        print(ctx.command.name.capitalize() + ' was executed successfully')



def setup(bot):
    bot.add_cog(Basic_Commands(bot))
