from nextcord import Interaction, slash_command, Message
from nextcord.ext import commands

class SomeError(Exception):
    def __init__(self):
        self.message = "I am an error :)"

class Error(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_error(self, interaction: Interaction, error):
        # This doesn't get called. Doesn't matter if the one in bot.py is commented out or not.
        print("I am not being trigerred :(")
    
    @slash_command()
    async def ping(self, interaction: Interaction):
        await interaction.send(f"Pong! {self.bot.latency * 1000}ms. Send a message to trigger an error.")
    
    @commands.Cog.listener()
    async def on_message(self, message: Message):
        raise SomeError()

def setup(bot: commands.Bot):
    bot.add_cog(Error(bot))