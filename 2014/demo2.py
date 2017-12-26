import pandas as pd

data = pd.read_csv('./2014_data/feature_bdi_epq.csv')

feature =  ['id','education','grade','department','gender','marriage','fathersta','mothersta','parentsMarriage','isRecommended','isArtStudent','isRecommendedByContest','fatherEducation','motherEducation','religion','brotherSisterCount','residence','politicalStatus']
feature_bdi = ['uid','BDIPoint']
feature_epq = ['uid','EPQPoint','EScale','PScale','NScale','LScale']
feature_fa = ['uid','FAPoint','FAMarriage','FAAttachmentRelation','FAFamilyFunction','FAChildhoodTrauma','FACopingStyle','FAPastExperience','FASocialSupport','FALifeMeaning','FALearningMotivation']

fa = pd.read_csv('./answer_fa_result.csv')
fa = fa.loc[:,feature_fa]

data = pd.merge(data,fa,left_on = 'id',right_on = 'uid',how = 'left',right_index=False)

na = data.isnull().any(axis = 1)

data = data[na.values == False]

data = data.drop('uid',axis = 1)
# print(data)
data.to_csv('./2014_data/feature_bdi_epq_fa.csv',index = False,encoding = 'utf-8')