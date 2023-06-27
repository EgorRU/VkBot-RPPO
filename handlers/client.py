from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink
from vkbottle.bot import Message, BotLabeler
from other import update_BD
import sqlite3


client_labeler = BotLabeler()


# старт
@client_labeler.message(text="Начать")
@client_labeler.message(payload={"cmd": "Меню"})
async def main(message: Message):
    await update_BD(message, "/start")
    base = sqlite3.connect("database.db")
    cur = base.cursor()
    base.execute(
        "CREATE TABLE IF NOT EXISTS registration_data(id PRIMARY KEY, first_name TEXT, last_name TEXT, time_register TEXT, last_time TEXT, last_action TEXT, count INTEGER, active TEXT)"
    )
    base.commit()
    active = int(
        cur.execute(
            f"SELECT active FROM registration_data WHERE id={message.peer_id}"
        ).fetchone()[0]
    )
    base.close()
    keyboard = Keyboard()
    keyboard.add(
        Text("Ресурсы ВятГУ", {"cmd": "Ресурсы ВятГУ"}),
        color=KeyboardButtonColor.PRIMARY,
    )
    keyboard.row()
    keyboard.add(
        Text("Цифровые кафедры", {"cmd": "Курс"}), color=KeyboardButtonColor.POSITIVE
    )
    keyboard.row()
    keyboard.add(
        Text("Помощь с ботом", {"cmd": "Помощь с ботом"}),
        color=KeyboardButtonColor.PRIMARY,
    )
    if active == 2:
        keyboard.row()
        keyboard.add(
            Text("Клавиатура тьютора", {"cmd": "Клавиатура тьютора"}),
            color=KeyboardButtonColor.NEGATIVE,
        )
    await message.answer("Основной раздел", keyboard=keyboard)


# ресурсы вятгу
@client_labeler.message(payload={"cmd": "Ресурсы ВятГУ"})
async def source_vyatsu(message: Message):
    await update_BD(message, "Ресурсы ВятГУ")
    keyboard = Keyboard()
    keyboard.add(OpenLink("https://www.vyatsu.ru/", "Сайт ВятГУ"))
    keyboard.add(OpenLink("https://new.vyatsu.ru/account/", "Личный кабинет"))
    keyboard.row()
    keyboard.add(OpenLink("https://e.vyatsu.ru/", "Moodle"))
    keyboard.add(OpenLink("https://lib.vyatsu.ru/", "Библиотека"))
    keyboard.row()
    keyboard.add(OpenLink("https://vk.com/vyatsu", "Вконтакте"))
    keyboard.add(OpenLink("https://t.me/vyatsunews", "Telegram"))
    keyboard.row()
    keyboard.add(Text("Меню", {"cmd": "Меню"}), color=KeyboardButtonColor.POSITIVE)
    await message.answer("Ресурсы ВятГУ", keyboard=keyboard)


# помощь с ботом
@client_labeler.message(payload={"cmd": "Помощь с ботом"})
async def help_with_bot(message: Message):
    await update_BD(message, "Помощь с ботом")
    await message.answer(
        'Основная информация:\n\nℹ️ Чтобы обновить клавиатуру, напишите Начать\n\nℹ️ С помощью бота Вы всегда можете получить электронные версии материалов.\n\nℹ️ Вопросы по поводу ошибок писать сюда:\nTelegram: @advanced_default_user\nVk: vk.com/advanced_default_user",'
    )


# Курс
@client_labeler.message(payload={"cmd": "Курс"})
async def source_vyatsu(message: Message):
    await update_BD(message, "Курс")
    keyboard = Keyboard()
    keyboard.add(
        Text("1 модуль", {"cmd": "1 модуль"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.add(
        Text("2 модуль", {"cmd": "2 модуль"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.add(
        Text("3 модуль", {"cmd": "3 модуль"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.add(
        Text("4 модуль", {"cmd": "4 модуль"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.row()
    keyboard.add(
        Text("5 модуль", {"cmd": "5 модуль"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.add(
        Text("6 модуль", {"cmd": "6 модуль"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.add(
        Text("7 модуль", {"cmd": "7 модуль"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.add(
        Text("8 модуль", {"cmd": "8 модуль"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.row()
    keyboard.add(Text("Меню", {"cmd": "Меню"}), color=KeyboardButtonColor.POSITIVE)
    await message.answer(
        "1 модуль - основы программирования на Python", keyboard=keyboard
    )
