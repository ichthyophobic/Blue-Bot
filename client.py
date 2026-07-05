import discord
from discord import app_commands

class Client(discord.Client):

    def __init__(self, guild_id) -> None:
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.guild = discord.Object(guild_id)

    async def on_ready(self):
        # Successful login message
        print(f'Successfully logged in as {self.user}')
        # Setting activity
        await self.change_presence(
            activity=discord.Game("Roblox")
        )

    async def setup_hook(self) -> None:
        # Syncing commands to our guild
        await self.tree.sync(guild=self.guild)
