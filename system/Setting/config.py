import os


class Config:
	os.chdir(os.path.abspath('..'))
	os.chdir(os.path.abspath('..'))
	path = os.getcwd()
	labeled_path = os.path.join(path,'alldata/labeled/')
	unlabeled_path = os.path.join(path,'alldata/unlabeled/')
	model_path = os.path.join(path,'system/Model/')
	
if __name__ == '__main__':
	config = Config()
	print(config.model_path)	
	