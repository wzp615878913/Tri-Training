import pandas as pd

feature = ['id','education','grade','department','gender','marriage','fathersta','mothersta','parentsMarriage','isRecommended','isArtStudent','isRecommendedByContest','fatherEducation','motherEducation','religion','brotherSisterCount','residence','politicalStatus']

data = pd.read_csv('./2015_data/feature_bdi_epq.csv')


# na = data.isnull().any(axis = 1)

# data = data[na.values == False]

# data.to_csv('./2015_data/feature.csv',index = False,encoding = 'utf-8')

fa = pd.read_csv('./answer_fa_result.csv')
fa = fa.loc[:,['uid','FAPoint','FAMarriage','FAAttachmentRelation','FAFamilyFunction','FAChildhoodTrauma','FACopingStyle','FAPastExperience','FASocialSupport','FALifeMeaning','FALearningMotivation']]

data = pd.merge(data,fa,left_on = 'id',right_on = 'uid',how = 'left',right_index=False)

na = data.isnull().any(axis = 1)

data = data[na.values == False]

data = data.drop('uid',axis = 1)

# print(data)


data.to_csv('./2015_data/feature_bdi_epq_fa.csv',index = False,encoding = 'utf-8')