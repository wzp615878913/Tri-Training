from process import Process
import pandas as pd

class Sample:
	"""自助法抽样生成初始训练集"""
	def __init__(self):
		self.S = []
	def bootstrapSample(self,dataSet):	
		S = dataSet.sample(n=800,replace = True)
		return S 

	def gen_Train_Set(self,L):
		for i in range(3):
			self.S.append(self.bootstrapSample(L))

if __name__ == "__main__":
	sample = Sample()
	sample.gen_Train_Set()
	train = sample.S[0]
	print(train[train.type == 0])
