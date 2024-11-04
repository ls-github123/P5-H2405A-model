#### 字符串分割

使用langchain的text_splitter模块，导入CharacterTextSplitter类

\- separator 分隔符

\- chunk_size 每块的最大长度

\- chunk_overlap 重复字符的长度

关于 `chunk_overlap` 参数，它指的是在分割文本时，相邻的两个文本块之间将有多少字符是重叠的。这个参数在某些情况下非常有用，比如当你想要确保某些关键信息（如句子的一部分）不会恰好被分割在两个不同的块中时。通过设置重叠，你可以增加相邻块之间的上下文联系，这有助于后续处理（如文本摘要、情感分析等）时保持更好的连贯性。

~~~
from langchain_community.document_loaders import TextLoader

# 实例化TextLoader对象
loader = TextLoader("doc/NBA新闻.txt",encoding="utf-8")
# 加载文档
docs = loader.load()
print(docs)

# 导入分割类
from langchain.text_splitter import CharacterTextSplitter

# 实例化
text_splitter = CharacterTextSplitter(separator="\n",chunk_size=150, chunk_overlap=0)

text_splitter.split_documents(docs)
~~~

###  常见的词向量模型

#### 1one-hot编码

one-hot编码

无论是人类还是计算机都很难直接将语言字符进行计算。我们期望着把语言字符转换为一种便于计算的形式，也就是把对应的词汇用数值类型的数据进行唯一表示。最简单的一种将语言字符转换为便于计算的一种方式就是one-hot编码。

~~~
Color  
-----  
red  
green  
blue  
red
~~~

结果

~~~
Color_red  Color_green  Color_blue  
---------  -----------  ----------  
    1          0           0  
    0          1           0  
    0          0           1  
    1          0           0
~~~

在这个例子中，我们为每一个颜色创建了一个新的列，并且在原始数据中的颜色对应的列上标记为 1，其余列标记为 0。

One-Hot Encoding 的主要优点是它创建了一个稀疏矩阵（稀疏矩阵（Sparse Matrix）是一种特殊的数据结构，其中绝大多数元素都是零（0）。在稀疏矩阵中，非零元素的数量远小于矩阵的总元素数量。由于稀疏矩阵中的大部分元素都是零，因此直接使用标准的矩阵存储方式（如二维数组）会浪费大量的存储空间。因此，稀疏矩阵通常采用特殊的存储格式来节省空间，并提高计算效率），这个矩阵可以很容易地用于大多数机器学习算法。然而，它的缺点也很明显，那就是当类别的数量非常大时，会导致特征空间变得非常大，这可能会增加计算成本，并可能导致过拟合。此外，One-Hot Encoding 不能很好地处理有序类别变量（即类别之间存在自然顺序的情况）。

\- 优点：

1）解决了分类器处理离散数据困难的问题

2）一定程度上起到了扩展特征的作用

\- 缺点：

1）没有考虑到词与词之间的顺序问题

2）全部都是词与词之间相互独立的表示

3）one-hot得到的特征是离散的，稀疏的

为了解决one-hot编码中词与词之间独立的缺点，引入embedding矩阵。embedding矩阵是一个行数为one-hot编码列数，列数自定义的一个随机权重矩阵。



#### 2 Word2Vec

 Word2vec 也叫 Word Embeddings，中文名“词向量”。作用就是将自然语言中的字词转为计算机可以理解的稠密向量（Dense Vector）。在word2vec出现之前，自然语言处理经常把字词转为离散的单独的符号，也就是One-Hot Encoder。

Word2Vec是由谷歌于2013年正式提出的，但是对词向量的研究可以追溯到2003年论文《a neural probabilistic language model》。但正是谷歌对Word2Vec的成功应用，让词向量的技术得以在业界迅速推广，使Embedding这一研究话题成为热点。毫不夸张地说，Word2Vec对人工智能时代Embedding方向的研究具有奠基性的意义。

Word2Vec是一种在自然语言处理中广泛使用的词嵌入技术，它通过训练神经网络模型将文本中的每个单词映射为一个高维向量，从而捕捉单词之间的语义关系。以下是一个Word2Vec的案例，用于说明其工作原理和应用。

案例背景

假设我们有一个包含大量文本数据的语料库，我们的目标是学习这些文本中单词的语义表示，以便在后续的NLP任务中使用。

