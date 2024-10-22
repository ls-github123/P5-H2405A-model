## 1. Jupyter Notebook介绍

Jupyter项目是一个非盈利的开源项目，源于2014年的ipython项目，并逐渐发展为支持跨所有编程语言的交互式数据科学计算的工具。

- Jupyter Notebook，原名IPython Notbook，是IPython的加强网页版，一个开源Web应用程序
- 名字源自Julia、Python 和 R（数据科学的三种开源语言）
- 是一款程序员和科学工作者的**编程/文档/笔记/展示**软件
- **.ipynb**文件格式是用于计算型叙述的**JSON文档格式**的正式规范

安装

~~~
pip3 install jupyter
~~~

~~~
# 输入命令
jupyter notebook
~~~

## 2.什么是Matplotlib

- 专门用于开发2D图表(包括3D图表)

- 使用起来及其简单

- 以渐进、交互式方式实现数据可视化

可视化是在整个数据挖掘的关键辅助工具，可以清晰的理解数据，从而调整我们的分析方法。

- 能将数据进行可视化,更直观的呈现
- 使数据更加客观、更具说服力

案例：

折线图

~~~
import matplotlib.pyplot as plt
# 1）创建画布(容器层)
plt.figure()
# 2）绘制折线图(图像层)
plt.plot([1, 2, 3, 4, 5, 6 ,7], [17, 17, 18, 15, 11, 11, 13])
# 3）显示图像
plt.show()
~~~

散点图

~~~
# 1）准备数据
#房屋面积
x = [225.98, 247.07, 253.14, 457.85, 241.58, 301.01,  20.67, 288.64,
       163.56, 120.06, 207.83, 342.75, 147.9 ,  53.06, 224.72,  29.51,
        21.61, 483.21, 245.25, 399.25, 343.35]
#房屋价格
y = [196.63, 203.88, 210.75, 372.74, 202.41, 247.61,  24.9 , 239.34,
       140.32, 104.15, 176.84, 288.23, 128.79,  49.64, 191.74,  33.1 ,
        30.74, 400.02, 205.35, 330.64, 283.45]

# 2）创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 3）绘制散点图
plt.scatter(x, y)

# 4）显示图像
plt.show()
~~~

柱状图

~~~
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Arial Unicode MS"] ## mac
plt.rcParams['font.family']=['Arial Unicode MS'] ## mac
#mpl.rcParams["font.sans-serif"] = ["SimHei"] ## win
#plt.rcParams['font.family']=['SimHei'] ## win

mpl.rcParams["axes.unicode_minus"] = False

# 1）准备数据
movie_name = ['雷神3：诸神黄昏','正义联盟','东方快车谋杀案','寻梦环游记','全球风暴','降魔传','追捕','七十七天','密战','狂兽','其它']

place_count = [60605,54546,45819,28243,13270,9945,7679,6799,6101,4621,20105]



# 2）创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 3）绘制饼图
plt.pie(place_count, labels=movie_name, autopct="%1.2f%%", colors=['b','r','g','y','c','m','y','k','c','g','y'])

# 显示图例
plt.legend()

# 添加标题
plt.title("电影排片占比")

# 4）显示图像
plt.show()
~~~

### 3.Numpy

（Numerical Python）是一个开源的Python科学计算库，用于快速处理任意维度的数组。Numpy支持常见的数组和矩阵操作。对于同样的数值计算任务，使用Numpy比直接使用Python要简洁的多。Numpy使用ndarray对象来处理多维数组，该对象是一个快速而灵活的大数据容器。

#### ndarray支持并行化运算（向量化运算）

#### Numpy底层使用C语言编写，内部解除了GIL（全局解释器锁），其对数组的操作速度不受Python解释器的限制，效率远高于纯Python代码。

~~~python
import random
import time
import numpy as np
a = []
for i in range(1000):
    a.append(random.random())
t1 = time.time()
sum1=sum(a)
t2=time.time()

b=np.array(a)
t4=time.time()
sum3=np.sum(b)
t5=time.time()
print(t2-t1, t5-t4)
~~~

### 4.Pandas

- 2008年WesMcKinney开发出的库
- 专门用于数据挖掘的开源python库
- **以Numpy为基础，借力Numpy模块在计算方面性能高的优势**
- **基于matplotlib，能够简便的画图**
- **独特的数据结构**

~~~
import numpy as np
stock_change = np.random.normal(0, 1, (10, 5))
print(stock_change)
~~~

~~~
import numpy as np
stock_change = np.random.normal(0, 1, (10, 5))
stock_change = pd.DataFrame(stock_change)
print(stock_change)
~~~

DataFrame对象既有行索引，又有列索引

- 行索引，表明不同行，横向索引，叫index
- 列索引，表名不同列，纵向索引，叫columns

~~~
df = pd.DataFrame({'month': [1, 4, 7, 10],
                    'year': [2012, 2014, 2013, 2014],
                    'sale':[55, 40, 84, 31]})

   month  sale  year
0  1      55    2012
1  4      40    2014
2  7      84    2013
3  10     31    2014
~~~

读取csv

~~~
4.5.1.1 读取csv文件-read_csv
pandas.read_csv(filepath_or_buffer, sep =',' , delimiter = None)
filepath_or_buffer:文件路径
usecols:指定读取的列名，列表形式
~~~
