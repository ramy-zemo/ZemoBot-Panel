from sql.general import conn_main, cur_main, decode_data, InvalidGuild
from discordapi.main import get_username_by_id, get_guild_name_by_id
import timeit


def xp_lvl(xp):
    if not xp:
        return 0

    level_person = 0
    increment = 100
    level = 0
    j = 1
    i = 100
    xp = int(xp)

    for x in range(100, 55000):
        level += 1
        if j == 10:
            j = 0
            increment += 100

        if i <= xp < i + increment:
            level_person = level

        i += increment
        j += 1

    return level_person


def get_top_user_ranking():
    cur_main.execute("SELECT (SELECT GUILD_ID FROM CONFIG WHERE ID=SERVER_ID), USER_ID, XP FROM LEVEL ORDER BY XP DESC LIMIT 4;")
    data = cur_main.fetchall()
    data = [(count + 1, get_username_by_id(x[1]), get_guild_name_by_id(x[0]), xp_lvl(x[2]), x[2]) for count, x in enumerate(data)]

    return data
