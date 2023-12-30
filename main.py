import os

from src import bot, Confirm


@bot.event
async def on_ready() -> None:
    channel = await bot.fetch_channel("1190770933431017663")
    await channel.send(
        "Если Вы хотите вступить в город - нажмите на кнопку ниже!",
        view=Confirm()
    )


if __name__ == "__main__":
    bot.run(os.environ["BOT_TOKEN"])
