import sqlite3
import datetime
from config import bot_send


# обновление базы данных
async def update_BD(message, command):
    user = await bot_send.api.users.get(message.from_id)
    current_time = str(datetime.datetime.now())[:19]
    base = sqlite3.connect("database.db")
    cur = base.cursor()
    base.execute(
        "CREATE TABLE IF NOT EXISTS registration_data(id PRIMARY KEY, first_name TEXT, last_name TEXT, time_register TEXT, last_time TEXT, last_action TEXT, count INTEGER, active TEXT)"
    )
    base.commit()
    id = cur.execute(
        f"SELECT id FROM registration_data WHERE id={message.peer_id}"
    ).fetchone()
    if id is None:
        cur.execute(
            "INSERT INTO registration_data values(?,?,?,?,?,?,?,?)",
            (
                message.peer_id,
                user[0].first_name,
                user[0].last_name,
                current_time,
                current_time,
                command,
                1,
                "1",
            ),
        )
        base.commit()
    else:
        cur.execute(
            "UPDATE registration_data SET first_name==?, last_name==?, last_time==?, last_action==? WHERE id=?",
            (
                user[0].first_name,
                user[0].last_name,
                current_time,
                command,
                message.peer_id,
            ),
        )
        base.commit()
        count = int(
            cur.execute(
                f"SELECT count FROM registration_data WHERE id={message.peer_id}"
            ).fetchone()[0]
        )
        cur.execute(
            "UPDATE registration_data SET count==? WHERE id=?",
            (count + 1, message.peer_id),
        )
        base.commit()
    base.close()