Word2Vec模型训练

1. 数据预处理
   - 对文本数据进行清洗，去除标点符号、停用词等无关信息。
   - 将文本数据切分为单词或短语，构建词汇表。
2. 模型选择
   - 选择Word2Vec模型，并确定其参数，如向量维度（例如，100维）、窗口大小（例如，5）等。
   - Word2Vec提供了两种主要的训练模型：Skip-Gram和CBOW（Continuous Bag of Words）。Skip-Gram模型通过给定一个中心词来预测其上下文单词，而CBOW模型则通过上下文单词来预测中心词。
3. 训练过程
   - 使用语料库中的文本数据训练Word2Vec模型。在训练过程中，模型会学习单词之间的共现关系，并将每个单词映射为一个高维向量。
   - 训练完成后，模型会生成一个词汇表到向量的映射表，其中每个单词都对应一个唯一的向量表示。

Word2Vec应用

1. 语义相似度计算
   - 利用Word2Vec生成的词向量，我们可以计算两个单词之间的语义相似度。例如，通过计算“猫”和“狗”两个单词向量的余弦相似度，我们可以发现它们之间的语义关系较为接近。
2. 文本分类
   - 在文本分类任务中，我们可以将文本中的单词转换为对应的词向量，并将这些向量作为特征输入到分类模型中。由于词向量能够捕捉单词之间的语义关系，因此这种方法通常能够提高文本分类的准确率。
3. 推荐系统
   - 在推荐系统中，我们可以将用户的行为序列和文本内容映射为词向量表示，然后计算用户向量和文本向量之间的相似度，从而为用户推荐相关的文本内容。

安装使用

以下是一个使用Python和Gensim库来训练Word2Vec模型的简单案例代码。Gensim是一个流行的主题建模和文档相似性检索的库，其中包含了对Word2Vec的实现。

首先，确保你已经安装了Gensim库。如果没有，可以使用pip进行安装：

~~~
pip install gensim
~~~

实现步骤：

第⼀步: 获取训练数据 

第⼆步: 训练词向量 

第三步: 模型超参数设定 

第四步: 模型效果检验 

第五步: 模型的保存与重加载

代码

~~~python
from gensim.models import Word2Vec  
from gensim.models.word2vec import LineSentence  
import logging  
  
# 配置日志，避免训练过程中的警告信息  
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)  
  
# 假设我们有一个名为'text_corpus.txt'的文本文件，每行包含一个句子，句子中的单词由空格分隔  
sentences = LineSentence('text_corpus.txt')  # 加载文本数据  
  
# 训练Word2Vec模型  
# 参数可以根据你的数据和需求进行调整  
#参数如vector_size（向量维度）、window（上下文窗口大小）、min_count（最小词频）和workers（工作线程数）都可以根据你的数据集和需求进行调整。
model = Word2Vec(sentences, vector_size=100, window=15, min_count=1, workers=4)  
  
# 保存模型，以便后续使用  
model.save("word2vec.model")  
  
# 加载已保存的模型  
# model = Word2Vec.load("word2vec.model")  
  
# 查找单词的向量表示  
vector = model.wv['apple']  # 假设'apple'在我们的词汇表中  
# print(vector)  
  
# 查找最相似的单词  
similar_words = model.wv.most_similar('apple')  
print(similar_words)  
  
~~~



#### 3 Embedding

Embedding在大模型中的到了广泛的应用。

ChatGPt在transform的基础上训练了自己的词向量模型。 还有阿里、百度分别推出了自己的词向量模型。

那么如何存储Embeddin呢，那么就需要用到向量数据库了，向量数据库后面再讲解。

Embedding，中文直译为“嵌入”，常被翻译为“向量化”或者“向量映射”。

计算机如何表示客观知识的世界？

![123](/Users/hanxiaobai/Downloads/dxb/h2405a/doc/p4课件/day03-大模型基础/images/20240527092224523.jpg)



**embedding**（嵌入）

在机器学习和自然语言处理（NLP）中，**embedding**（嵌入）是一种将一个高维空间中的对象（如单词、短语、句子、图像等）映射到一个低维、稠密、连续的向量空间中的表示方法。这种表示方法通常能够保留原始对象之间的某些关系或属性，使得在向量空间中相似的对象具有相近的表示。

