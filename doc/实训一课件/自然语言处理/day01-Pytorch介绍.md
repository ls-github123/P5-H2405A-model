### 1.什么是Pytorch 

Pytorch是⼀个基于Numpy的科学计算包, 向它的使⽤者提供了两⼤功能. 

作为Numpy的替代者, 向⽤户提供使⽤GPU强⼤功能的能⼒. 

做为⼀款深度学习的平台, 向⽤户提供最⼤的灵活性和速度.

### 2.Pytorch的基本元素操作

Tensors张量: 张量的概念类似于Numpy中的ndarray数据结构, 最⼤的区别在于Tensor可以利 

⽤GPU的加速功能. 

我们使⽤Pytorch的时候, 常规步骤是先将torch引⽤进来

代码

~~~python
from __future__ import print_function
import torch
#创建一个没有初始化的矩阵
x=torch.empty(5,3)
print(x)
#创建一个有初始化的矩阵
x=torch.rand（5,3)
print(x)
#创建一个全零矩阵并可指定数据元素的类型为long
x=torch.zeros(5,3,dtype=torch.long)
#直接通过数据创建张量
x=torch.tensor([2.5,3.5])
print(x)
#通过已有的一个张量创建相同尺寸的新张量,利用news_methods得到一个张量
x = x.new_ones(5,3,dtype=torch.double)
print(x)
#利用randn_like方法得到相同张量尺寸的一个新张量，并且采用随机初始化来对其赋值
y=torch.randn_like(x,dtype=torch.float)
print(y)
#得到张量的尺寸
print(x.size())

~~~

对⽐有⽆初始化的矩阵: 当声明⼀个未初始化的矩阵时, 它本身不包含任何确切的值. 当创 

建⼀个未初始化的矩阵时, 分配给矩阵的内存中有什么数值就赋值给了这个矩阵, 本质上是 

毫⽆意义的数据. 

### 3.python基本操作

#### 加法操作

~~~python
from __future__ import print_function
import torch
x = x.new_ones(5,3,dtype=torch.double)
y = torch.rand(5,3)
print(x+y)
#第二种方式
print(torch.add(x,y))
#第三种方式
#提前设定一个空的张量
result = torch.empty(5,3)
#将空的张量作为加法的结果存储张量
torch.add(x,y,out=result)
print(result)
#第四种方式 in-place(原地转换)
y.add_(x)
print(y)

~~~

注意:

所有in-place的操作函数都有⼀个下划线的后缀. 

⽐如x.copy_(y), x.add_(y), 都会直接改变x的值. 

#### 用类似于Numpy的方式对张量进行操作

