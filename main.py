import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

GUILD_ID = 915996676144111706
ROOT_DIR = Path(__file__).parent

load_dotenv()

bot = discord.Bot(intents=discord.Intents.all())

# Load cogs in ./cogs
for filename in os.listdir(ROOT_DIR / "cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.slash_command(
    guild_ids=[GUILD_ID],
    name="refresh",
    description="Refreshes the bot's cogs",
)
@commands.has_permissions(administrator=True)
async def refresh(ctx):
    response = await ctx.respond("Reloading cogs...")
    for filename in os.listdir(ROOT_DIR / "cogs"):
        if filename.endswith(".py"):
            await response.edit_original_response(
                content=f"Reloading `{filename[:-3]}`"
            )
            bot.reload_extension(f"cogs.{filename[:-3]}")

    await response.edit_original_response(content="✔ Cogs reloaded")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.check
async def globally_block_dms(ctx):
    # Return false if the guild is None
    # This will block commands from being run in DMs to eliminate permission-based security risks
    return ctx.guild is not None


def run():
    load_dotenv()
    bot.run(os.getenv("BOT_TOKEN"))


if __name__ == "__main__":
    run()
