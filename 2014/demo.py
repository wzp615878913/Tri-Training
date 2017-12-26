import pandas as pd

feature = ['id','education','grade','department','gender','marriage','fathersta','mothersta','parentsMarriage','isRecommended','isArtStudent','isRecommendedByContest','fatherEducation','motherEducation','religion','brotherSisterCount','residence','politicalStatus']
data = pd.read_csv('./student.csv')
data = data.loc[:,feature]
na = data.isnull().any(axis = 1)

data = data[na.values == False]
data = data.replace(to_replace = '男',value = 1)
data = data.replace(to_replace = '女',value = 0)
data.to_csv('./2014_data/feature.csv',index = False,encoding = 'utf-8')
# print(data)