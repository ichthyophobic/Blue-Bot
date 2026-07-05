from discord import Guild, HTTPException, Member, app_commands
from discord import Interaction
from datetime import timedelta

def fetch_moderation_commands(tree: app_commands.CommandTree):

    async def permission_check(
        interaction: Interaction,
        member: Member,
        ) -> bool:

        assert isinstance(interaction.user, Member)
        assert isinstance(interaction.guild, Guild)

        if member == interaction.user:
            await interaction.response.send_message(
                "You can't moderate yourself.",
                ephemeral=True,
            )
            return False

        if member == interaction.guild.owner:
            await interaction.response.send_message(
                "You can't moderate the owner.",
                ephemeral=True,
            )
            return False

        if interaction.user.top_role <= member.top_role:
            await interaction.response.send_message(
                "Error: You have a lower or equal role to member.",
                ephemeral=True,
            )
            return False

        if interaction.guild.me.top_role <= member.top_role:
            await interaction.response.send_message(
                "Error: The member has higher permissions than me.",
                ephemeral=True,
            )
            return False

        return True

    @tree.command(name='kick', description='Kick a member')
    @app_commands.guild_only()
    @app_commands.default_permissions(kick_members=True)
    @app_commands.checks.has_permissions(kick_members=True)
    @app_commands.checks.bot_has_permissions(kick_members=True)
    async def kick(
        interaction: Interaction,
        member: Member,
        reason: str | None = None
    ):

        if not await permission_check(interaction, member):
            return

        reason = reason or "Not specified"

        try:
            await member.kick(reason=reason)
        except HTTPException:
            await interaction.response.send_message(
                "Error: Failed to kick member due to Discord API error.",
                ephemeral=True,
            )
        else:
            await interaction.response.send_message(
                f"Successfully kicked the member {member.mention}.\nReason: {reason}"
            )

    @tree.command(name='ban', description='Ban a member')
    @app_commands.guild_only()
    @app_commands.default_permissions(ban_members=True)
    @app_commands.checks.has_permissions(ban_members=True)
    @app_commands.checks.bot_has_permissions(ban_members=True)
    async def ban(
        interaction: Interaction,
        member: Member,
        reason: str | None = None
    ):

        if not await permission_check(interaction, member):
            return

        reason = reason or 'Not specified'

        try:
            await member.ban(reason=reason)
        except HTTPException:
            await interaction.response.send_message(
                "Error: Failed to ban member to Discord API error.",
                ephemeral=True,
            )
        else:
            await interaction.response.send_message(
                f"Successfully banned the member {member.mention}.\nReason: {reason}"
            )

    @tree.command(name='timeout', description='Timeout a member')
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(moderate_members=True)
    @app_commands.checks.bot_has_permissions(moderate_members=True)
    async def timeout(
        interaction: Interaction,
        member: Member,
        duration: int | None = None,
        reason: str | None = None
    ):

        if not await permission_check(interaction, member):
            return

        reason = reason or 'Not specified'
        duration = duration or 5

        if duration < 1 or duration > 28 * 24 * 60:
            await interaction.response.send_message(
                "The duration must be from 1 minute to 28 days.",
                ephemeral=True,
            )
            return

        try:
            await member.timeout(timedelta(minutes=duration), reason=reason)
        except HTTPException:
            await interaction.response.send_message(
                "Error: Failed to timeout member to Discord API error.",
                ephemeral=True,
            )
        else:
            await interaction.response.send_message(
                f"Successfully timed out the member {member.mention}.\nDuration: {duration}\nReason: {reason}"
            )
