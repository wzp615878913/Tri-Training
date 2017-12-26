import pandas as pd

import pandas as pd

# 分割0，1样本
data = pd.read_csv('./crisisintervention.csv')
data = data.loc[:,['uid']]
data['pt'] = 1
# print(data)
# _2 = data[data['suggestion']==2]
# _3 = data[data['suggestion']==3]
# _4 = data[data['suggestion']==4]

# _1 = data[data['suggestion']==1]
# _5 = data[data['suggestion']==5]

# label_1 = pd.concat([_2,_3,_4])
# label_0 = pd.concat([_1,_5])


# label_1 = label_1.replace(to_replace = [2,3,4],value = 1)
# label_0 = label_0.replace(to_replace = [1,5],value = 0)
# print(label_1)
# print(label_0)
# label_0 = label_0.drop_duplicates()
label_1 = data.drop_duplicates()
# label_0.columns = ['uid','pt']
# label_1.columns = ['uid','pt']
# print(label_1)

# label_0.to_csv('./2015_data/label_0_interview.csv',index = False)
label_1.to_csv('./2015_data/label_1_crisis.csv',index = False)

#  去重

# label_1 = pd.read_csv('./2015_data/label_1_interview.csv')
# label_0 = pd.read_csv('./2015_data/label_0_interview.csv')
# uid_1 = label_1['uid'].values
# uid_0 = label_0['uid'].values

# uid_0_1 = [x for x in uid_0 if x in uid_1]
# print(uid_0_1)
# uid_0 = list(uid_0)
# ind = []
# for x in uid_0_1:
# 	ind.append(uid_0.index(x))
# label_0 = label_0.drop(ind,axis = 0)
# label_0.to_csv('./2015_data/label_0_psycase.csv',index = False)
