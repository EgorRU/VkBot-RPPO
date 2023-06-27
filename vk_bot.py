from vkbottle import Bot
from config import api, labeler
from handlers import *
import asyncio


labeler.load(admin_labeler)
labeler.load(tutor_labeler)
labeler.load(client_labeler)
labeler.load(module_1_labeler)
labeler.load(module_2_labeler)
labeler.load(module_3_labeler)
labeler.load(module_4_labeler)
labeler.load(module_5_labeler)
labeler.load(module_6_labeler)
labeler.load(module_7_labeler)
labeler.load(module_8_labeler)

bot = Bot(
    api=api,
    labeler=labeler,
)

asyncio.run(bot.run_polling())