在自然语言处理中，**word embedding**（词嵌入）是最常见的嵌入类型，它将词汇表中的每个单词映射到一个固定大小的向量。这些向量通常是通过训练神经网络模型（如Word2Vec、GloVe、FastText等）在大量文本数据上学习得到的。

词嵌入的主要优点包括：

1. **语义表示**：词嵌入能够捕捉单词之间的语义关系。在向量空间中，相似的单词（如“猫”和“狗”）通常具有相近的表示，而不相关的单词则具有较远的距离。
2. **降低维度**：与独热编码相比，词嵌入使用低维向量表示单词，从而减少了计算复杂性和存储需求。
3. **泛化能力**：由于词嵌入是在大量文本数据上训练得到的，因此它们能够处理未见过的单词或短语（通过计算其附近单词的向量表示的平均值或类似方法）。

词嵌入在NLP任务中有着广泛的应用，如文本分类、情感分析、命名实体识别、机器翻译等。通过将文本中的单词表示为词嵌入向量，可以将NLP任务转化为机器学习问题，并利用各种机器学习算法进行建模和预测。

此外，除了词嵌入之外，还有其他类型的嵌入方法，如句子嵌入（将整个句子映射为一个向量）和文档嵌入（将整个文档映射为一个向量）。这些嵌入方法可以帮助我们处理更复杂的NLP任务，如问答系统、文本摘要等。

安装

~~~
pip3 install torch
~~~

案例

~~~python
import torch  
import torch.nn as nn  
import torch.optim as optim  
  
# 超参数  
vocab_size = 10000  # 词汇表大小  
embedding_dim = 50  # 嵌入维度  
output_dim = 2      # 输出维度（例如，二分类任务）  
num_epochs = 5      # 训练轮数  
batch_size = 64     # 批处理大小  
learning_rate = 0.001 # 学习率  
  
# 模拟文本数据（实际中你会从文本数据集中获取这些索引）  
# 这里我们随机生成一些单词索引作为示例  
text_indices = torch.randint(0, vocab_size, (batch_size, 10))  # (batch_size, sequence_length)  
  
# 标签数据（随机生成）  
labels = torch.randint(0, output_dim, (batch_size,))  
  
# 定义模型  
class SimpleEmbeddingModel(nn.Module):  
    def __init__(self, vocab_size, embedding_dim, output_dim):  
        super(SimpleEmbeddingModel, self).__init__()  
        self.embedding = nn.Embedding(vocab_size, embedding_dim)  
        self.fc = nn.Linear(embedding_dim, output_dim)  
  
    def forward(self, text_indices):  
        # 取文本序列中最后一个单词的嵌入（简化的例子）  
        embedded = self.embedding(text_indices)[:, -1, :]  
        output = self.fc(embedded)  
        return output  
  
# 实例化模型  
model = SimpleEmbeddingModel(vocab_size, embedding_dim, output_dim)  
  
# 定义损失函数和优化器  
criterion = nn.CrossEntropyLoss()  
optimizer = optim.SGD(model.parameters(), lr=learning_rate)  
  
# 训练模型  
for epoch in range(num_epochs):  
    # 前向传播  
    outputs = model(text_indices)  
    loss = criterion(outputs, labels)  
  
    # 反向传播和优化  
    optimizer.zero_grad()  
    loss.backward()  
    optimizer.step()  
  
    # 打印统计信息  
    if (epoch+1) % 1 == 0:  
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')  
  
# 训练完成后，你可以通过调用model.embedding来获取嵌入层  
# 例如，查询索引为5的单词的嵌入向量  
embedding_vector = model.embedding(torch.tensor([5], dtype=torch.long))  
print(embedding_vector)
~~~

### 向量模型的区别BGE、BCE 和 M3E

#### BGE (Bi-Encoder for Generating Embeddings)

介绍
BGE 指的是一种双编码器模型，用于生成嵌入向量（Embeddings）。这种模型通常用于句子级别的语义表示，可以用于句子相似度计算、信息检索等任务。
原理：BGE模型使用两个编码器，一个用于编码查询句子，另一个用于编码文档或答案句子。两个编码器的输出向量通过某种相似度度量（余弦相似度）进行比较，以评估两个句子之间的相似度。
应用场景：BGE模型常用于搜索引擎中的相关性评分、问答系统的候选答案排序等任务。

