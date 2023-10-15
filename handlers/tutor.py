from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink, DocMessagesUploader
from vkbottle.bot import Message, BotLabeler
from config import bot_send
from other import update_BD


tutor_labeler = BotLabeler()

# основной раздел тьютора
@tutor_labeler.message(payload={"cmd": "Клавиатура тьютора"})
async def keyboard_tutor(message: Message):
    await update_BD(message, "Клавиатура тьютора")
    
    keyboard_tutor = Keyboard()
    keyboard_tutor.add(OpenLink( "https://docs.google.com/spreadsheets/d/1VoLwNVuGzpxd3Pd67T77tj_VNnaGHfY5pm2ABtd0eHA/edit", "Сводная таблица",))
    keyboard_tutor.row()
    
    keyboard_tutor.add(Text("Логи", {"cmd": "Логи"}), color=KeyboardButtonColor.POSITIVE)
    keyboard_tutor.row()
    
    keyboard_tutor.add(Text("Распред. тьюторов по группам", {"cmd": "Распред. тьюторов по группам"}),color=KeyboardButtonColor.POSITIVE)
    keyboard_tutor.row()
    
    keyboard_tutor.add(Text("Меню", {"cmd": "Меню"}), color=KeyboardButtonColor.POSITIVE)
    await message.answer("Клавиатура тьютора", keyboard=keyboard_tutor)


# Распред. тьюторов по группам
@tutor_labeler.message(payload={"cmd": "Распред. тьюторов по группам"})
async def group_tutor(message: Message):
    doc_upd = DocMessagesUploader(bot_send.api)
    document = await doc_upd.upload(
        title="Группы тьюторов.pdf",
        file_source="src/tutor/Группы тьюторов.pdf",
        peer_id=message.peer_id,
    )
    await message.answer(attachment=document)


# Логи по модулям
@tutor_labeler.message(payload={"cmd": "Логи"})
async def logs(message: Message):
    await message.answer("Текст",dont_parse_links=1)
