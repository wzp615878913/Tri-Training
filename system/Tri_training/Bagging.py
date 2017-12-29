import numpy as np 


""" 以硬投票的方式集成三个已训练好的分类器 """

class  Bagging:
	""" 构造函数参数为一个含有三个分类器的列表 """
	def __init__(self, arg):
		self.M = arg  # 初始的三个分类器

	""" 预测函数 """
	def predict(self,T):
		x = T.drop(['id','type'],1)
		x_test = x.values
		y_1 = self.M[0].predict(x_test)
		y_2 = self.M[1].predict(x_test)
		y_3 = self.M[2].predict(x_test)
		y = np.array([y_1,y_2,y_3])
		y_pre = list(map(sum,zip(*y)))
		def f(x):
			if x>1:
				return 1
			else:
				return 0
		y_pre = list(map(f,y_pre))
		return np.array(y_pre)
