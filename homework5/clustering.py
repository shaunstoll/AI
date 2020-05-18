import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster

def main ():
	if len(sys.argv)!= 2:
		print("usage: " + str(sys.argv[0]) + " <trees.png>")
		exit()

	image = plt.imread(sys.argv[1])
	#plt.imshow(image)
	#plt.show()

	x,y,z = image.shape
	image_2d = image.reshape(x*y, z)

	kmeans = cluster.KMeans(n_clusters=5)
	kmeans.fit(image_2d)

	cluster_centers = kmeans.cluster_centers_
	cluster_labels = kmeans.labels_

	plt.imshow(cluster_centers[cluster_labels].reshape(x,y,z))
	plt.show()
	

if __name__ == "__main__":
	main()