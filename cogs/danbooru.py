
import discord
from discord.ext import commands
from pybooru import Danbooru
from typing import Optional
import json
import urllib.request
import os
from random import randint
import cfg

dan = Danbooru(cfg.site)

class danbooru(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(name = "img")
  async def img(self, ctx, number_of_images, tags: Optional[str]):
    '''returns image(s) with specyfic tag(s) using danbooru\ntags have to be separated by [comma]'''
    x = 0
    while x < 10:
      random = randint(1, 1000)
      
      tags = tags.split(sep = ',')
      print(tags)
      tags = ' '.join(tags)
      print(tags)

      id_list = dan.post_list(limit = number_of_images, page = random, tags = tags)

      for i in id_list:

        json_str = json.dumps(i)
        json_object = json.loads(json_str)

        if json_object['file_size'] <= 8000000:

          print("file id ", json_object['id'])
          print("fileurl ", json_object['file_url'])
          print("file size ", json_object['file_size'])
        
          urllib.request.urlretrieve(json_object['file_url'], f"./art/{json_object['id']}.png")

          with open(f"./art/{json_object['id']}.png", 'rb') as fp:
            await ctx.send(file=discord.File(fp, f"./art/{json_object['id']}.png"))
        
          os.remove(f"./art/{json_object['id']}.png")
          x = 10
        else:
          x += 1

  @commands.command(name = "taglist")
  async def tag_list(self, ctx, name):
    '''returns tag(s) that contain(s) given string'''
    tags = dan.tag_list(name_matches = name)
    
    for tag in tags:
      await ctx.send("tag: {0} | posts: {1} | category: {2}".format(tag['name'],tag['post_count'] , tag['category']))

def setup(client):
  client.add_cog(danbooru(client))