from sql.general import conn_main, cur_main, decode_data, InvalidGuild


def get_all_guild_ids():
    cur_main.execute("SELECT GUILD_ID FROM CONFIG")

    return cur_main.fetchall()


def get_active_guild_ids():
    cur_main.execute("SELECT GUILD_ID FROM CONFIG WHERE ACTIVE=1")

    return cur_main.fetchall()
