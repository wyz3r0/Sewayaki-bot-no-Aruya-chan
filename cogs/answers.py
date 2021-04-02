
from discord.ext import commands

class answers(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f'> pong {round(self.client.latency * 1000)}ms')

  @commands.command()
  async def hello(self, ctx):
    await ctx.send("> Hellow~")

def setup(client):
  client.add_cog(answers(client))
