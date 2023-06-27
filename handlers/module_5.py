from vkbottle import (
    Keyboard,
    KeyboardButtonColor,
    Text,
    DocMessagesUploader,
)
from vkbottle.bot import Message, BotLabeler
from config import bot_send
from other import update_BD


module_5_labeler = BotLabeler()


@module_5_labeler.message(payload={"cmd": "5 модуль"})
async def module_5(message: Message):
    await update_BD(message, "5 модуль")
    await message.answer("В разработке")
