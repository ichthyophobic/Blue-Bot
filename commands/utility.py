from discord import Interaction, app_commands
from discord.abc import Snowflake

def fetch_utility_commands(tree: app_commands.CommandTree, guild: Snowflake):

    @tree.command(name='about', description='About the bot', guild=guild)
    async def about(interaction: Interaction):
        await interaction.response.send_message(
            "Blue Bot\n"
            "It's a free-to-use open-source project\n"
            "Source: https://github.com/ichthyophobic/Blue-Bot"
        )
