import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_dataframe(df):
	buf = io.BytesIO()

	fig, ax = plt.subplots(nrows=1, ncols=1, figsize=[15, 8])
	ax.set_title('compra e venda')
	ax.set_xlabel("anos")
	ax.set_ylabel("usd")
	ax.plot(df)
	ax.axvline(df.index[50])
	for i in range(50, df.index.size, 150):
		ax.axvline(df.index[i], color="red")
	for j in range(0, df.index.size +1, 75):
		ax.axvline(df.index[j], color="green")

	fig.savefig(buf, format="png")
	return (buf)
