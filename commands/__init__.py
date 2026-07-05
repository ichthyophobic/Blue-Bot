from discord.app_commands import CommandTree
from .moderation import fetch_moderation_commands
from .ticketing import fetch_ticketing_commands

async def fetch_commands(tree: CommandTree):
    fetch_moderation_commands(tree)
    fetch_ticketing_commands(tree)
