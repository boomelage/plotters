import pandas as pd
import matplotlib.pyplot as plt

def PlotCols(df,col_names=None,index=None,figsize=(10,15),exclusions=None):
	"""
	index parameter currently supports only pandas timestamps
	

	"""
	if index != None:
		df = df.set_index(index)
		df.index = pd.to_datetime(df.index)
	else:
		index = []
	if col_names == None:
		plotcols = df.columns.tolist()
	else:
		plotcols = col_names
	if exclusions == None:
		exclusions = []
	plotcols = [c for c in plotcols if c not in exclusions or c != index or c.find('date')!=-1]
	print(plotcols)
	fig,axs = plt.subplots(len(plotcols),figsize=figsize,sharex=True)
	for i,col in enumerate(plotcols):
		axs[i].plot(df[col],color='purple',label=col.replace('_',' '))
		axs[i].legend()
	plt.show()