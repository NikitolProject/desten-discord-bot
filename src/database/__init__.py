import os

import bson

from src.database.models import INewUser


class Database:

    async def add_new_user(self, new_user: INewUser) -> bool:
        await self.__create_data_directory()

        with open(f"{os.getcwd()}/data/user.bson", "rb") as file:
            current_data = file.read()

        current_data = bson.loads(current_data)

        if current_data.get(str(new_user.id), False):
            return False

        current_data[new_user.id] = new_user.mention

        with open(f"{os.getcwd()}/data/user.bson", "wb") as file:
            file.write(bson.dumps(current_data))

        return True

    async def __create_data_directory(self) -> None:
        if "data" in os.listdir(os.getcwd()):
            return None
        
        os.mkdir(f"{os.getcwd()}/data")

        with open(f"{os.getcwd()}/data/user.bson", "wb") as file:
            file.write(bson.dumps({"-1": "null"}))
