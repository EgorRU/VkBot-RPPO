from vkbottle import (
    Keyboard,
    KeyboardButtonColor,
    Text,
    DocMessagesUploader,
)
from vkbottle.bot import Message, BotLabeler
from config import bot_send
from other import update_BD


module_8_labeler = BotLabeler()


@module_8_labeler.message(payload={"cmd": "8 модуль"})
async def module_8(message: Message):
    await update_BD(message, "8 модуль")
    await message.answer("В разработке")
