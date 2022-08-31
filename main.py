import sqlite3

def start_command(message):
    connect = sqlite3.connect('qwe.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
    )""")

    connect.commit()

    people_id = message.chat.id

    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        # add values in fields
        user_id = [message.chat.id]
        cursor.execute(f"INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()
    else:
        bot.send_message(message.chat.id, "Такой пользователь уже есть")