import discord

from src.instance import (
    bot, database, INewUser
)


class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='Стать жителем', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:        
        for role in interaction.user.roles:
            if role.id in [935224998744973413, 867354643264831498]:
                return await interaction.response.send_message(
                    'Вы уже вступили в город!',
                    ephemeral=True
                )

        new_user = INewUser(interaction.user.id, interaction.user.mention)
        is_added_new_user = await database.add_new_user(new_user)

        if not is_added_new_user:
            return await interaction.response.send_message(
                'Вы уже отправили заявку на вступление в город!',
                ephemeral=True
            )
        
        await interaction.response.send_message(
            'Ожидайте, скоро с Вами свяжется член приёмной комиссии', 
            ephemeral=True
        )

        channel = await bot.fetch_channel("982240175495184445")
        guild_roles = await channel.guild.fetch_roles()
        current_role = None

        for role in guild_roles:
            if role.id != 982230828731994142:
                continue
            current_role = role

        if current_role is None:
            return await channel.send(f"@here\nИгрок {interaction.user.mention} хочет стать жителем города!")
        
        await channel.send(f"{current_role.mention}\nИгрок {interaction.user.mention} хочет стать жителем города!")
