from vkbottle import (
    Keyboard,
    KeyboardButtonColor,
    Text,
    DocMessagesUploader,
)
from vkbottle.bot import Message, BotLabeler
from config import bot_send
from other import update_BD


module_4_labeler = BotLabeler()


@module_4_labeler.message(payload={"cmd": "4 модуль"})
async def module_4(message: Message):
    await update_BD(message, "4 модуль")
    await message.answer("В разработке")
