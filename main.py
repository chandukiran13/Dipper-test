import discord
import os
import requests
import json
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
#quote
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the stars ✨"))

@client.event
async def on_message(message):
  #checking bot
  if message.author.bot:
    return 
  #checking wether message is from a server or not
  if not message.guild:
    embed = discord.Embed(title = "Hello I'm Dipper",description="""If you want to invite me to your server
    This [here](https://discord.com/api/oauth2/authorize?client_id=788758779926806588&permissions=1043521&scope=bot "This is my normal Invite link") is my normal invite link
    This [here](https://discord.com/api/oauth2/authorize?client_id=788758779926806588&permissions=8&scope=bot "Admin link") is admin invite""",color=0x800080)
    await message.channel.send(embed=embed)
    return 
  """
  if message.channel.id == 787672271333621762:
    print(message.content)
    return
  """
  #storing the message in a var for easy usage
  msg = message.content 
  if msg == '$hello':
    await message.channel.send("Welp... hi")
    return

  if msg == '$inspire':
    quote = get_quote()
    await message.channel.send(quote)
    del quote
    return

  if msg == "$ping":
    lat = int(client.latency*1000)
    await message.channel.send("my latency is `"+str(lat)+"ms`")
    del lat
    return
    
  if msg.startswith("$embed"):
    if not message.guild.id == 787672270364475432:
      return
    msg=msg[6:]
    lis_t = msg.split("|",1)
    if len(lis_t) <2:
      await message.channel.send("Requirements not satisfied. You have to have a | as a seperator between the title and message.")
      return
    embed = discord.Embed(title = lis_t[0],description = lis_t[1],color=0xFEFEFE)
    channel_req = client.get_channel(796322727316946981)
    await channel_req.send(embed = embed)
    del channel_req, lis_t, embed
    return

  if msg == '$check':
    e = discord.Embed(title="Hello how are you, Maybe I'm still alive",description="[check](https://youtu.be/fn3KWM1kuAw 'Hmm what are you doing?')",color = 250)
    await message.channel.send("Hello",embed = e)
    del e
    return

  #repeats a message
  if msg.startswith("$echo"):
    msg = msg[6:]
    spl = msg.split(" ",1)
    spl[0]="".join(filter(str.isdigit,spl[0]))
    if len(spl[0]) == 18:
      channel_req = client.get_channel(int(spl[0]))
      await channel_req.send(spl[1])
      del channel_req,spl
    else:
      await message.channel.send(msg)
    return
    
  #gender role
  if msg == '$gender':
    e = discord.Embed(title="Choose a Gender",description="""<@&748550073620758629> : :male_sign: ✧⋄⋆⋅⋆⋄✧⋄⋆⋅⋆⋄✧ <@&748550204491563059> : :female_sign: 
⋆⋄✧⋄⋆⋅⋆⋄✧⋄⋆ <@&748550335886393344> : :question: ⋆⋄✧⋄⋆⋅⋆⋄✧⋄⋆ """,color = 0xff9900)
    channel_req = client.get_channel(797354450603606037)
    await channel_req.send("",embed = e)
    del e,channel_req
    return

  #color role
  if msg == '$color':
    e = discord.Embed(title="",description="""<@&797364090300399647>: :womans_hat:‏‏‎ ‎ ‎ ‎⋆ ★ ⋆‏‏‎ ‎ ‎ <@&776056680521531412>: :sunflower:
<@&776056536946442241>: :tangerine:‏‏‎ ‎ ‎ ‎⋆ ★ ⋆‏‏‎ ‎ ‎ <@&797364285633855488>: :icecream:""",color = 0xf8ff6b)
    channel_req = client.get_channel(797354450603606037)
    await channel_req.send("",embed = e)
    del e,channel_req
    return

  #uber role
  if msg == '$uber':
    e = discord.Embed(title="React below to become an Uber",description="""An Uber is someone who is willing *to be pinged* to take people on:
:candle: Candle Runs
:sparkles: Winged Light Runs
:volcano:  Eden Runs
:office: Office Trips - must have TGC Cape""",color = 0x96f6ff)
    channel_req = client.get_channel(797354450603606037)
    await channel_req.send("",embed = e)
    del e,channel_req
    
keep_alive()
client.run(os.getenv('TOKEN'))