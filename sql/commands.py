from sql.general import conn_main, cur_main, decode_data, InvalidGuild


def get_all_commands():
    cur_main.execute("SELECT COMMAND FROM COMMANDS;")

    return cur_main.fetchall()


def get_all_commands_with_id():
    cur_main.execute("SELECT ID, COMMAND FROM COMMANDS;")
    try:
        return tuple([(x[0], x[1].capitalize()) for x in cur_main.fetchall()])
    except IndexError:
        return ()


def get_categories_with_command_count():
    cur_main.execute("SELECT CATEGORY_ID, COMMAND FROM COMMANDS;")
    data = cur_main.fetchall()
    dict_data = {}

    for entry in data:
        cur_main.execute("SELECT CATEGORY FROM COMMAND_CATEGORIES WHERE ID=%s;", (entry[0],))
        category = cur_main.fetchone()

        if category[0] + "_category" not in dict_data:
            dict_data[category[0] + "_category"] = 1
        else:
            dict_data[category[0] + "_category"] = dict_data[category[0] + "_category"] + 1

    cur_main.execute("SELECT COMMAND FROM ADMIN_COMMANDS;")
    dict_data["admin_commands"] = len(cur_main.fetchall())

    return dict_data


def create_command(category: str, command: str, parameters: str, description: str):
    sql = "INSERT INTO COMMANDS (CATEGORY_ID, COMMAND, PARAMETERS, DESCRIPTION) VALUES ((SELECT ID FROM COMMAND_CATEGORIES WHERE CATEGORY=%s), %s, %s, %s);"
    val = (category, command, parameters, description)
    try:
        cur_main.execute(sql, val)
        conn_main.commit()
        return 0
    except Exception as e:
        return e


def delete_command(command: str = "", command_id: int = 0):
    if command:
        sql = "DELETE FROM COMMANDS WHERE COMMAND=%s"
        val = (command,)
    elif command_id:
        sql = "DELETE FROM COMMANDS WHERE ID=%s"
        val = (command_id,)
    else:
        # TODO Create Error
        raise Exception

    cur_main.execute(sql, val)
    conn_main.commit()
