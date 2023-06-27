from vkbottle import (
    Keyboard,
    KeyboardButtonColor,
    Text,
    DocMessagesUploader,
)
from vkbottle.bot import Message, BotLabeler
from config import bot_send
from other import update_BD


module_3_labeler = BotLabeler()


@module_3_labeler.message(payload={"cmd": "3 модуль"})
async def module_3(message: Message):
    await update_BD(message, "3 модуль")
    await message.answer("В разработке")
