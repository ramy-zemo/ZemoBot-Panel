import requests
from config import DISCORD_TOKEN


def get_guild_name_by_id(guild_id: int) -> str:
    headers = {"Authorization": f"Bot {DISCORD_TOKEN}"}

    ini = requests.get(f"https://discord.com/api/v8/guilds/{guild_id}", headers=headers)

    data = ini.json()

    return data["name"] if "name" in data else ""


def get_username_by_id(user_id: int) -> str:
    headers = {"Authorization": f"Bot {DISCORD_TOKEN}"}

    ini = requests.get(f"https://discord.com/api/v8/users/{user_id}", headers=headers)

    data = ini.json()

    return data["username"] if "username" in data else ""
