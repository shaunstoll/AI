import sys
import pandas as pd
import numpy as np
#import plot_db
import copy

alphas = (0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 0.58)

def lr(df) :
	data = df.to_numpy()
	age_mean = np.mean(data, axis=0)[0]
	age_stdev = np.std(data, axis=0)[0]
	weight_mean = np.mean(data, axis=0)[1]
	weight_stdev = np.std(data, axis=0)[1]
	n = len(data[:,0])
	outFrame = pd.DataFrame()
	outFrame["alpha"] = alphas
	iterations = [100]*9
	iterations.append(7)
	outFrame["iterations"] = iterations
	b_0 = []
	b_age = []
	b_weight = []

	for age, i in zip(data[:,0], range(n)):
		data[i, 0] = (age - age_mean) / age_stdev

	for weight, i in zip(data[:,1], range(n)):
		data[i, 1] = (weight - weight_mean) / weight_stdev


	for a in alphas :
		iterations = 0
		w = [0]*len(data[0])
		prevR = sys.maxsize
		r = 0

		while iterations < 100 and (a != 0.58 or iterations < 7):
			iterations += 1
			r = R(data, w)
			#if a == 0.58:
				#print(prevR - r)
			
			w = update(data, w, a, n)
			prevR = r

		b_0.append(w[-1])
		b_age.append(w[0])
		b_weight.append(w[1])
		#print(w)
		#plot_db.visualize_3d(df, lin_reg_weights=[w[-1],w[0],w[1]])

	outFrame["b_0"] = b_0
	outFrame["b_age"] = b_age
	outFrame["b_weight"] = b_weight
	outFrame.to_csv(output_filename, index=False, header=False)

def f(x, w) :
	f = w[-1]
	for i in range(len(w) - 1) :
		f += w[i]*x[i]

	return f


def R(data, w) :
	R = 0
	n = len(data[:,0])
	for x in data :
		R += (f(x, w) - x[-1]) * (f(x, w) - x[-1])

	return R / (2 * n)


def update(data, w, a, n) :
	tmp = copy.deepcopy(w)

	s = 0
	for i in range(n) :
		s += (f(data[i], tmp) - data[i, -1])

	w[-1] = w[-1] - a/n * s

	
	for j in range(len(w) - 1) :
		s = 0
		for i in range(n) :
			s += (f(data[i], tmp) - data[i, -1]) * data[i,j]

		w[j] = w[j] - a/n * s

	return w


def main ():
	if len(sys.argv)!= 3:
		print("usage: " + str(sys.argv[0]) + " <data2.csv> <result2.csv>")
		exit()

	data = pd.read_csv(sys.argv[1], header = None)
	global output_filename
	output_filename = sys.argv[2]

	lr(data)

if __name__ == "__main__":
	main()