import discord

from discord.ext import commands

from src.database import Database, INewUser


class Bot(commands.Bot):

    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix=commands.when_mentioned_or('$'), 
            intents=intents
        )


bot = Bot()
database = Database()
