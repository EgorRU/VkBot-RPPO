from vkbottle import (
    Keyboard,
    KeyboardButtonColor,
    Text,
    DocMessagesUploader,
    OpenLink
)
from vkbottle.bot import Message, BotLabeler
from config import bot_send
from other import update_BD


module_1_labeler = BotLabeler()

#клавиатура
keyboard = Keyboard()
keyboard.add(
    Text("О модуле", {"cmd": "О модуле1"}), color=KeyboardButtonColor.PRIMARY
)
keyboard.add(Text("Лекции", {"cmd": "Лекции1"}), color=KeyboardButtonColor.PRIMARY)
keyboard.row()
keyboard.add(
    Text("Материал лаб. работ", {"cmd": "Материал лаб. работ1"}),
    color=KeyboardButtonColor.PRIMARY,
)
keyboard.add(
    Text("Материал сам. работ", {"cmd": "Материал сам. работ1"}),
    color=KeyboardButtonColor.PRIMARY,
)
keyboard.row()
keyboard.add(
    Text("Доп. материал", {"cmd": "Доп. материал1"}),
    color=KeyboardButtonColor.PRIMARY,
)
keyboard.add(
    Text("Аттестация", {"cmd": "Аттестация1"}), color=KeyboardButtonColor.PRIMARY
)
keyboard.row()
keyboard.add(
    Text("Файл со всеми материалами", {"cmd": "Файл со всеми материалами1"}),
    color=KeyboardButtonColor.NEGATIVE,
)
keyboard.row()
keyboard.add(
    Text("Расписание модуля", {"cmd": "Расписание модуля1"}),
    color=KeyboardButtonColor.PRIMARY,
)
keyboard.row()
keyboard.add(
    Text("Выбор модуля", {"cmd": "Курс"}), color=KeyboardButtonColor.POSITIVE
)
keyboard.add(Text("Меню", {"cmd": "Меню"}), color=KeyboardButtonColor.POSITIVE)


# 1 модуль
@module_1_labeler.message(payload={"cmd": "1 модуль"})
async def module_1(message: Message):
    await update_BD(message, "1 модуль")
    await message.answer("Модуль 1", keyboard=keyboard)


# Файл со всеми материалами
@module_1_labeler.message(payload={"cmd": "Файл со всеми материалами1"})
async def file_1(message: Message):
    await update_BD(message, "Файл со всеми материалами1")
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Основы программирования на Python.pdf",
        file_source="src/module_1/Основы программирования на Python.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)


#Расписание модуля
@module_1_labeler.message(payload={"cmd": "Расписание модуля1"})
async def file_1(message: Message):
    await update_BD(message, "Расписание модуля1")
    await message.answer('Расписание модуля')


# Назад в модуль
@module_1_labeler.message(payload={"cmd": "Назад в модуль 1"})
async def back_module_1(message: Message):
    await update_BD(message, "Назад в модуль 1")
    await message.answer("Модуль 1", keyboard=keyboard)



# О модуле
@module_1_labeler.message(payload={"cmd": "О модуле1"})
async def about_module_1(message: Message):
    await update_BD(message, "О модуле 1")
    await message.answer("О модуле")


