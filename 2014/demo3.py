import pandas as pd

# data = pd.read_csv('./preview.csv')

# data = data.loc[:,['uid','zd0']]

# data = data[data['zd0']==0]


# data = data.drop_duplicates()
# # print(data)

# data = data.replace(to_replace = 0,value = 1)
# # print(data)

# data.to_csv('./2014_data/label_1_preview.csv',index = False)

label_1 = pd.read_csv('./2014_data/label_1_preview.csv')
# label_0 = pd.read_csv('./2014_data/label_0_preview.csv')

# # uid_1 = label_1['uid'].values

# # uid_0 = label_0['uid'].values

# # uid_0_1 = [x for x in uid_0 if x in uid_1]
# # uid_0 = list(uid_0)
# # index = []
# # for x in uid_0_1:
# # 	index.append(uid_0.index(x))
# # label_0 = label_0.drop(index,axis = 0)
label_1.columns = ['uid','pt']
print(label_1)

# label_0.to_csv('./2014_data/label_0_preview.csv',index = False)
label_1.to_csv('./2014_data/label_1_preview.csv',index = False)