#### BCE (Binary Cross Entropy)

介绍
BCE 是二元交叉熵（Binary Cross Entropy）的简称，这是一种常用的损失函数，常用于二分类问题中。
原理：二元交叉熵损失函数衡量了两个概率分布之间的差异，其中一个分布通常是由模型预测得到的概率，另一个则是真实的标签（0 或 1）。

应用场景：BCE广泛应用于深度学习中的二分类任务，如图像分类中的正负样本分类、情感分析中的正面负面情绪分类等。

~~~python
损失函数（Loss Function）是机器学习和深度学习中一个关键的概念，它用于衡量模型预测值与真实值之间的差异。损失函数的选择和设计直接影响到模型的训练效果和最终性能。损失函数的值越小，表明模型的预测结果与真实值之间的差距越小，即模型的性能越好。因此，通常情况下，损失函数的值越小越好。在训练过程中，随着迭代次数的增加，损失函数的值应该是单调递减的。如果损失函数的值在训练过程中没有明显下降，甚至上升，这可能意味着出现了过拟合或欠拟合等问题。
过拟合（over-fitting）：所建的机器学习模型或者是深度学习模型在训练样本中表现得过于优越，导致在测试数据集中表现不佳。
欠拟合（under-fitting）：模型学习的太过粗糙，连训练集中的样本数据特征关系都没有学出来。


大多数深度学习框架（如TensorFlow、PyTorch等）都提供了现成的损失函数实现，可以直接调用

import torch
import torch.nn as nn

# 创建MSE损失对象
mse_loss = nn.MSELoss()

# 假设真实值和预测值
y_true = torch.tensor([1.0, 2.0, 3.0])
y_pred = torch.tensor([1.5, 1.8, 3.2])

# 计算损失
loss = mse_loss(y_pred, y_true)
print("MSE Loss: ", loss.item())

~~~

解决过拟合问题

~~~
1. 增加训练数据
原理：更多的训练数据可以帮助模型更好地学习数据中的通用模式，而不是仅仅学习训练集中的特异性细节。
实践：如果可能的话，收集更多的数据或者使用数据增强技术（如图像旋转、缩放等）来生成更多的训练样本。
2. 简化模型
原理：减少模型的复杂度可以降低其过拟合的可能性。
实践：减少模型的层数或节点数，或者使用更简单的模型架构（如线性模型代替复杂的神经网络）。
3. 正则化
原理：正则化通过对模型参数施加惩罚来防止模型过于复杂。
方法：
L1 正则化（Lasso Regression）：对参数的绝对值进行惩罚，有助于产生稀疏解。
L2 正则化（Ridge Regression）：对参数的平方值进行惩罚，有助于缩小参数值。


~~~

解决欠拟和的问题

~~~
1. 增加模型复杂度
原理：通过增加模型的复杂度，使模型能够更好地拟合数据中的模式。
实践：
增加神经网络层数：对于深度学习模型，可以通过增加隐藏层数量来提高模型的复杂度。
增加每层的神经元数目：增加每层的宽度也可以提高模型的表达能力。
使用更复杂的模型：例如从线性模型转向非线性模型，如决策树、支持向量机（SVM）等。

2. 增加特征
原理：增加特征可以帮助模型更好地捕捉数据中的信息。
实践：
添加多项式特征：对于线性模型，可以添加多项式特征来增加模型的非线性能力。
特征工程：手动选择或构造新的特征，以捕捉数据中的更多信息。
使用特征选择技术：如主成分分析（PCA）、线性判别分析（LDA）等，来提取更有意义的特征。

3. 改进特征表示
原理：通过改进特征的表示形式，可以提高模型的拟合能力。
实践：
词嵌入（Word Embedding）：对于文本数据，可以使用词嵌入技术来表示词语，以捕捉词语之间的关系。
图像预处理：对于图像数据，可以进行归一化（它通过调整数据的尺度，使得数据在一定范围内，从而消除数据量纲和量级的影响，提高模型训练的稳定性和速度。最小最大值归一化将数据缩放到一个固定的范围内，通常为 [0, 1] 或 [-1, 1]。Z-score标准化（或称为标准化）通过将数据转换为标准正态分布（均值为0，标准差为1）来实现）预处理，以改善特征的质量。

