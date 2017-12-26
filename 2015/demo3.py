import pandas as pd

# label_0_interview = pd.read_csv('./2015_data/label_0_interview.csv')
# label_0_preview = pd.read_csv('./2015_data/label_0_preview.csv')
# label_0_psycases = pd.read_csv('./2015_data/label_0_psycase.csv')



# lable_0 = pd.concat([label_0_interview,label_0_preview,label_0_psycases])

# lable_0 = lable_0.drop_duplicates()
# print(lable_0)

# lable_0.to_csv('./2015_data/label_0.csv',index = False)

# 去重

label_1 = pd.read_csv('./2015_data/label_1.csv')
label_0 = pd.read_csv('./2015_data/label_0.csv')
uid_1 = label_1['uid'].values
uid_0 = label_0['uid'].values

uid_0_1 = [x for x in uid_0 if x in uid_1]
# print(uid_0_1)
uid_0 = list(uid_0)
ind = []
for x in uid_0_1:
	ind.append(uid_0.index(x))
label_0 = label_0.drop(ind,axis = 0)
# print(label_0)
label_0.to_csv('./2015_data/label_0.csv',index = False)
