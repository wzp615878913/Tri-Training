import pandas as pd
import numpy as np
from sklearn import preprocessing
# 合并14，15年数据
# unlabel_data_14 = pd.read_csv('./data_new/unlabel_data_14.csv')
# unlabel_data_15 = pd.read_csv('./data_new/unlabel_data_15.csv')
# unlabel_data_14 = unlabel_data_14.drop(['type'],axis = 1)
# unlabel_data_15 = unlabel_data_15.drop(['type'],axis = 1)
# unlabel_data = pd.concat([unlabel_data_14,unlabel_data_15])

# # 变换education，grade，department

# unlabel_data = unlabel_data.replace({'education':{7:1,8:2,9:3}})
# unlabel_data = unlabel_data.replace({'grade':{6:1,7:2}})
# unlabel_data = unlabel_data.replace({'department':{4:2,10:3}})
# unlabel_data = unlabel_data.replace({'department':{11:4,12:5,17:6,18:7,20:8,21:9,22:10}})
# unlabel_data = unlabel_data.replace({'department':{23:11,24:12,25:13,28:14,29:15,30:16,31:17,32:18,39:19,40:20,41:21,43:22}})
# unlabel_data = unlabel_data.replace({'department':{44:23,46:24,47:25,48:26,62:27,67:28,68:29,84:30,86:31,126:32,127:33,180:34,182:35,901:36,902:37,903:38,904:39,906:40,907:41,1000:42}})
# unlabel_data = unlabel_data.replace({'department':{206:43,905:44,908:45,999:46}})
# unlabel_data.to_csv('./data_new/unlabel_data.csv',index = False)

# 合并14，15年数据
# label_data_14 = pd.read_csv('./data_new/label_data_14.csv')
# label_data_15 = pd.read_csv('./data_new/label_data_15.csv')
# label_data = pd.concat([label_data_14,label_data_15])

# 变换education，grade，department

# label_data = label_data.replace({'education':{7:1,8:2,9:3}})
# label_data = label_data.replace({'grade':{6:1,7:2}})
# label_data = label_data.replace({'department':{4:2,10:3}})
# label_data = label_data.replace({'department':{11:4,12:5,17:6,18:7,20:8,21:9,22:10}})
# label_data = label_data.replace({'department':{23:11,24:12,25:13,28:14,29:15,30:16,31:17,32:18,39:19,40:20,41:21,43:22}})
# label_data = label_data.replace({'department':{44:23,46:24,47:25,48:26,62:27,67:28,68:29,84:30,86:31,126:32,127:33,180:34,182:35,901:36,902:37,903:38,904:39,906:40,907:41,1000:42}})
# label_data = label_data.replace({'department':{206:43,905:44,908:45,999:46}})
# label_data.to_csv('./data_new/label_data.csv',index = False)

# 标准化处理
# label_data = pd.read_csv('./data_new/unlabel_data.csv')
# label_data.iloc[:,1:] = label_data.iloc[:,1:].astype(np.float64)
# label_data.iloc[:,1:] = label_data.iloc[:,1:].apply(preprocessing.scale)
# label_data.to_csv('./data_new/unlabel_data_scale.csv',index = False)
# print(label_data)
# 正则化处理
# label_data = pd.read_csv('./data/label_data.csv')
# print(label_data[label_data.pt == 1])
# print(label_data)
# label_data.iloc[:,1:-1] = label_data.iloc[:,1:-1].astype(np.float64)












