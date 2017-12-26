import pandas as pd
import numpy as np
label = pd.read_csv('./2014_data/label.csv')
feature = pd.read_csv('./2014_data/feature.csv')

data = pd.merge(feature, label,left_on = 'id',right_on = 'uid',how = 'left')

data = data.drop('uid',axis = 'columns')

# label_data_0 = data[data['pt']==0]
# label_data_1 = data[data['pt']==1]
# label_data = pd.concat([label_data_0,label_data_1])

# label_data.to_csv('./2014_data/label_data.csv',index = False)
unlabel_data = data[pd.isnull(data['pt'])]

unlabel_data.to_csv('./2014_data/unlabel_data.csv',index = False)
