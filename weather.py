import discord



key_features = {
    'temp' : 'Temperature',
    'feels_like' : 'Feels Like',
    'temp_min' : 'Minimum Temperature',
    'temp_max' : 'Maximun Temperature'    
}

def parse_data(data):
    data = data['main']
    del data['humidity']
    del data['pressure']
    return data

def weather_messages(data, location):
    location = location.title()
    message = discord.Embed(title = f'{location} Weather', description = f'Here is the weather for {location}.', color = 0x05cffc)
    for key in data:
        message.add_field(name  = key_features[key], value = str(data[key]), inline = False)
    return message

def error_message(location):
    location = location.title()
    return discord.Embed(title = 'Nu blir det mega Error...', description = f'There was an error findi {location}.', color = 0x05cffc)