~~~
print(x[:,1]
~~~

#### 改变张量的形状：torch.view()

~~~
x=torch.randn(4,4)
#tensor.view()操作需要保证数据元素的总数量不变
y=x.view(16)
#-1代表自动匹配个数
z=x.view(-1,8)
print(x.size(),y.size(),z.size())
~~~

如果张量中只有一个元素，可以用.item()将值取出，作为一个python number

~~~
x=torch.randn(1)
print(x)
print(x.item())
~~~

### 4.关于Torch Tensor和Numpy array之间的相互转换 

Torch Tensor和Numpy array共享底层的内存空间, 因此改变其中⼀个的值, 另⼀个也会随之 

被改变. 

#### 将torch tensor转换成numpy array

~~~
a = torch.ones(5)
print(a)
#将torch tensor转换成numpy array
b = a.numpy()
print(b)
#对其中一个进行加法操作，另一个也随之被改变
a.add_(1)
print(a)
print(b)
~~~

#### 将numpy array转换成torch tensor

~~~
import numpy as np
a=np.ones(5)
b=torch.from_numpy(a)
np.add(a,1,out=a)
print(a)
print(b)
~~~

所有在CPU上的Tensors, 除了CharTensor, 都可以转换为Numpy array并可以反向转换

关于Cuda Tensor: Tensors可以⽤.to()⽅法来将其移动到任意设备上

~~~python
# 如果服务器上已经安装了GPU和CUDA
if torch.cuda.is_available():
 # 定义⼀个设备对象, 这⾥指定成CUDA, 即使⽤GPU
 device = torch.device("cuda")
 # 直接在GPU上创建⼀个Tensor
 y = torch.ones_like(x, device=device)
 # 将在CPU上⾯的x张量移动到GPU上⾯
 x = x.to(device)
 # x和y都在GPU上⾯, 才能⽀持加法运算
 z = x + y
 # 此处的张量z在GPU上⾯
 print(z)
 # 也可以将z转移到CPU上⾯, 并同时指定张量元素的数据类型
 print(z.to("cpu", torch.double))
~~~

### 5.⼩节总结 

#### 学习了什么是Pytorch. 

Pytorch是⼀个基于Numpy的科学计算包, 作为Numpy的替代者, 向⽤户提供使⽤GPU强 

⼤功能的能⼒. 

做为⼀款深度学习的平台, 向⽤户提供最⼤的灵活性和速度. 

#### 学习了Pytorch的基本元素操作. 

矩阵的初始化: 

torch.empty() 

torch.rand(n, m) 

torch.zeros(n, m, dtype=torch.long) 

其他若⼲操作: 

x.new_ones(n, m, dtype=torch.double) 

torch.randn_like(x, dtype=torch.fl oat) 

x.size() 

#### 学习了Pytorch的基本运算操作.

x.view() 

x.item() 

#### 学习了Torch Tensor和Numpy Array之间的相互转换. 

##### 将Torch Tensor转换为Numpy Array: 

b = a.numpy() 

##### 将Numpy Array转换为Torch Tensor: 

b = torch.from_numpy(a) 

注意: 所有才CPU上的Tensor, 除了CharTensor, 都可以转换为Numpy Array并可以反向转 

换. 

#### 学习了任意的Tensors可以⽤.to()⽅法来将其移动到任意设备上. 

x = x.to(device)

### 6.pytorch中的autograd

在整个Pytorch框架中, 所有的神经⽹络本质上都是⼀个autograd package(⾃动求导⼯具包) 

autograd package提供了⼀个对Tensors上所有的操作进⾏⾃动微分的功能. 

#### Torch.Tensor

torch.Tensor是整个package中的核⼼类, 如果将属性.requires_grad设置为True, 它将追踪在 

这个类上定义的所有操作. 当代码要进⾏反向传播的时候, 直接调⽤.backward()就可以⾃动计 

算所有的梯度. 在这个Tensor上的所有梯度将被累加进属性.grad中. 

如果想终⽌⼀个Tensor在计算图中的追踪回溯, 只需要执⾏.detach()就可以将该Tensor从计 

算图中撤下, 在未来的回溯计算中也不会再计算该Tensor. 

除了.detach(), 如果想终⽌对计算图的回溯, 也就是不再进⾏⽅向传播求导数的过程, 也可以 

采⽤代码块的⽅式with torch.no_grad():, 这种⽅式⾮常适⽤于对模型进⾏预测的时候, 因为预 

测阶段不再需要对梯度进⾏计算. 

#### 关于torch.Function

Function类是和Tensor类同等重要的⼀个核⼼类, 它和Tensor共同构建了⼀个完整的类, 

每⼀个Tensor拥有⼀个.grad_fn属性, 代表引⽤了哪个具体的Function创建了该Tensor. 

如果某个张量Tensor是⽤户⾃定义的, 则其对应的grad_fn is None.

#### 关于Tensor的操作

~~~
x1=torch.ones(3,3)
print(x1)
x = torch.ones(2,2,requires_grad=True)
print(x)
~~~

在具有requires_grad=True的Tensor上执行一个加法操作

~~~
y=x+2
print(y)
~~~

打印Tensor的grad_fn属性

~~~
print(x.grad_fn)
print(y.grad_fn)
~~~

在tensor上执行更复杂的操作

~~~
z=y*y*3
out=z.mean()
print(z,out)
~~~

关于⽅法.requires_grad_(): 该⽅法可以原地改变Tensor的属性.requires_grad的值. 如果没 

有主动设定默认为False.

~~~
a = torch.randn(2, 2) a = ((a * 3) / (a - 1))
print(a.requires_grad)
a.requires_grad_(True)
print(a.requires_grad) b = (a * a).sum()
print(b.grad_fn)
~~~

#### 关于梯度Gradients

在Pytorch中, 反向传播是依靠.backward()实现的

~~~
z=y*y*3
out=z.mean()
out.backward()
print(x.grad)
~~~

关于⾃动求导的属性设置: 可以通过设置.requires_grad=True来执⾏⾃动求导, 也可以通过 

代码块的限制来停⽌⾃动求导. 

~~~
print(x.requires_grad)
print((x ** 2).requires_grad)
with torch.no_grad():
 print((x ** 2).requires_grad)
~~~

可以通过.detach()获得⼀个新的Tensor, 拥有相同的内容但不需要⾃动求导. 

~~~
print(x.requires_grad) y = x.detach()
print(y.requires_grad)
print(x.eq(y).all())

~~~

