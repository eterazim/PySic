import discord
from discord.ext import commands
from discord.ext.commands import Bot
import youtube_dl
import random

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

depression = 0

class music(commands.Cog):
   def __init__(self, client):
      self.client = client
   
   @commands.command()
   async def join(self,ctx):
        if ctx.author.voice is None:
           await ctx.send("Dumbass you aren't in a vc")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
           await voice_channel.connect()
        else:
           await ctx.voice_client.move_to(voice_channel)
      
   @commands.command()
   async def disconnect(self,ctx):
       await ctx.voice_client.disconnect()

   @commands.command()
   async def play(self,ctx,url):
       ctx.voice_client.stop()
       FFMPEP_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
       YDL_OPTIONS = {'format':"bestaudio"}
       vc = ctx.voice_client

       with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
         info = ydl.extract_info(url, download=False)
         url2 = info['formats'][0]['url']
         source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEP_OPTIONS)
         vc.play(source)

   @commands.command()
   async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Ight ight, its stoppin what a party pooper")

   @commands.command()
   async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Ayy, the partys back on")
  
   @commands.command()
   async def bruh(self,ctx):
      await ctx.send("Damn bro that is a real bruh moment")

   @commands.command()
   async def dumbassmoment(self,ctx):
     await ctx.send("fucking dumbass")
  
   @commands.command()
   async def short(self,ctx):
     with open('short.gif', 'rb') as f:
      picture = discord.File(f)
      await ctx.send(file=picture)
   
   @commands.command()
   async def cooltest(self,ctx):
     await ctx.send("Performing Cool Test:")
     n = random.randint(1,2)
     if n == 1:
       await ctx.send("Damn bro the tests came back you're lookin pretty cool")
     if n == 2:
       await ctx.send("Sheesh the uncoolness is off the charts")
    
   @commands.command()
   async def basedtest(self,ctx):
     await ctx.send("Based Test in progress")
     n = random.randint(1,2)
     if n == 1:
       await ctx.send("Holy shit my based detector is off the charts")
     if n == 2:
       await ctx.send("I can't believe im saying this but you're looking unbased")

   @commands.command()
   async def hoesmad(self,ctx):
     await ctx.send("Fertlizer moment")
     with open('hoesmad.mp4', 'rb') as f:
       picture = discord.File(f)
       await ctx.send(file=picture)

   @commands.command()
   async def whowon(self,ctx):
     await ctx.send("Figuring out the truth")
     w = random.randint(1,2)
     if w == 1:
       await ctx.send("Liam is the true winner according to my calcuations")
     if w == 2:
       await ctx.send("Evy has won god damn liam you gotta be more based")

   @commands.command()
   async def depressioncount(self,ctx):
      await ctx.send(depression)     
          
def setup(client):
   client.add_cog(music(client))
