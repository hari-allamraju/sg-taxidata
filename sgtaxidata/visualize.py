import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot_data(data):
	ax=None
	for x,y in data:
		if ax:
			ax=plt.plot(x,y)
		else:
			plt.plot(x,y,axes=ax)
	plt.show()

def plot_model(X,y,model):
    plt.scatter(X, y,color='g')
    plt.plot(X, model.predict(X),color='g')

    plt.scatter(X, y, color='r')
    plt.show()


def plot_hist(d,xlabel,ylabel):
	N, bins, patches = plt.hist(d,100,ec='k')

	cmap = plt.get_cmap('jet')
	low = cmap(0.5)
	medium =cmap(0.25)
	high = cmap(0.8)
	l=len(patches)
	
	for i in range(l):
		if i < 20:
			patches[i].set_facecolor(low)
		elif i < 80:
			patches[i].set_facecolor(medium)
		else:
			patches[i].set_facecolor(high)

	plt.xlabel(xlabel, fontsize=16)  
	plt.ylabel(ylabel, fontsize=16)
	plt.xticks(fontsize=14)  
	plt.yticks(fontsize=14)
	ax = plt.subplot(111)  
	ax.spines["top"].set_visible(False)  
	ax.spines["right"].set_visible(False)

	#create legend
	handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in [low,medium, high]]
	labels= ["low","medium", "high"]
	plt.legend(handles, labels)

	plt.show()