#Import Stuff
import discord
import json
import requests
from weather import *

other_keywords = ('help', 'version')

client = discord.Client()

api_key = 'eb9d4b88480f4a672b237fb2b39fb156'


@client.event
async def on_ready():
    general_channel = client.get_channel(801062429731323925)
    await general_channel.send('Weather Bot is online!')
    await client.change_presence(status=discord.Status.online)

@client.event
async def on_disconnect():
    general_channel = client.get_channel(801062429731323925)
    await general_channel.send('Bye...')
    await client.change_presence(status=discord.Status.offline)
    
@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith('--'):
        if not message.content.endswith(other_keywords):
            location = message.content.replace('--', '').lower()
            if len(location) >= 1:
                url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
                try:
                    data = json.loads(requests.get(url).content)
                    data = parse_data(data)
                    await message.channel.send(embed = weather_messages(data, location))
                except KeyError:
                    await message.channel.send(embed = error_message(location))

client.run('Nzk5MzM1MDE0MzE0OTM0Mjcy.YACEvg.EFTYzAygVcjt0ccXLgytE-BhoUE')