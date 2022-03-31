import pandas as pd
import numpy as np
from pandas_datareader import DataReader




class DriveBot:
	def __init__(self, data_source):
		self.data_source = data_source

	def get_data(self, ticker, start, end):
		df = pd.DataFrame(DataReader(ticker, self.data_source, start, end))
		return df
