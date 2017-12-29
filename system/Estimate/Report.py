import pandas as pd 
from sklearn.metrics import classification_report

class  estimate:

	"""准确率评估"""
	def Score(self,M,T):
		score = []
		y = T['type']
		x = T.drop(['id','type'],1)
		x_test = x.values
		y_test = y.values
		for i in range(3):
			score.append(M[i].score(x_test,y_test))
		return score

	""" 对三个分类器做评估报告 """
	def class_report(self,M,T):
		y_true = T['type']
		x = T.drop(['id','type'],1)
		x_test = x.values
		target = ['class 0','class 1']
		for i in range(3):
			y_pred = M[i].predict(x_test)
			report = classification_report(y_true, y_pred,target_names = target)
			print("分类器{0}的性能报告：\n {1}".format(i,report))

	""" 对通过Bagging集成的分类器做评估报告 """
	def bagging_report(self,M,T):
		y_true = T['type']
		target = ['class 0','class 1']
		y_pred = M.predict(T)
		report = classification_report(y_true,y_pred,target_names = target)
		print("三个分类器集成后的性能报告：\n {0}".format(report))
		
