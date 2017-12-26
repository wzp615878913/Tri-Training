import numpy as np
from random import randrange
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.preprocessing import normalize

import matplotlib.pyplot as plt





def distanceNorm(Norm,D_value):
	# initialization
	

	# Norm for distance
	if Norm == '1':
		counter = np.absolute(D_value)
		counter = np.sum(counter)
	elif Norm == '2':
		counter = np.power(D_value,2)
		counter = np.sum(counter)
		counter = np.sqrt(counter)
	elif Norm == 'Infinity':
		counter = np.absolute(D_value)
		counter = np.max(counter)
	else:
		raise Exception('We will program this later......')

	return counter





def fit(features,labels,iter_ratio):
	# initialization
	(n_samples,n_features) = np.shape(features)
	distance = np.zeros((n_samples,n_samples))
	weight = np.zeros(n_features)


	if iter_ratio >= 0.5:
		# compute distance
		for index_i in range(n_samples):
			for index_j in range(index_i+1,n_samples):
				D_value = features[index_i] - features[index_j]
				distance[index_i,index_j] = distanceNorm('2',D_value)
		distance += distance.T
	else:
		pass;


	# start iteration
	for iter_num in range(int(iter_ratio*n_samples)):
		# print iter_num;
		# initialization
		nearHit = list()
		nearMiss = list()
		distance_sort = list()

		# random extract a sample
		index_i = randrange(0,n_samples,1)
		self_features = features[index_i]

		# search for nearHit and nearMiss
		if iter_ratio >= 0.5:
			distance[index_i,index_i] = np.max(distance[index_i])	# filter self-distance 
			for index in range(n_samples):
				distance_sort.append([distance[index_i,index],index,labels[index]])
		else:
			# compute distance respectively
			distance = np.zeros(n_samples)
			for index_j in range(n_samples):
				D_value = features[index_i] - features[index_j]
				distance[index_j] = distanceNorm('2',D_value)
			distance[index_i] = np.max(distance)		# filter self-distance 
			for index in range(n_samples):
				distance_sort.append([distance[index],index,labels[index]])
		distance_sort.sort(key = lambda x:x[0])
		for index in range(n_samples):
			if nearHit == [] and distance_sort[index][2] == labels[index_i]:
				# nearHit = distance_sort[index][1];
				nearHit = features[distance_sort[index][1]]
			elif nearMiss == [] and distance_sort[index][2] != labels[index_i]:
				# nearMiss = distance_sort[index][1]
				nearMiss = features[distance_sort[index][1]]
			elif nearHit != [] and nearMiss != []:
				break
			else:
				continue

		# update weight
		weight = weight - np.power(self_features - nearHit,2) + np.power(self_features - nearMiss,2)
	# print(weight/(iter_ratio*n_samples))
	return weight/(iter_ratio*n_samples)



def test():
	label_data = pd.read_csv('./data/label_data_normal.csv')
	label = label_data.loc[:,['pt']]
	features = label_data.iloc[:,1:-1]
	features = features.values
	labels = label.values
	# for x in range(1,10):
	weight = fit(features,labels,0.8)	# 特征权重
	Y_axis = list(label_data.columns)
	Y_axis = Y_axis[1:-1]
	df = pd.DataFrame(columns = ['features','weight'])
	df['features'] = Y_axis
	df['weight'] = weight
	df = df.sort_values(by = ['weight'])
	plt.figure()  
	df.plot(kind='barh', x='features', y='weight', legend=False, figsize=(6, 10))  
	plt.title('Feature Importance')  
	plt.xlabel('Feature weight')  
	plt.show()  
	
if __name__ == '__main__':	
	test()





