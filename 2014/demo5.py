import pandas as pd

# label_1_interview = pd.read_csv('./2014_data/label_1_interview.csv')
# label_1_preview = pd.read_csv('./2014_data/label_1_preview.csv')
# label_1_psycases = pd.read_csv('./2014_data/label_1_psycases.csv')
# label_1_crisis = pd.read_csv('./2014_data/label_1_crisis.csv')
# label_1_consult = pd.read_csv('./2014_data/label_1_consult.csv')



# lable_1 = pd.concat([label_1_interview,label_1_preview,label_1_psycases,label_1_crisis,label_1_consult])

# lable_1 = lable_1.drop_duplicates()

# lable_1.to_csv('./2014_data/label_1.csv',index = False)

# 去重

# label_1 = pd.read_csv('./2014_data/label_1.csv')
# label_0 = pd.read_csv('./2014_data/label_0.csv')
# uid_1 = label_1['uid'].values
# uid_0 = label_0['uid'].values

# uid_0_1 = [x for x in uid_0 if x in uid_1]
# print(uid_0_1)
# uid_0 = list(uid_0)
# ind = []
# for x in uid_0_1:
# 	ind.append(uid_0.index(x))
# label_0 = label_0.drop(ind,axis = 0)

# label_0.to_csv('./2014_data/label_0.csv',index = False)









