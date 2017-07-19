import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)


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