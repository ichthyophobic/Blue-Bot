from discord.abc import Snowflake
from discord.app_commands import CommandTree
from .moderation import fetch_moderation_commands
from .ticketing import fetch_ticketing_commands
from .utility import fetch_utility_commands

def fetch_commands(tree: CommandTree, guild: Snowflake):
    print('Loading moderation commands...')
    fetch_moderation_commands(tree, guild)
    print('Loading ticketing commands...')
    fetch_ticketing_commands(tree, guild)
    print('Loading utility commands...')
    fetch_utility_commands(tree, guild)
