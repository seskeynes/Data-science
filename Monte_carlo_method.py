import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from scipy.stats import uniform
import seaborn as sns

#set_theme alias set multiple theme parameters in one step
sns.set()

#设定参数（模型变量）
#100000个点
n=100000

#圆半径
r=1.0

#圆心
o_x,o_y=(0.,0.)



#生成随机样本，满足条件(o_x-r,2*r)对应区间[o_x-r,(o_x-r)+2*r]内的点，生成随机样本n
uniform_x=uniform(o_x-r,2*r).rvs(n)
uniform_y=uniform(o_y-r,2*r).rvs(n)


#计算随机点和原点距离，距离采用了欧氏距离
d_array=np.sqrt((uniform_x-o_x)**2+(uniform_y-o_y)**2)


#计算落入圆的点数量
res=sum(np.where(d_array<r,1,0))



#根据上面公式得到预估pi

#直接计算pi方法一
pi_1=(res/n)*4

#直接计算pi方法二
pi_2=(res/n)/(r**2)*(2*r)**2




#将图形绘制出来

#画个矩形
fig,ax=plt.subplots(1,1)
ax.plot(uniform_x,uniform_y,'ro',markersize=0.1)

#调整轴距，使得横纵轴相等
plt.axis('equal')

#轴中加圆
circle=Circle(xy=(o_x,o_y),radius=r,alpha=0.5)
ax.add_patch(circle)

#显示图像
plt.show()


#打印pi_1计算值
print('pi_1={}'.format(pi_1))


#通过pi_1和pi_2的两个值相等确认两种计算方式无异
#打印pi_2计算值
print('pi_2={}'.format(pi_2))



