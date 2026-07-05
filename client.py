import discord
from discord import app_commands
from commands import fetch_commands

class Client(discord.Client):

    def __init__(self, guild_id) -> None:
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.guild = discord.Object(id=guild_id)

    async def on_ready(self):
        # Successful login message
        print(f'Successfully logged in as {self.user}')
        # Setting activity
        await self.change_presence(
            activity=discord.Game("Open-Source")
        )

    async def setup_hook(self):
        print('Syncing commands...')
        fetch_commands(self.tree, self.guild)
        synced = await self.tree.sync(guild=self.guild)
        print("Synced:", [cmd.name for cmd in synced])
