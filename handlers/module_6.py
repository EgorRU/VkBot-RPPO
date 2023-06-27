from vkbottle import (
    Keyboard,
    KeyboardButtonColor,
    Text,
    DocMessagesUploader,
)
from vkbottle.bot import Message, BotLabeler
from config import bot_send
from other import update_BD


module_6_labeler = BotLabeler()


@module_6_labeler.message(payload={"cmd": "6 модуль"})
async def module_6(message: Message):
    await update_BD(message, "6 модуль")
    await message.answer("В разработке")
