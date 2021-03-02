
import discord
from discord.ext import commands
color = 0x05cffc

class ErrorHandling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            Missing_command_embed = discord.Embed(title='MissingRequiredArgument', timestamp=ctx.message.created_at, color=0xFF0000)
            Missing_command_embed.add_field(name=error, value='Invalid command, type `@mention + help` for usable commands!')
            Missing_command_embed.set_author(name='ERROR!!!')
            Missing_command_embed.set_image(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.windowslatest.com%2Fwp-content%2Fuploads%2F2020%2F06%2FWindows-10-BSOD-error.jpg&f=1&nofb=1')
            await ctx.send(embed=Missing_command_embed)

        if isinstance(error, commands.MissingRequiredArgument):
            Missing_embed = discord.Embed(title='MissingRequiredArgument', timestamp=ctx.message.created_at, color=0xFF0000)
            Missing_embed.add_field(name=error, value='Invalid use of command, type `prefix + help` for usable commands!')
            Missing_embed.set_author(name='ERROR!!!')
            Missing_embed.set_image(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.windowslatest.com%2Fwp-content%2Fuploads%2F2020%2F06%2FWindows-10-BSOD-error.jpg&f=1&nofb=1')
            await ctx.send(embed=Missing_embed)

        if isinstance(error, commands.MissingRole):
            Missing_Role_embed = discord.Embed(title='MissingRole', timestamp=ctx.message.created_at, color=0xFF0000)
            Missing_Role_embed.add_field(name=error, value='**Invalid use of command, type `prefix + help` for usable commands!**')
            Missing_Role_embed.set_author(name='ERROR!!!')
            Missing_Role_embed.set_image(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.windowslatest.com%2Fwp-content%2Fuploads%2F2020%2F06%2FWindows-10-BSOD-error.jpg&f=1&nofb=1')
            await ctx.send(embed=Missing_Role_embed)

def setup(bot):
    bot.add_cog(error_handling(bot))
