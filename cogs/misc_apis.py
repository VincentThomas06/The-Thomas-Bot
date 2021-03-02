import discord
from discord.ext import commands
from aiohttp import request
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
color = 0x05cffc

class RandomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.5)
        print('Api Commands | Cog Loaded')

    @commands.command(name='f', aliases=['fact', 'facts about',])
    async def f(self, ctx, animal: str):
        if animal.lower() in ('dog', 'cat', 'panda', 'koala', 'bird', 'fox'):
            URL = f'https://some-random-api.ml/facts/{animal.lower()}'
            async with request("GET", URL, headers={}) as response:
                if response.status == 200:
                    data = await response.json()
                    fact = data['fact']
                    fact_embed = discord.Embed(title=f'**Fact | {animal.capitalize()}**', description=data['fact'], timestamp=ctx.message.created_at, color=color)
                    if animal.lower() in ('dog'):
                        URL = "https://api.thedogapi.com/v1/images/search/?api_key=b9b7d56f-fe95-4554-aacd-6fe6777ed06c"
                        async with request("GET", URL, headers={}) as response:
                            if response.status == 200:
                                doggo = await response.json()
                                doggo = doggo[0]
                                image = (doggo.get('url'))
                                doggo = (doggo.get('breeds'))
                                doggo = doggo[0]
                                race = (doggo.get('name'))
                                fact_embed = discord.Embed(title=f'**Fact | {animal.capitalize()}** | {race}', description=fact, timestamp=ctx.message.created_at, color=color)
                                fact_embed.set_image(url=image)
                    if animal.lower() in ('cat'):
                        URL = 'https://api.thecatapi.com/v1/images/search'
                        async with request("GET", URL, headers={}) as response:
                            if response.status == 200:
                                data = await response.json()
                                data = data[0]
                                fact_embed.set_image(url= data['url'])
                                print(data['url'])
                                print('Cat command executed')
            await ctx.send(embed=fact_embed)
            print(animal.capitalize() + ' command executed')
        else:
            await ctx.send(f'Hmm that animal doesn\'t seem to exist.. is {animal} an animal?')

    @commands.command(name='joke')
    async def joke(self, ctx):
        URL = "https://some-random-api.ml/joke"
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                advise_embed = discord.Embed(title="**Joke**", description=f"**{data['joke']}**", timestamp=ctx.message.created_at, color=color)
                await ctx.send(embed=advise_embed)

    @commands.command(name='jokewithresponse', aliases=['joke2', 'telljoke'])
    async def jokewithresponse(self, ctx):
        URL = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw&type=twopart'
        async with request("GET", URL) as response:
            if response.status == 200:
                data = await response.json()
                joke_embed = discord.Embed(title= '**' + (data.get('setup')) + '**', description='**||' + (data.get('delivery')) + '||**')
                joke_embed.set_author(name='Type: ' + (data.get('category')))
                await ctx.send(embed = joke_embed)

    @commands.command(name='meme')
    async def meme(self, ctx):
        URL = 'https://some-random-api.ml/meme'
        async with request('GET', URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                meme_embed = discord.Embed(title=data['category'].capitalize(), description=data['caption'].capitalize(), timestamp=ctx.message.created_at, color=color)
                meme_embed.set_image(url=data['image'])
                await ctx.send(embed=meme_embed)
            else:
                await ctx.send(f'API returned a {response.status} status.')

    @commands.command(name='advice')
    async def advice(self, ctx):
        URL = 'https://api.adviceslip.com/advice'
        response = requests.get(URL)
        data = response.json()['slip']
        await ctx.send(data.get('advice'))

def setup(bot):
    bot.add_cog(Random_Commands(bot))
