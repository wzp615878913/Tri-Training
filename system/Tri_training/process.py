import numpy as np
import pandas as pd
from system.Setting.config import Config
# 预处理数据

class Process:
	def __init__(self):
		self.labeled_path = Config.labeled_path
		self.unlabeled_path = Config.unlabeled_path
		self.L = None # 初始已标记样本集
		self.T = None # 测试集
		self.U = None # 初始未标记样本集

	
	# 读取已标记数据并且分割训练集和测试集
	def read_labeled(self):
		label_data = pd.read_csv(self.labeled_path+'label_data_scale.csv')
		train = label_data.sample(n =800)
		self.L = train
		self.T = label_data.drop(train.index.values)

	# 读取未标记数据 
	def read_unlabeled(self):
		unlabel_data = pd.read_csv(self.unlabeled_path+'unlabel_data_scale.csv')
		self.U = unlabel_data

if __name__=='__main__':
	pro = Process()
	pro.read_labeled()
	pro.read_unlabeled()
	L = pro.L
	print(L)
	
	
	
	