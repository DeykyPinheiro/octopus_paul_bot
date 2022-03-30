from turtle import update
import requests


class TelegramBot:
	def __init__(self, TOKEN):
		self.url = f"https://api.telegram.org/bot{TOKEN}/"


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
		else:
			return ("não entendi, use uma resposta valida")

	def send_answer(self, chat_id, answer):
		link_to_send = f"{self.url}sendMessage?chat_id={chat_id}&text={answer}"
		requests.post(link_to_send)
		return


