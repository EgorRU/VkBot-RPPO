from vkbottle import Keyboard, KeyboardButtonColor, Text
from vkbottle.bot import Message, BotLabeler
from config import bot_send, ADMIN_API
import sqlite3


admin_labeler = BotLabeler()

# Панель админа
@admin_labeler.message(text="/info")
async def admin_panel(message: Message):
    if message.peer_id == ADMIN_API:
        await message.answer("Текст")
    else:
        await message.answer("Недостаточно прав")
       


# отправка рассылки
@admin_labeler.message(text="/student <item>")
async def mailing_list(message: Message, item: str):
    if message.peer_id == ADMIN_API:
        base = sqlite3.connect("database.db")
        cur = base.cursor()
        base.execute( "CREATE TABLE IF NOT EXISTS registration_data(id PRIMARY KEY, first_name TEXT, last_name TEXT, time_register TEXT, last_time TEXT, last_action TEXT, count INTEGER, active TEXT)")
        base.commit()
        data_user = cur.execute(f"SELECT id, active FROM registration_data").fetchall()
        for i in data_user:
            user = int(i[0])
            active = int(i[1])
            try:
                keyboard = Keyboard()
                keyboard.add(Text("Ресурсы ВятГУ", {"cmd": "Ресурсы ВятГУ"}),color=KeyboardButtonColor.NEGATIVE)
                keyboard.row()
                
                keyboard.add(Text("Цифровые кафедры", {"cmd": "Курс"}),color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
                
                keyboard.add(Text("Помощь с ботом", {"cmd": "Помощь с ботом"}),color=KeyboardButtonColor.PRIMARY)
                if active == 2:
                    keyboard.row()
                    keyboard.add(Text("Клавиатура тьютора", {"cmd": "Клавиатура тьютора"}),color=KeyboardButtonColor.NEGATIVE)
                await bot_send.api.messages.send(peer_id=user, message=item, random_id=0, keyboard=keyboard)
            except:
                cur.execute("UPDATE registration_data SET active==? WHERE id=?", (0, user))
                base.commit()
        await message.answer("Рассылка успешно отправлена")
        base.close()
    else:
        await message.answer("Недостаточно прав")