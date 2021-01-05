import discord
import os
import requests
import json
#import time
from keep_alive import keep_alive
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(member.name)
    await member.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
  if message.guild == null:
    return
  if message.author == client.user:
    return
  msg = message.content
  if msg == '$hello':
    await message.channel.send("welp...hi")
  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  if 'happy birthday' in msg.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')
  if msg == "$ping":
    lat = int(client.latency*1000)
    await message.channel.send("my latency is `"+str(lat)+"ms`")
  if msg.startswith('$check'):
    e = discord.Embed(title="Hello how are you, Maybe I'm still alive",description="[check](https://youtu.be/fn3KWM1kuAw 'Hmm what are you doing?')",color = 250)
    await message.channel.send("Hello",embed = e)
    del e
keep_alive()
client.run(os.getenv('TOKEN'))