
import discord
from discord.ext import commands
from pybooru import Danbooru
from typing import Optional
import json
import urllib.request
import os
from random import randint
import cfg

dan = Danbooru(cfg.site)    #creating object dan with given site

class danbooru(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(name = "img")
  async def img(self, ctx, number_of_images, tags: Optional[str]):
    '''returns image(s) with specyfic tag(s) using danbooru
    tags have to be separated by [comma]
    
    Ratings:

    "rating:explicit" or "rating:e"
    Search for posts that are rated explicit.
    
    "rating:questionable" or "rating:q"
    Search for posts that are rated questionable.

    "rating:safe" or "rating:s"
    Search for posts that are rated safe.

    Searching:

    "blonde_hair,blue_eyes"
    Search for posts that have both blonde hair and blue eyes.

    "~blonde_hair,~blue_eyes"
    Search for posts that have either blonde hair or blue eyes.

    "-blonde_hair,-blue_eyes"
    Search for posts that don't have blonde hair or blue eyes.

    "blonde_hair,*_(cosplay)"
    Search for posts that have blonde hair and at least one tag ending with "_(cosplay)".'''
    x = 0
    try:    #spliting tags for danbooru
      tags = tags.split(sep = ',')
      tags = ' '.join(tags)
    except:
      pass

    tags2 = str(tags)
    
    if tags == "None":    #cheking if tags were given
      a = [1]
    else:
      a = [1]

    b = dan.tag_list(name = tags)

    if a != []:   #checking if tags have any of spacial characters
      if "rating:" in tags2 or "-" in tags2 or "*" in tags2 or "~" in tags2:   #searching for special character
        a = [1]
      elif b == []:   #if given tags not exist b == [] so program must not be executed
        a = []
        await ctx.send("> there's no such tag")
      else:
        pass
    else:
      a = []  
      await ctx.send("> there's no such tag")

    while x < 10 and a != []:   #prefenting to big files for destroying the program
      random = randint(1, 1000)

      id_list = dan.post_list(limit = number_of_images, page = random, tags = tags) #getting posts

      for i in id_list:   #main loop

        json_str = json.dumps(i)    #changing python dict to json str
        json_object = json.loads(json_str)    #changing json str to json object

        if json_object['file_size'] <= 8000000:   #checking if file isn't to big
          
          print("file id ", json_object['id'])
          print("fileurl ", json_object['file_url'])
          print("file size ", json_object['file_size'])
          
          character = json_object['tag_string_character']   #list of charater names
          character = character.split(sep = ' ')

          embed = discord.Embed(title = character[0], colour = cfg.bot_colour)    #creating embed
          embed.set_author(name = f"author: {json_object['tag_string_artist']}")  #adding author to embed
          embed.set_footer(text = json_object['file_url'])                        #adding url to embed

          urllib.request.urlretrieve(json_object['file_url'], f"./art/{json_object['id']}.png") #saving file with image inside

          with open(f"./art/{json_object['id']}.png", 'rb') as fp:                    #opening file with image
            await ctx.send(embed = embed)                                             #sending embed
            await ctx.send(file = discord.File(fp, f"./art/{json_object['id']}.png")) #sending file
        
          os.remove(f"./art/{json_object['id']}.png")                                 #removing file

          f = open("./art/urls.txt", "a")                                   #opening txt file
          f.write(f"{json_object['file_url']} | {tags} | {character[0]}\n") #savinng url, tags and character name
          f.close()                                                         #closing file

          x = 10
        else:                                 #if file to big sending url
          x += 1
          ctx.send(json_object['file_url'])
          print("file to big")

  @commands.command(name = "taglist")     #command taglist created
  async def tag_list(self, ctx, name):
    '''returns tag(s) that contain(s) given string
    you have to include "*" before tag'''
    tags = dan.tag_list(name_matches = name, hide_empty = "yes", order = "name")  #getting tags
    
    for tag in tags:
      await ctx.send("> tag: {0} | posts: {1} | category: {2}".format(tag['name'],tag['post_count'] , tag['category']))         #sending tags to discord

def setup(client):
  client.add_cog(danbooru(client))