4. 增加训练次数
原理：通过增加训练次数，可以让模型有更多机会学习数据中的模式。
实践：
增加训练迭代次数：在训练过程中，增加训练轮次，使模型有更多机会收敛到一个好的解。
调整学习率：使用学习率衰减策略，或者使用自适应学习率调整算法（如Adam、RMSprop等），以帮助模型更好地收敛。
5. 使用更强的学习算法
原理：选择更强的学习算法可以提高模型的拟合能力。
实践：
集成学习：使用集成学习方法，如随机森林（Random Forest）、梯度提升树（Gradient Boosting Trees）（通过不断地添加新模型来修正已有模型的预测误差，从而构建一个强模型）等，以提高模型的泛化能力。
使用预训练模型：利用预训练模型的特征提取能力，然后在特定任务上进行微调。
6. 改进优化算法
原理：通过改进优化算法，可以让模型更快地找到全局最优解或较好的局部最优解。
实践：
使用动量（Momentum）：在梯度下降算法中加入动量项，以帮助模型更快地逃离局部极小值。

~~~

随机森林

~~~
随机森林算法原理
1. 集成学习（Ensemble Learning）
集成学习的思想是通过组合多个模型的预测结果来提高整体的预测性能。随机森林正是基于集成学习思想的一种算法，它通过构建多个决策树来实现。

2. 决策树（Decision Tree）
随机森林中的每一个成员都是一个决策树。决策树是一种树形结构的分类模型，它通过一系列的规则来划分数据，最终到达叶子节点，每个叶子节点对应一个类别或输出值。

3. 随机抽取子样本（Bootstrapping）
随机森林在构建每棵树时，都会从原始数据集中通过有放回的方式随机抽取一个子样本（Bootstrap Sample），这样每个子样本与原始数据集大小相同，但包含了一些重复的样本。这种方法称为自助法（Bootstrapping）。

4. 随机选取特征（Feature Randomness）
在构建每棵决策树的过程中，不是使用所有特征来选择分裂节点，而是从所有特征中随机选取一个子集来进行分裂。这样做可以减少模型之间的相关性，从而提高模型的整体泛化能力。

5. 集成预测结果
每棵树都会对输入样本进行预测，最终的预测结果通常是通过投票（对于分类问题）或取平均（对于回归问题）的方式来决定的。

随机森林的实现过程
随机森林的构建过程可以概括为以下几个步骤：

1. 数据准备
准备训练数据集 

2. 抽取子样本
从原始数据集 中随机抽取 n 个样本（有放回抽取），形成一个新的数据集 
3. 构建决策树
对于每一个子样本 ，构建一棵决策树 

重复上述步骤直到达到预设的最大深度或满足停止条件。
4. 集成预测
对于分类问题，每棵树对输入样本进行分类预测，最终结果为多数表决的结果。
对于回归问题，每棵树对输入样本进行回归预测，最终结果为所有树预测值的平均值。
优点
鲁棒性强：随机森林能够处理高维数据和大量的特征，不易受到异常值的影响。
泛化能力强：通过集成多个决策树，随机森林具有较强的泛化能力，不易过拟合。
特征重要性评估：随机森林可以评估特征的重要性，帮助特征选择。
缺点
解释性较弱：相比于单一决策树，随机森林的解释性较差，因为它是多个决策树的集成。
计算成本高：训练多个决策树需要消耗较多的计算资源和时间，尤其是在大数据集上。
~~~



#### M3E (Multimodal Multilingual Multitask Encoder)

介绍
M3E 表示一种多模态、多语言、多任务的编码器模型。这类模型旨在处理来自不同模态（如文本、图像、音频等）的数据，并能够支持多种语言和任务。
原理：M3E模型通常设计为能够处理多种类型的数据，并且可以在多种任务上进行训练，如翻译、图像描述生成、语音识别等。
应用场景：M3E模型可以应用于跨模态检索、多语言翻译、多任务学习等领域，特别是在需要综合多种类型的数据进行决策或生成的情况下。

总结
BGE 是一种用于生成句子嵌入的双编码器模型，主要用于句子相似度计算和信息检索。
BCE 是一种常用于二分类问题的损失函数，用于衡量模型预测与真实标签之间的差异。
M3E 是一种多模态、多语言、多任务的编码器模型，旨在处理多种类型的数据并在多种任务上进行训练。
这三种概念在NLP领域有着不同的应用范围和目的。BGE主要用于句子级别的语义表示，BCE则是用于监督学习中的损失计算，而M3E则是一种更为综合性的模型，适用于处理多模态和多语言的数据。

