import pandas as pd
import numpy as np

label = pd.read_csv('./2015_data_new/onlyLabel.csv')
feature = pd.read_csv('./2015_data_new/feature.csv')
data = pd.merge(feature, label,left_on = 'id',right_on = 'uid',how = 'left')
data = data.drop('uid',axis = 'columns')
# print(data)
label_data_0 = data[data['type']==0]
label_data_1 = data[data['type']==1]
label_data = pd.concat([label_data_0,label_data_1])
# print(label_data)
# label_data.to_csv('./2015_data_new/label_data.csv',index = False)
unlabel_data = data[pd.isnull(data['type'])]
unlabel_data.to_csv('./2015_data_new/unlabel_data.csv',index = False)
# print(unlabel_data)