from sql.general import conn_main, cur_main, decode_data, InvalidGuild


def get_all_admin_commands():
    cur_main.execute("SELECT COMMAND FROM ADMIN_COMMANDS;")

    return cur_main.fetchall()


def create_admin_command(command: str, parameters: str, description: str):
    sql = "INSERT INTO ADMIN_COMMANDS (COMMAND, PARAMETERS, DESCRIPTION) VALUES (%s, %s, %s);"
    val = (command, parameters, description)

    try:
        cur_main.execute(sql, val)
        conn_main.commit()
        return 0

    except Exception as e:
        return e


def delete_admin_command(command: str):
    sql = "DELETE FROM ADMIN_COMMANDS WHERE COMMAND=%s"
    val = (command,)

    cur_main.execute(sql, val)
    conn_main.commit()
