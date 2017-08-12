import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

font = {'family': 'Times New Roman',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

def plot_data(data):
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.grid()
	for x,y in data:
		ax=plt.plot(x,y)
	plt.show()

def plot_model(X,y,model):
	plt.rcParams['figure.figsize'] = (12.0,12.0)
	fig=plt.figure()
	ax=fig.add_subplot(211)
	ax.grid()
	ax.plot(y,'-b')
	P=model.predict(X)
	ax.plot(P,'-g')
	#create legend
	handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in ['b','g']]
	labels= ["Original Data","Predicted Data"]
	ax.legend(handles, labels)

	ax1=fig.add_subplot(212)
	ax1.grid()
	e=[a-b for a,b in zip(P,y)]
	ax1.plot(e,'-r')
    #create legend
	handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in ['r']]
	labels= ["Prediction Error"]
	ax1.legend(handles, labels)
	plt.show()


def plot_hist(d,xlabel="Taxi Count",ylabel="Number of occurences",l=10,h=90):
	plt.rcParams['figure.figsize'] = (12.0,6.0)
	fig=plt.figure()
	ax=fig.add_subplot(111)
	N, bins, patches = ax.hist(d,100,ec='k')

	cmap = plt.get_cmap('jet')
	low = cmap(0.5)
	medium =cmap(0.25)
	high = cmap(0.8)
	
	for i in range(len(patches)):
		if i < l:
			patches[i].set_facecolor(low)
		elif i < h:
			patches[i].set_facecolor(medium)
		else:
			patches[i].set_facecolor(high)

	ax.set_xlabel(xlabel, fontdict=font)  
	ax.set_ylabel(ylabel, fontdict=font)
	ax.set_xticklabels([],fontdict=font)  
	ax.set_yticklabels([],fontdict=font)
	#ax = plt.subplot(111)  
	ax.spines["top"].set_visible(False)  
	ax.spines["right"].set_visible(False)

	#create legend
	handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in [low,medium, high]]
	labels= ["lowest %s bins "%(l,),"between %s and %s bins "%(l,h), "highest %s bins"%(h,)]
	ax.legend(handles, labels)

	plt.show()