DashScopeEmbeddings 是指使用阿里云DashScope平台提供的嵌入（Embedding）服务。嵌入服务主要用于将文本转换成向量表示，这些向量可以用来计算文本之间的相似度，支持诸如语义搜索、推荐系统、问答系统等多种应用场景

BGE是由北京智源人工智能研究院提出的新的embedding模型。BGE一发布得到了大家的广泛关注，相比于其他的中文embedding模型，在benchmark测评平台的检索任务上排名是最高的，目前现在在工业界也是应用的非常多。我们也做了一些测试，显示BGE的效果确实还不错。
此外BGE的训练主要包括3部分：
（1）通用文本上进行预训练；
（2）通用文本上finetinue(采用unlabeled数据)；
（3）特定任务上finetinue(采用有labeled数据)；
bge向量模型是1024维的，可以在自有数据集上做微调，这进一步方面提升bge在私有数据集上的准确度。

M3E是由MokaAI训练的：专注于中文文本处理，具有强大的文本处理能力和灵活的部署选项，M3E属于小模型，资源使用不高，CPU也可以运行，适合私有化部署和资源受限的环境。

BCE是网易有道训练并发布的，主要用于他自己的开源产品Qanything，能获得到的资料比较少。

### BGE部署

bge我们项目中使用的是bge-large-zh-v1.5版本，在本地部署的，部署使用的是langchain中HuggingFaceBgeEmbeddings，本地部署需要指定bge模型文件的路径，然后启动项目就可以了。主要使用两个方法：embed_documents和embed_query。分别是向量化文档和向量化查询语句。
bge向量模型是1024维的，支持在自有数据集上做微调，不过我们项目中没有微调。

- 下载向量模型bge-large-zh-v1.5

```
git clone https://huggingface.co/BAAI/bge-large-zh-1.5
或者
git clone https://www.modelscope.cn/AI-ModelScope/bge-large-zh-v1.5.git
```

- 安装依赖

```
pip install sentence-transformers
```

- 模型加载：

```
from langchain.embeddings import HuggingFaceBgeEmbeddings
embeddings = HuggingFaceBgeEmbeddings(
    model_name="E:/model/bge-large-zh-v1.5"
)
ff = embeddings.embed_documents(["你好"])
print(ff)
print(len(ff[0]))
```

### Milvus

#### 简介

Milvus 是一个开源的向量数据库，旨在解决向量搜索问题。Milvus 支持向量搜索、向量索引、向量存储、向量搜索服务、向量数据管理、向量数据可视化等功能。

Milvus 支持 Python、Java、C++、Go、Rust、JavaScript 等语言，支持 CPU 和 GPU 硬件加速。

Milvus 支持多种索引类型，包括 Flat、IVF_FLAT、IVF_SQ8、IVF_PQ、HNSW

Milvus 支持多种向量距离计算方式，包括 L2、IP、Cosine。

Milvus 支持多种数据存储方式，包括 Memory、Mmap、S3、MinIO、Local。

Milvus 支持多种数据可视化方式，包括 Milvus Web、Milvus Dashboard、Milvus WebUI、Milvus Grafana。

官网：https://milvus.io/

#### 架构

Milvus 2.0 是一款云原生向量数据库，采用​存储与计算分离​的架构设计，所有组件均为无状态组件，极大地增强了系统弹性和灵活性。

![image](/Users/hanxiaobai/Downloads/dxb/讲义/assets/image-20240630234444648.png)

整个系统分为四个层次：

 接入层（Access Layer）：系统的门面，由一组无状态 proxy 组成。对外提供用户连接的 endpoint，负责验证客户端请求并合并返回结果。

 服务层（Coordinator Service）：系统的大脑，负责分配任务给执行节点。协调服务共有四种角色，分别为 root coord、data coord、query coord 和 index coord。

 执行节点（Worker Node）：系统的四肢，负责完成协调服务下发的指令和 proxy 发起的数据操作语言（DML）命令。执行节点分为三种角色，分别为 data node、query node 和 index node。

 存储服务 （Storage）： 系统的骨骼，负责 Milvus 数据的持久化，分为元数据存储（meta store）、消息存储（log broker）和对象存储（object storage）三个部分。

