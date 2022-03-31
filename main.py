from src.telegramBot import TelegramBot
from src.data.driveBot import DriveBot
from dotenv import dotenv_values
import pandas as pd
import numpy as np
import os


KEYS = dotenv_values(".env")
TOKEN = KEYS["API_KEY"]
# telegram_bot = TelegramBot(TOKEN=TOKEN)
# telegram_bot.start()

end = pd.to_datetime("today") - np.timedelta64(1, "D")
start = end - np.timedelta64(1,"Y")
drive_bot = DriveBot("yahoo")
print(drive_bot.get_data("BTC-USD", start, end).head())
