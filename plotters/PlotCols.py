import pandas as pd
import matplotlib.pyplot as plt

def PlotCols(df,exclusions=None,index=None):
	"""
	index parameter currently supports only pandas timestamps
	

	"""
	if index != None:
		df = df.set_index(index)
		df.index = pd.to_datetime(df.index)
	else:
		index = []
	plotcols = df.columns.tolist()
	if exclusions == None:
		exclusions = []

	plotcols = [c for c in plotcols if c not in exclusions and c != index]

	fig,axs = plt.subplots(len(plotcols),figsize=figsize,sharex=True)


	for i,col in enumerate(plotcols):
		axs[i].plot(df[col],color='purple',label=col.replace('_',' '))
		axs[i].legend()
	plt.show()


from pathlib import Path
from model_settings import ms
ms.find_root(Path(__file__))
ms.collect_spx_calibrations()


exclusions = ['date']
index = 'calculation_date'
df = ms.spx_calibrations
figsize = (10,15)


PlotCols(df,index='calculation_date')