import os

from src import bot, Confirm


@bot.event
async def on_ready() -> None:
    channel = await bot.fetch_channel("1190770933431017663")
    await channel.purge(limit=100)
    await channel.send(
        "Если Вы хотите вступить в город - нажмите на кнопку ниже!",
        view=Confirm()
    )


if __name__ == "__main__":
    bot.run("MTE5MDc0Mzk4MDYyNzk5MjY1Ng.G5zgCj.RnBuF2hNrjSbhgWVJ5pcdO7b4490xtxMJgEcrw")
