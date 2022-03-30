from src.telegramBot import TelegramBot
from dotenv import dotenv_values
import os

KEYS = dotenv_values(".env")
TOKEN = KEYS["API_KEY"]

bot = TelegramBot(TOKEN=TOKEN)
bot.start()
