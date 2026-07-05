from discord import Guild, HTTPException, Member, app_commands
from discord import Interaction

def setup(tree: app_commands.CommandTree):

    async def permission_check(
        interaction: Interaction,
        member: Member,
        ) -> bool:

        assert isinstance(interaction.user, Member)
        assert isinstance(interaction.guild, Guild)

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
    async def kick(interaction: Interaction, member: Member, reason: str | None = None):

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
    async def ban(interaction: Interaction, member: Member, reason: str | None = None):

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
