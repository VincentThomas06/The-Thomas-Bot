import discord
import asyncio
import requests
import time
from discord.ext import commands

color = 0x05cffc

class Covid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.1)
        print('Covid Command | Cog Loaded')

    @commands.command(name='c', alises=['corona', 'covid'], brief='.c {county} for corona stats')
    async def c(self, ctx, *, countryName = None):

        try:
            if countryName is None:
                embed=discord.Embed(title="This command is used like this: ``` .covid [country]```", colour=color, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)

            else:
                url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
                stats = requests.get(url)
                json_stats = stats.json()
                country = json_stats["country"]
                totalCases = json_stats["cases"]
                todayCases = json_stats["todayCases"]
                totalDeaths = json_stats["deaths"]
                todayDeaths = json_stats["todayDeaths"]
                recovered = json_stats["recovered"]
                active = json_stats["active"]
                critical = json_stats["critical"]
                casesPerOneMillion = json_stats["casesPerOneMillion"]
                deathsPerOneMillion = json_stats["deathsPerOneMillion"]
                totalTests = json_stats["totalTests"]
                testsPerOneMillion = json_stats["testsPerOneMillion"]
                embed2 = discord.Embed(title=f"**COVID-19 Status Of {country}**!", description=None, colour=color, timestamp=ctx.message.created_at)
                embed2.add_field(name="**Total Cases**", value=totalCases, inline=True)
                embed2.add_field(name="**Cases Today**", value=todayCases, inline=True)
                embed2.add_field(name="**Total Deaths**", value=totalDeaths, inline=True)
                embed2.add_field(name="**Deaths Today**", value=todayDeaths, inline=True)
                embed2.add_field(name="**Recovered**", value=recovered, inline=True)
                embed2.add_field(name="**Active**", value=active, inline=True)
                embed2.add_field(name="**Critical**", value=critical, inline=True)
                embed2.add_field(name="**Cases Per One Million**", value=casesPerOneMillion, inline=True)
                embed2.add_field(name="**Deaths Per One Million**", value=deathsPerOneMillion, inline=True)
                embed2.add_field(name="**Total Tests**", value=totalTests, inline=True)
                embed2.add_field(name="**Tests Per One Million**", value=testsPerOneMillion, inline=True)
                embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/564520348821749766/701422183217365052/2Q.png")
                await ctx.send(embed=embed2)
                level = 'INFO: '
                print(countryName.capitalize() + ' was executed successfully')
        except:
            embed3 = discord.Embed(title="Invalid Country Name Or API Error! Try Again..!", colour=0xff0000, timestamp=ctx.message.created_at)
            embed3.set_author(name="Error!")
            await ctx.send(embed=embed3)
            level = 'ERROR: '
            print('Covid: ' + countryName + ' failed to execute')

def setup(bot):
    bot.add_cog(Covid(bot))
