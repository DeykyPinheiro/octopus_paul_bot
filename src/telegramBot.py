import io
import requests
import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta
import datetime
from src.data.driveBot import DriveBot
from src.visualization.visualize import plot_dataframe



class TelegramBot:
	def __init__(self, TOKEN):
		self.url = f"https://api.telegram.org/bot{TOKEN}/"
		self.drive_bot = DriveBot("yahoo")
		self.end_ts = pd.to_datetime("today") - np.timedelta64(1, "D")
		self.start_ts = self.end_ts - np.timedelta64(1,"Y")


	def start(self):
		update_id = None
		while True:
			updates = self.get_message(update_id)
			messages = updates["result"]

			if messages:
				for message in messages:
					try:
						update_id = message["update_id"]
						chat_id = message["message"]["from"]["id"]
						message_text = message["message"]["text"]
						answer_bot = self.create_answer(message_text)
						self.send_answer(chat_id, answer_bot)
					except:
						pass

	def get_message(self, update_id):
		link_request = f"{self.url}getUpdates?timeout1000"
		if update_id:
			link_request = f"{self.url}getUpdates?timeout1000&offset={update_id + 1 }"
		result = requests.get(link_request)
		return result.json()

	def create_answer(self, message_text):
		if message_text in ["oi", "ola", "eae", "eai"]:
			return ("ola querido usuario")
		elif message_text in ["df"]:
			df = self.drive_bot.get_data("BTC-USD", self.start_ts, self.end_ts)
			return df.head(10)
		elif message_text in ["grafico"]: # preciso subir um grafico
			df = self.drive_bot.get_data("BTC-USD", self.start_ts, self.end_ts)
			return plot_dataframe(df)
		else:
			return ("não entendi, use uma resposta valida")

	def send_answer(self, chat_id, answer):
		if type(answer) == type(io.BytesIO()):
			answer.seek(0)
			requests.post(f"{self.url}sendPhoto?chat_id={chat_id}", files = dict(photo=answer))
			answer.close()
			return
		else:
			link_to_send = f"{self.url}sendMessage?chat_id={chat_id}&text={answer}"
			requests.post(link_to_send)
			return



