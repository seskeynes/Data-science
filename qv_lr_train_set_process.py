#处理样本集数据

#导入包
import numpy as np
import pandas as pd

#通过pandas读取txt文件
data=pd.read_csv('/Users/***/Documents/qv_train2.txt',sep='$',encoding='utf-8')
data

#删除无用信息
data.drop(['rowkey','cid'],axis=1,inplace=True)


#将处理好的数据输出
data.to_excel("/Users/keynesjin/Documents/LR_QV_train_set.xls", index=False)
