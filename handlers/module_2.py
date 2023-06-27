from vkbottle import (
    Keyboard,
    KeyboardButtonColor,
    Text,
    DocMessagesUploader,
)
from vkbottle.bot import Message, BotLabeler
from config import bot_send
from other import update_BD


module_2_labeler = BotLabeler()


@module_2_labeler.message(payload={"cmd": "2 модуль"})
async def module_2(message: Message):
    await update_BD(message, "2 модуль")
    await message.answer("В разработке")
