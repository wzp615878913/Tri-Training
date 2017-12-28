import os


class Config:
	os.chdir(os.path.abspath('..'))
	os.chdir(os.path.abspath('..'))
	path = os.getcwd()
	labeled_path = os.path.join(path,'Alldata/labeled/')
	unlabeled_path = os.path.join(path,'Alldata/unlabeled/')
	
if __name__ == '__main__':
	config = Config()
	print(config.model_path)	
	