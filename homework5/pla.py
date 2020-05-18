import sys
import pandas as pd
import numpy as np
#import plot_db

def perceptron(df):
	data = df.to_numpy()
	w = [0]*(np.size(data,1))
	global d 
	d = len(w) - 1
	label = np.size(data,1) - 1
	dif = 1
	wFrame = pd.DataFrame(columns=["weight_1", "weight_2", "b"])

	while dif != 0:
		#if w[0] != 0 and w[1] != 0 :
			#plot_db.visualize_scatter(df, weights=w)

		dif = 0
		for x in data :
			if x[label]*f(x, w) <= 0 :
				dif += 1
				w[-1] = w[-1] + x[label]
				for i in range(0,d) :
					w[i] = w[i] + x[label]*x[i]

		wFrame.loc[len(wFrame)] = w

	wFrame.to_csv(output_filename, index=False, header=False)

def f(x, w):
	f = w[-1]
	for i in range (0,d):
		f += w[i]*x[i]

	return f

def main ():
	if len(sys.argv)!= 3:
		print("usage: " + str(sys.argv[0]) + " <data1.csv> <result1.csv>")
		exit()

	data = pd.read_csv(sys.argv[1], header = None)
	global output_filename
	output_filename = sys.argv[2]

	perceptron(data)

if __name__ == "__main__":
	main()