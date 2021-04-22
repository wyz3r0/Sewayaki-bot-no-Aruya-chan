
import cfg
from discord import Embed
from discord.ext import menus
from discord.ext import commands
from discord.utils import get
from typing import Optional

def syntax(command):
	cmd_and_aliases = "|".join([str(command), *command.aliases])
	params = []

	for key, value in command.params.items():
		if key not in ("self", "ctx"):
			params.append(f"[{key}]" if "NoneType" in str(value) else f"<{key}>")

	params = " ".join(params)

	return f"`{cfg.bot_prefix}{cmd_and_aliases} {params}`"

"""
class help_menue(ListPageSources):
  def __init__(self, ctx, data):
    self.ctx = ctx

    super().__init__(data, per_page = 3)

  async def write_page(self, menu, fielsd = []):
    return

  async def format_page(self, menu, commands):
    fields = []

    for cmd in commands:
      fields.appaend()
"""


class help(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.client.remove_command("help")

  async def cmd_help(self, ctx, command):
    embed = Embed(title = f"`{command}`", description = syntax(command), colour = cfg.bot_colour)
    embed.add_field(name="Command description", value=command.help)
    await ctx.send(embed=embed)

  @commands.command(name = "help", aliases = ["h"])
  async def h(self, ctx, cmd: Optional[str]):
    """shows this message"""
    if cmd is None:
      pass

    else:
      if (command := get(self.client.commands, name = cmd)):
        await self.cmd_help(ctx, command)

      else:
        await ctx.send(f"> {cmd} dose not exist")


def setup(client):
  client.add_cog(help(client))
