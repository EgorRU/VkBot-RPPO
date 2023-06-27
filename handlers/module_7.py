from vkbottle import (
    Keyboard,
    KeyboardButtonColor,
    Text,
    DocMessagesUploader,
)
from vkbottle.bot import Message, BotLabeler
from config import bot_send
from other import update_BD


module_7_labeler = BotLabeler()


@module_7_labeler.message(payload={"cmd": "7 модуль"})
async def module_7(message: Message):
    await update_BD(message, "7 модуль")
    await message.answer("В разработке")
