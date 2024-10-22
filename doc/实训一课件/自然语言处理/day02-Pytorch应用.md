### 1.使⽤Pytorch构建⼀个神经⽹络

关于torch.nn: 

使⽤Pytorch来构建神经⽹络, 主要的⼯具都在torch.nn包中. 

nn依赖于autograd来定义模型, 并对其⾃动求导. 

### 2.构建神经⽹络的典型流程: 

~~~
1.定义⼀个拥有可学习参数的神经⽹络 

2.遍历训练数据集 

3.处理输⼊数据使其流经神经⽹络 

4.计算损失值 

5.将⽹络参数的梯度进⾏反向传播 

6.以⼀定的规则更新⽹络的权重
~~~

### 3.我们⾸先定义⼀个Pytorch实现的神经⽹络

~~~python
# 导⼊若⼲⼯具包
import torch
import torch.nn as nn
import torch.nn.functional as F
# 定义⼀个简单的⽹络类
class Net(nn.Module):
     def __init__(self):
         super(Net, self).__init__()
         # 定义第⼀层卷积神经⽹络, 输⼊通道维度=1, 输出通道维度=6, 卷积核⼤⼩3*3
         self.conv1 = nn.Conv2d(1, 6, 3)
         # 定义第⼆层卷积神经⽹络, 输⼊通道维度=6, 输出通道维度=16, 卷积核⼤⼩3*3
         self.conv2 = nn.Conv2d(6, 16, 3)
         # 定义三层全连接⽹络
         self.fc1 = nn.Linear(16 * 6 * 6, 120)
         self.fc2 = nn.Linear(120, 84)
         self.fc3 = nn.Linear(84, 10)
     def forward(self, x):
         # 在(2, 2)的池化窗⼝下执⾏最⼤池化操作
         x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
         x = F.max_pool2d(F.relu(self.conv2(x)), 2)
         x = x.view(-1, self.num_flat_features(x))
         x = F.relu(self.fc1(x))
         x = F.relu(self.fc2(x))
         x = self.fc3(x)
         return x
     def num_flat_features(self, x):
         # 计算size, 除了第0个维度上的batch_size
         size = x.size()[1:]
         num_features = 1
         for s in size:
             num_features *= s
         return num_features
net = Net()
print(net)

	
~~~

注意

模型中所有的可训练参数, 可以通过net.parameters()来获得

~~~
params = list(net.parameters())
print(len(params))
print(params[0].size())
~~~

假设图像的输⼊尺⼨为32 * 32: 

~~~
input = torch.randn(1, 1, 32, 32)
out = net(input)
print(out)
~~~

有了输出张量后, 就可以执⾏梯度归零和反向传播的操作了. 

~~~
net.zero_grad()
out.backward(torch.randn(1, 10))
~~~

torch.nn构建的神经⽹络只⽀持mini-batches的输⼊, 不⽀持单⼀样本的输⼊. 

⽐如: nn.Conv2d 需要⼀个4D Tensor, 形状为(nSamples, nChannels, Height, Width). 如 

果你的输⼊只有单⼀样本形式, 则需要执⾏input.unsqueeze(0), 主动将3D Tensor扩充成 

4D Tensor. 