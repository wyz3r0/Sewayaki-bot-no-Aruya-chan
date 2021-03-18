
import discord
import os
from keep_me_alive import keep_me_alive
from replit import db

client = discord.Client()

symbol = '>'

def 

@client.event
async def on_ready():
  print('Ohayo gozaimasu~ Aruyadesu')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith(symbol + 'hello'):
    await message.channel.send('Hellow~')

  if message.content.startswith(symbol + 'symbol'):
    await message.channel.send('So what do you want me to react to?')


keep_me_alive()
client.run(os.getenv('token'))