#### 基本概念

#### db

数据库

#### Collection

包含一组 entity，可以等价于关系型数据库系统（RDBMS）中的表。

#### Entity

包含一组 field。field 与实际对象相对应。field 可以是代表对象属性的结构化数据，也可以是代表对象特征的向量。primary key 是用于指代一个 entity 的唯一值。

**注意：**​ 你可以自定义 primary key，否则 Milvus 将会自动生成 primary key。请注意，目前 Milvus 不支持 primary key 去重，因此有可能在一个 collection 内出现 primary key 相同的 entity。

#### Field

Entity 的组成部分。​​Field​​ 可以是结构化数据，例如数字和字符串，也可以是向量。

**注意：**​

Milvus 2.0 现已支持标量字段过滤。并且，Milvus 2.0 在一个集合中只支持一个主键字段。

#### Milvus 与关系型数据库的对应关系如下：

| Milvus向量数据库 | 关系型数据库 |
| ---------------- | ------------ |
| Collection       | 表           |
| Entity           | 行           |
| Field            | 字段         |

#### Partition

分区是集合（Collection）的一个分区。Milvus 支持将收集数据划分为物理存储上的多个部分。这个过程称为分区，每个分区可以包含多个段。

#### Segment

Milvus 在数据插入时，通过合并数据自动创建的数据文件。一个 collection 可以包含多个 segment。一个 segment 可以包含多个 entity。在搜索中，Milvus 会搜索每个 segment，并返回合并后的结果。

#### Sharding

Shard 是指将数据写入操作分散到不同节点上，使 Milvus 能充分利用集群的并行计算能力进行写入。默认情况下，单个 Collection 包含 2 个分片（Shard）。目前 Milvus 采用基于​主键哈希​的分片方式，未来将支持随机分片、自定义分片等更加灵活的分片方式。

**注意：**​ 分区的意义在于通过划定分区减少数据读取，而分片的意义在于多台机器上并行写入操作。

#### 索引

索引基于原始数据构建，可以提高对 collection 数据搜索的速度。Milvus 支持多种​​索引类型​​。为提高查询性能，你可以为每个向量字段指定一种索引类型。目前，一个向量字段仅支持一种索引类型。切换索引类型时，Milvus 自动删除之前的索引。

#### 数据类型

```
Primary key field supports:

INT64: numpy.int64
VARCHAR: VARCHAR
Scalar field supports:

BOOL: Boolean (true or false)
INT8: numpy.int8
INT16: numpy.int16
INT32: numpy.int32
INT64: numpy.int64
FLOAT: numpy.float32
DOUBLE: numpy.double
VARCHAR: VARCHAR
JSON: JSON
Array: Array
FLOAT_VECTOR
```

### Milvus 安装

#### docker安装 Milvus

```
curl -sfL https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh -o standalone_embed.sh

bash standalone_embed.sh start
```

#### docker compose 安装 milvus

#### 在线安装

```
wget https://github.com/milvus-io/milvus/releases/download/v2.4.5/milvus-standalone-docker-compose.yml -O docker-compose.yml

sudo docker compose up -d

Creating milvus-etcd  ... done
Creating milvus-minio ... done
Creating milvus-standalone ... done
```

### Milvus 使用

#### 自定义创建表

```
from pymilvus import MilvusClient, DataType
# 3. Create a collection in customized setup mode

# 3.1. Create schema
schema = MilvusClient.create_schema(
    auto_id=False,
    enable_dynamic_field=True,
)

# 3.2. Add fields to schema
schema.add_field(field_name="my_id", datatype=DataType.INT64, is_primary=True)
schema.add_field(field_name="my_vector", datatype=DataType.FLOAT_VECTOR, dim=5)

# 3.3 准备索引parameters
index_params = client.prepare_index_params()

# 3.4 添加索引
index_params.add_index(
    field_name="my_id",
    index_type="STL_SORT"
)

index_params.add_index(
    field_name="my_vector", 
    index_type="IVF_FLAT",
    metric_type="IP",
    params={ "nlist": 128 }
)

# 3.5 创建collection
client.create_collection(
    collection_name="my_collection1",
    schema=schema,
    index_params=index_params
)
```

