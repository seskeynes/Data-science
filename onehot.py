#one - hot 应用
#从sklearn导入one-hot
from sklearn.preprocessing import OneHotEncoder

#handle_unkown 意味着忽略位置特征，转换为空
enc=OneHotEncoder(handle_unknown='ignore')

#一共四个数据，三个特征
X=[['Male',1],['Female',3],['Female',2]]

enc.fit(X)

enc.categories_

#将目标特征onehot下
enc.transform([['Female',1],['Male',4]]).toarray()

#给定特定的onehot矩阵，求出特征
enc.inverse_transform([[0,1,1,0,0],[0,0,0,1,0]])

#得到所有转换过的特征名称/列数
enc.get_feature_names(['gender','group'])

#drop掉每个特征的第一列
drop_enc=OneHotEncoder(drop='first').fit(X)

drop_enc.categories_

drop_enc.transform([['Female',1],['Male',2]]).toarray()


#每个特征如果只有两个分类，则会被删除第一个分类，分类是1个或者大于2的分类不会被删除
drop_binary_enc=OneHotEncoder(drop='if_binary').fit(X)
drop_binary_enc.transform([['Female',1],['Male',2]]).toarray()



#测试如果性别大于3种，后面分类有1个的情况
Y=[['Male',1],['Female',1],['unkonwn',2]]
enc.fit(Y)
drop_binary_enc_y=OneHotEncoder(drop='if_binary').fit(Y)
drop_binary_enc_y.transform([['Female',1],['Male',2]]).toarray()
