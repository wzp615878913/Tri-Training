import pandas as pd

# 分割0，1样本
data = pd.read_csv('./crisisintervention.csv')
data = data.loc[:,['uid']]
data = data.drop_duplicates()
data['pt'] = 1
data.to_csv('./2014_data/label_1_crisis.csv',index = False)

# label_0 = label_0.drop_duplicates()

# label_1 = label_1.drop_duplicates()
# label_0.columns = ['uid','pt']
# label_1.columns = ['uid','pt']

# label_0.to_csv('./2014_data/label_0_interview.csv',index = False)
# label_1.to_csv('./2014_data/label_1_interview.csv',index = False)

#  去重

# label_1 = pd.read_csv('./2014_data/label_1_interview.csv')
# label_0 = pd.read_csv('./2014_data/label_0_interview.csv')
# uid_1 = label_1['uid'].values
# uid_0 = label_0['uid'].values

# uid_0_1 = [x for x in uid_0 if x in uid_1]
# uid_0 = list(uid_0)
# ind = []
# for x in uid_0_1:
# 	ind.append(uid_0.index(x))
# label_0 = label_0.drop(ind,axis = 0)
# label_0.to_csv('./2014_data/label_0_interview.csv',index = False)

# 改标签

# label_1 = pd.read_csv('./2014_data/label_1_psycases.csv')
# label_0 = pd.read_csv('./2014_data/label_0_psycases.csv')

# label_0.columns = ['uid','pt']
# label_1.columns = ['uid','pt']

# label_0.to_csv('./2014_data/label_0_psycases.csv',index = False)
# label_1.to_csv('./2014_data/label_1_psycases.csv',index = False)















