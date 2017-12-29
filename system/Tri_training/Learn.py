from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
import xgboost as xgb
import numpy as np
from bootstrapSample import Sample
from system.Setting.config import Config
from process import Process
from Bagging import Bagging


class Learn:

	def __init__(self):
		pass
	"""SVM算法"""
	def SVM(self,S):
		train = S
		y = train['type']
		x = train.drop(['id','type'],1)
		x_train = x.values
		y_train = y.values
		clt = svm.SVC(C=821,kernel='rbf',gamma=0.001,decision_function_shape='ovr')
		clt.fit(x_train,y_train.ravel())
		return clt

	""" 朴素贝叶斯算法 """
	def Naive_Bayes(self,S):
		train = S
		y = train['type']
		x = train.drop(['id','type'],1)
		x_train = x.values
		y_train = y.values.ravel()
		gnb = GaussianNB()
		clt = gnb.fit(x_train, y_train)
		return clt 
	""" 决策树算法 """
	def Tree(self,S):
		train = S
		y = train['type']
		x = train.drop(['id','type'],1)
		x_train = x.values
		y_train = y.values.ravel()
		clf = tree.DecisionTreeClassifier()
		clf = clf.fit(x_train, y_train)
		return clf

	""" XGBoost """
	# def XGBoost(self,S):
		# params = {  
  #       'min_child_weight': 10,  
  #       'eta': 0.02,  
  #       'colsample_bytree': 0.7,  
  #       'max_depth': 10,  
  #       'subsample': 0.7,  
  #       'alpha': 1,  
  #       'gamma': 1,  
  #       'silent': 1,  
  #       'verbose_eval': True,  
  #       'seed': 12  
  #   	}   
		# train = S
		# y = train['pt']  
  #   	X = train.drop(['pt', 'id'], 1)  
  #   	xgtrain = xgb.DMatrix(X, label=y)  
  #  		bst = xgb.train(params, xgtrain, num_boost_round=rounds)  
   		

	""" 准确率评估 """
	def Estimate(self,T,M):
		y = T['type']
		x = T.drop(['id','type'],1)
		x_test = x.values
		y_test = y.values	
		score = M.score(x_test,y_test)
		return score	
	""" 返回模型 """
	def genModel(self,i,L):
		switch = {
			0 : self.SVM(L),
			1 : self.Naive_Bayes(L),
			2 : self.Tree(L)
		}
		return switch.get(i)
	
if __name__ == '__main__':
	pro = Process()
	pro.read_labeled()
	L = pro.L
	T = pro.T
	learn = Learn()
	M = []
	for i in range(3):
		M.append(learn.genModel(i,L))
	bagging = Bagging(M)
	y_pre = bagging.predict(T)
	print(type(y_pre))
	






