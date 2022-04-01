from src.telegramBot import TelegramBot
from src.data.driveBot import DriveBot
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os

load_dotenv()
TOKEN = os.getenv("API_KEY")

telegram_bot = TelegramBot(TOKEN)
telegram_bot.start()
