from process import Process
from Learn import Learn
import pandas as pd
import math
from bootstrapSample import Sample
from system.Estimate.Accuracy import estimate


class Tri_training:
	"""三体训练法"""
	def __init__(self):
		self.L = None  # 原始已标记样本集
		self.U = None  # 初始未标记样本集
		self.M = []  # 初始三个分类器
		self.T = None  # 测试集
		self.S = None  # 初始三个训练集
		self.Learn = None
		self.e = [0.5,0.5,0.5]
		self.l_1 = [0,0,0]
		self.Ln = []	
		self.Update = [] 
		self.E = [] 
		self.Estimate = estimate() # 评估器

	""" 准备数据 """
	def pre_data(self):
		pro = Process()
		pro.read_labeled()
		pro.read_unlabeled()
		unlabel = pro.U.sample(n = 3500)
		sample = Sample()
		sample.gen_Train_Set(pro.L)
		self.S = sample.S
		self.L = pro.L
		self.U = unlabel
		self.T = pro.T
		learn = Learn()
		self.Learn = learn
		for i in range(3):
			self.M.append(learn.genModel(2,self.S[i]))

	""" 估计从两个分类器的组合中导出的假设的分类错误率 """
	def MeasureError(self,H_j,H_k):
		count = 0
		err = 0
		labeled = self.L.values
		L_x = labeled[:,1:-1]
		L_y = labeled[:,-1]
		pre_j = H_j.predict(L_x)
		pre_k = H_k.predict(L_x)
		j_eq_k = pre_j == pre_k
		count = len([x for x in j_eq_k if x == True])
		for x in range(len(labeled)):
			if j_eq_k[x] and pre_j[x]!=L_y[x]:
				err+=1
		err = err / count
		return err

	""" 随机移除指定数目的样本 """
	def Subsample(self,L_t,s):
		n = L_t.shape[0] - s
		for i in range(n):
			sample = L_t.sample(n=1)
			L_t.drop(sample.index.values,inplace = True)

	""" 训练过程 """
	def Training(self):
		print(self.Estimate.Score(M = self.M,T = self.T))
		change = True
		n = 0
		while change:
			change =False
			count = [0,0,0]
			n += 1
			Train = [None,None,None]
			for i in range(3):
				self.Ln.append(pd.DataFrame())
				self.Update.append(False)
				M_jk = [self.M[x] for x in range(3) if x != i]
				self.E.append(self.MeasureError(M_jk[0],M_jk[1]))
				if self.E[i] < self.e[i]:
					iters = self.U.iterrows()
					for row in iters:
						row_x = row[1].values
						pre_j = M_jk[0].predict(row_x[1:].reshape(1,-1))
						pre_k = M_jk[1].predict(row_x[1:].reshape(1,-1))
						if pre_j == pre_k:
							x = row[1].to_frame().transpose()
							x['type'] = pre_j
							self.Ln[i] = self.Ln[i].append(x,ignore_index = True)
							count[i]+=1
					if self.l_1[i] == 0:
						item = (self.E[i]/(self.e[i]-self.E[i]))+1
						self.l_1[i] = math.floor(item)
					if self.l_1[i] < count[i]:
						if self.E[i]*count[i] < self.e[i]*self.l_1[i]:
							self.Update[i] = True
						elif self.l_1[i] > self.E[i]/(self.e[i]-self.E[i]):
							s = (self.e[i]*self.l_1[i])/self.E[i] - 1
							s = math.ceil(s)					
							self.Subsample(self.Ln[i], s)
							count[i]=s
							self.Update[i] = True				
			for i in range(3):
				if self.Update[i] == True:
					change = True
					Train[i] = pd.concat([self.L,self.Ln[i]],ignore_index = True)
					self.M[i] = self.Learn.genModel(2,Train[i])
					self.e[i] = self.E[i]
					self.l_1[i] = count[i]
			self.Update = []
			self.Ln = []
			self.E = []
			print('第{0}次循环'.format(n))
			print(self.Estimate.Score(M = self.M,T = self.T))

if __name__ == "__main__":
	tri = Tri_training()
	tri.pre_data()
	tri.Training()


