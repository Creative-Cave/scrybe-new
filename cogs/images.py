import discord
import os
from discord.ext import commands
from main import GUILD_ID
import random
import random


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        guild_ids=[GUILD_ID], name="layla", description="Get a random Layla image"
    )
    async def layla(self, ctx):
        image = os.path.join("./layla", random.choice(os.listdir("./layla")))
        await ctx.respond(file=discord.File(image))


def setup(bot):
    bot.add_cog(Images(bot))
