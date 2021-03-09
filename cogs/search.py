from googlesearch import search
from discord.ext import commands
import aiohttp
import discord
import time
color = 0x05cffc

class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.4)
        print('Search Commands | Cog Loaded')    
    
    
    
    @commands.command()
    async def search(self, ctx, *, query):
    	author = ctx.author.mention
    	await ctx.channel.send(f"**------------------ Results {author} ------------------**")
    	async with ctx.typing():
    		for j in search(query, tld="co.in", num=1, stop=1, pause=2):
    			await ctx.send(f"\n:point_right: {j}")

    @commands.command()
    async def pic(self, ctx, *, search):
        commands.ses = aiohttp.ClientSession()
        search = search.replace(' ', '')
        url = f'https://api.unsplash.com/photos/random?query={search}&orientation=squarish&content_filter=high&client_id=xdN4A4Oan38AvFGmVR_tnEtl_T5VjKsTk_Po5nbvN6k'
        async with commands.ses.get(url) as r:
            if r.status in range(200, 299):
                data = await r.json()
                url = data['urls']['regular']
                mbed = discord.Embed(title=f'Heres you\'re pic! | ' + search, color=color, timestamp=ctx.message.created_at)
                mbed.set_image(url=url)
                await ctx.send(embed=mbed)
            else:
                await ctx.send('Error when making request {}'.format(r.status))

def setup(bot):
    bot.add_cog(Search(bot))
