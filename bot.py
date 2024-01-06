import logging
import nextcord
from nextcord.ext import commands


logger = logging.getLogger("nextcord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="nextcord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(
    intents=intents,
    allowed_mentions=nextcord.AllowedMentions(
        everyone=False, roles=True, users=True, replied_user=True
    ),
    owner_id=914452175839723550,
)
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")
    logger.info(f"Logged in as {bot.user} ({bot.user.id})")

# This gets called, but the one in exts/errors.py doesn't. Doesn't matter if this is commented out or not.

# @bot.event
# async def on_error(interaction: nextcord.Interaction, error):
#     """
#     For hiding traceback for handdeled errors.
#     """
#     print("I am being triggered (bot.py) :)")


exts = ["exts.errors"]
for ext in exts:
    bot.load_extension(ext)
    print(f"Loaded extension {ext}")
    logger.info(f"Loaded extension {ext}")

bot.run("TOKEN") # Replace TOKEN with your bot token.