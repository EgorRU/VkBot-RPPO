from vkbottle import Bot
from config import token
from handlers import *
import asyncio


bot = Bot(token)

bot.labeler.load(admin_labeler)
bot.labeler.load(tutor_labeler)
bot.labeler.load(client_labeler)
bot.labeler.load(module_1_labeler)
bot.labeler.load(module_2_labeler)
bot.labeler.load(module_3_labeler)
bot.labeler.load(module_4_labeler)
bot.labeler.load(module_5_labeler)
bot.labeler.load(module_6_labeler)
bot.labeler.load(module_7_labeler)
bot.labeler.load(module_8_labeler)

if __name__=="__main__":
    asyncio.run(bot.run_polling())
