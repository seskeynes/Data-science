#!/usr/bin/env python
# coding: utf-8

# # 投资数学模型

#  - 通过数学这个工具建立模型去了解自己的投入模式，并且积累一些常用的数学模型，建立评估体系
#  - 积累模型思维，重要的是思想不是工具 anytime ！

# ## 固定收益投入产出比模型假设：

# 收益是一个固定值（预期值），投入成本是时间+本金，是一个随着时间波动的递减函数

# 本文：预期收益1w，投入7k，盈利预计3k，给出对应的函数


import numpy as np
import matplotlib.pyplot as plt


a=10000 #目标资产
b=7000 #投入成本

#数据标准化，标准量纲
a1=(a/(a+b))*365
b1=(b/(a+b))*365

x=np.arange(0,365,1)
y=(a1-b1)/(b1+x) #y越大价值越高


plt.title('Fixed assets input-output ratio')
plt.plot(x,y)




