import pandas as pd
import numpy as np
# label_1 = pd.read_csv('./2015_data/label_1.csv')
# label_0 = pd.read_csv('./2015_data/label_0.csv')
# label = pd.concat([label_0,label_1])
# print(label)
# label.to_csv('./2015_data/label.csv',index = False)
feature = pd.read_csv('./2015_data/feature.csv')
label = pd.read_csv('./2015_data/label.csv')
data = pd.merge(feature, label,left_on = 'id',right_on = 'uid',how = 'left')

data = data.drop('uid',axis = 'columns')
# print(data)

# label_data_0 = data[data['pt']==0]
# label_data_1 = data[data['pt']==1]
# label_data = pd.concat([label_data_0,label_data_1])
# print(label_data)

# label_data.to_csv('./2015_data/label_data.csv',index = False)
unlabel_data = data[pd.isnull(data['pt'])]
# print(unlabel_data)
unlabel_data.to_csv('./2015_data/unlabel_data.csv',index = False)