# Клавиатура лекций
keyboard_lect_1 = Keyboard()
keyboard_lect_1.add(
    Text("Видео 1", {"cmd": "Видео 11"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.add(
    Text("Презент-я 1", {"cmd": "Презент-я 11"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.add(
    Text("Материал 1", {"cmd": "Материал 11"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.row()
keyboard_lect_1.add(
    Text("Видео 2", {"cmd": "Видео 12"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.add(
    Text("Презент-я 2", {"cmd": "Презент-я 12"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.add(
    Text("Материал 2", {"cmd": "Материал 12"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.row()
keyboard_lect_1.add(
    Text("Видео 3", {"cmd": "Видео 13"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.add(
    Text("Презент-я 3", {"cmd": "Презент-я 13"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.add(
    Text("Материал 3", {"cmd": "Материал 13"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.row()
keyboard_lect_1.add(
    Text("Видео 4", {"cmd": "Видео 14"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.add(
    Text("Презент-я 4", {"cmd": "Презент-я 14"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.add(
    Text("Материал 4", {"cmd": "Материал 14"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.row()
keyboard_lect_1.add(
    Text("Видео 5", {"cmd": "Видео 15"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.add(
    Text("Презент-я 5", {"cmd": "Презент-я 15"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.add(
    Text("Материал 5", {"cmd": "Материал 15"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lect_1.row()
keyboard_lect_1.add(
    Text("Назад", {"cmd": "Назад в модуль 1"}), color=KeyboardButtonColor.POSITIVE
)


# Основной раздел лекций
@module_1_labeler.message(payload={"cmd": "Лекции1"})
async def lect_1(message: Message):
    await update_BD(message, "Лекции1")
    await message.answer("Лекции", keyboard=keyboard_lect_1)


# 1 лекция
@module_1_labeler.message(payload={"cmd": "Видео 11"})
async def lect_11(message: Message):
    await message.answer("https://youtu.be/FK-sqG2mrlk", dont_parse_links=1)
    

# 2 лекция
@module_1_labeler.message(payload={"cmd": "Видео 12"})
async def lect_12(message: Message):
    await message.answer("https://youtu.be/1fJ3LFlWY3I", dont_parse_links=1)


# 3 лекция
@module_1_labeler.message(payload={"cmd": "Видео 13"})
async def lect_13(message: Message):
    await message.answer("https://youtu.be/eJRZwVaix9s", dont_parse_links=1)


# 4 лекция
@module_1_labeler.message(payload={"cmd": "Видео 14"})
async def lect_14(message: Message):
    await message.answer("https://youtu.be/GP0jUYaZBHs", dont_parse_links=1)
    

# 5 лекция
@module_1_labeler.message(payload={"cmd": "Видео 15"})
async def lect_15(message: Message):
    await message.answer("https://youtu.be/cQ7_4Lg99sw", dont_parse_links=1)
    

# 1 презентация
@module_1_labeler.message(payload={"cmd": "Презент-я 11"})
async def presentation_11(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Презентация - Говорим с компьютером на одном языке.pdf",
        file_source="src/module_1/Презентация - Говорим с компьютером на одном языке.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)


# 2 презентация
@module_1_labeler.message(payload={"cmd": "Презент-я 12"})
async def presentation_12(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Презентация - Открыть ящик ПИТОНА.pdf",
        file_source="src/module_1/Презентация - Открыть ящик ПИТОНА.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)


# 3 презентация
@module_1_labeler.message(payload={"cmd": "Презент-я 13"})
async def presentation_13(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Презентация - Когда нужно сделать выбор.pdf",
        file_source="src/module_1/Презентация - Когда нужно сделать выбор.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)
    

# 4 презентация
@module_1_labeler.message(payload={"cmd": "Презент-я 14"})
async def presentation_14(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Презентация - Ходить вокруг, а не около.pdf",
        file_source="src/module_1/Презентация - Ходить вокруг, а не около.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)
    

# 5 презентация
@module_1_labeler.message(payload={"cmd": "Презент-я 15"})
async def presentation_15(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Презентация - О простеньком боте замолвите слово.pdf",
        file_source="src/module_1/Презентация - О простеньком боте замолвите слово.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)
    

# 1 Материал
@module_1_labeler.message(payload={"cmd": "Материал 11"})
async def material_11(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Говорим с компьютером на одном языке.pdf",
        file_source="src/module_1/1.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)


# 2 Материал
@module_1_labeler.message(payload={"cmd": "Материал 12"})
async def material_12(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Открыть ящик ПИТОНА.pdf",
        file_source="src/module_1/2.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)


# 3 Материал
@module_1_labeler.message(payload={"cmd": "Материал 13"})
async def material_13(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Когда нужно сделать выбор.pdf",
        file_source="src/module_1/3.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)


# 4 Материал
@module_1_labeler.message(payload={"cmd": "Материал 14"})
async def material_14(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Ходить вокруг, а не около.pdf",
        file_source="src/module_1/4.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)


# 5 Материал
@module_1_labeler.message(payload={"cmd": "Материал 15"})
async def material_15(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="О простеньком боте замолвите слово.pdf",
        file_source="src/module_1/5.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)


# Клавиатура лабораторных работ
keyboard_lab_1 = Keyboard()
keyboard_lab_1.add(
    Text("Лаб работа 1", {"cmd": "Лаб. работа 11"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lab_1.add(
    Text("Доп. материал к работе 1", {"cmd": "Доп. материал к работе 11"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lab_1.row()
keyboard_lab_1.add(
    Text("Лаб работа 2", {"cmd": "Лаб. работа 12"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lab_1.add(
    Text("Доп. материал к работе 2", {"cmd": "Доп. материал к работе 12"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lab_1.row()
keyboard_lab_1.add(
    Text("Лаб работа 3", {"cmd": "Лаб. работа 13"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lab_1.add(
    Text("Доп. материал к работе 3", {"cmd": "Доп. материал к работе 13"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_lab_1.row()
keyboard_lab_1.add(
    Text("Назад", {"cmd": "Назад в модуль 1"}), color=KeyboardButtonColor.POSITIVE
)


# Основной раздел лабораторных работ
@module_1_labeler.message(payload={"cmd": "Материал лаб. работ1"})
async def lab_1(message: Message):
    await update_BD(message, "Материалы лаб1")
    await message.answer("Лабораторые работы", keyboard=keyboard_lab_1)


# 1 лаба
@module_1_labeler.message(payload={"cmd": "Лаб. работа 11"})
async def lab_11(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Лабораторная работа 1 1М.pdf",
        file_source="src/module_1/Лабораторная работа 1 1М.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)
   


# доп 1 лаба
@module_1_labeler.message(payload={"cmd": "Доп. материал к работе 11"})
async def lab_11_dop(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Доп. материал к работе 1 1М.pdf",
        file_source="src/module_1/Доп. материал к работе 1 1М.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)


# 2 лаба
@module_1_labeler.message(payload={"cmd": "Лаб. работа 12"})
async def lab_12(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Лабораторная работа 2 1М.pdf",
        file_source="src/module_1/Лабораторная работа 2 1М.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)
   


# доп 2 лаба
@module_1_labeler.message(payload={"cmd": "Доп. материал к работе 12"})
async def lab_12_dop(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Доп. материал к работе 2 1М.pdf",
        file_source="src/module_1/Доп. материал к работе 2 1М.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)


# 3 лаба
@module_1_labeler.message(payload={"cmd": "Лаб. работа 13"})
async def lab_13(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Лабораторная работа 3 1М.pdf",
        file_source="src/module_1/Лабораторная работа 3 1М.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)
   


# доп 3 лаба
@module_1_labeler.message(payload={"cmd": "Доп. материал к работе 13"})
async def lab_13_dop(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Доп. материал к работе 3 1М.pdf",
        file_source="src/module_1/Доп. материал к работе 3 1М.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)
   

# Клавиатура самостоятельных работ
keyboard_by_himself_1 = Keyboard()
keyboard_by_himself_1.add(
    Text("Графика в Python", {"cmd": "Графика в Python"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_by_himself_1.row()
keyboard_by_himself_1.add(
    Text("Работа с файлами", {"cmd": "Работа с файлами1"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_by_himself_1.row()
keyboard_by_himself_1.add(
    Text("Яндекс.Контест", {"cmd": "Яндекс.Контест1"}), color=KeyboardButtonColor.PRIMARY
)
keyboard_by_himself_1.row()
keyboard_by_himself_1.add(
    Text("Назад", {"cmd": "Назад в модуль 1"}), color=KeyboardButtonColor.POSITIVE
)


# Основной раздел самостоятельных работ
@module_1_labeler.message(payload={"cmd": "Материал сам. работ1"})
async def by_himself_material(message: Message):
    await update_BD(message, "Материал сам. работ1")
    await message.answer("Раздел самостоятельного материала", keyboard=keyboard_by_himself_1)


# Элементарная графика в Python
@module_1_labeler.message(payload={"cmd": "Графика в Python"})
async def by_himself_11(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document1 = await doc_upd.upload(
        title="logo.py",
        file_source="src/module_1/logo.py",
        peer_id=message.peer_id,
    )
    document2 = await doc_upd.upload(
        title="logo.jpg",
        file_source="src/module_1/logo.jpg",
        peer_id=message.peer_id,
    )
    await message.answer("Элементарная графика в Python: https://youtu.be/ibWo576pW5M", dont_parse_links=1)
    await message.answer(attachment=document1)
    await message.answer(attachment=document2)


# Работа с файлами
@module_1_labeler.message(payload={"cmd": "Работа с файлами1"})
async def by_himself_12(message: Message):
    await message.answer("Работа с файлами: https://youtu.be/GDqFig4IM7U", dont_parse_links=1)


# Яндекс.Контест
@module_1_labeler.message(payload={"cmd": "Яндекс.Контест1"})
async def by_himself_13(message: Message):
    keyboard = Keyboard()
    keyboard.add(OpenLink("https://official.contest.yandex.ru/contest/41063/", "1 контест"))
    keyboard.row()
    keyboard.add(OpenLink("https://official.contest.yandex.ru/contest/41305/", "2 контест"))
    keyboard.row()
    keyboard.add(
        Text("Назад", {"cmd": "Материал сам. работ1"}), color=KeyboardButtonColor.POSITIVE
    )
    await message.answer("Раздел Яндекса Контеста - задачи для закрепления материала", keyboard=keyboard)


# Дополнительный материал
@module_1_labeler.message(payload={"cmd": "Доп. материал1"})
async def additional_material_11(message: Message):
    await update_BD(message, "Доп. материал1")
    keyboard = Keyboard()
    keyboard.add(
        Text("Установка Python", {"cmd": "Установка Python"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.row()
    keyboard.add(
        Text("Работа со строками", {"cmd": "Работа со строками"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.add(
        Text("Работа с файлами", {"cmd": "Работа с файлами2"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.row()
    keyboard.add(
        Text("Графика в консоли", {"cmd": "Графика в консоли"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.add(
        Text("Битовые операции", {"cmd": "Битовые операции"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.row()
    keyboard.add(
        Text("Встроенные функции", {"cmd": "Встроенные функции"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.add(
        Text("Самоучители", {"cmd": "Самоучители"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.row()
    keyboard.add(
        Text("Пользовательские функции", {"cmd": "Пользовательские функции"}), color=KeyboardButtonColor.PRIMARY
    )
    keyboard.row()
    keyboard.add(
        Text("Назад", {"cmd": "Назад в модуль 1"}), color=KeyboardButtonColor.POSITIVE
    )
    await message.answer("Раздел дополнительного материала", keyboard=keyboard)


# Тест
@module_1_labeler.message(payload={"cmd": "Аттестация1"})
async def test_1(message: Message):
    await update_BD(message, "Аттестация1")
    keyboard = Keyboard()
    keyboard.add(OpenLink("https://e.vyatsu.ru/mod/quiz/view.php?id=558716", "Аттестация"))
    keyboard.row()
    keyboard.add(OpenLink("https://e.vyatsu.ru/mod/feedback/view.php?id=558717", "Обратная связь"))
    keyboard.row()
    keyboard.add(
        Text("Назад", {"cmd": "Назад в модуль 1"}), color=KeyboardButtonColor.POSITIVE
    )
    await message.answer("Тест", keyboard=keyboard)