# Snoopin around are we?
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import music

depressioncount = 0

cogs = [music]

client = commands.Bot(command_prefix='?', case_insensitive=True, intents = discord.Intents.all())

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="Dodging cease and desist letters since 2021"))

@client.event
async def on_message(message):
      if 'womens rights' in message.content:
       with open('womensrights.png', 'rb') as f:
        picture = discord.File(f)
        await message.channel.send(file=picture)
      await client.process_commands(message)

      if message.attachments and message.channel.id == 888895928935780464: 
        await message.pin()
      await client.process_commands(message)

      if 'depression' in message.content:
        await message.channel.send("stfu fertlizer")
        depressioncount + 1
      await client.process_commands(message)

      if 'depression' in message.content and 'womens rights' in message.content:
        await message.channel.send("jesus christ your killing me here")
      await client.process_commands(message)

      if 'deep' in message.content:
        await message.channel.send(":eyes:")
      await client.process_commands(message)

      if 'based' in message.content:
        await message.channel.send("Based")
      await client.process_commands(message)


for i in range(len(cogs)):
  cogs[i].setup(client)

       
client.run("ODg4MTU2MTU2NTU0NTM5MDA5.YUOl4A.C9229nIltRQIMeCjItuCB-itJaM")

