# 第五单元  Prompts高级

## **一、昨日知识点回顾**

```python
1.langchain概述及应用场景
2.prompt提示词的应用
```

------

## **二、考核目标**

```
1.示例选择器的类型
2.prompts和示例选择器综合案例应用
3.输出解析器的各种类型及应用
```

------

## **三、本单元知识详讲**

### 5.1 示例选择器 Example selectors

#### 5.1.1 介绍及应用

如果您拥有大量的示例，您可能需要选择在提示中包含哪些示例。ExampleSelector 是负责执行此操作的类。 基本接口定义如下所示：

```text
class BaseExampleSelector(ABC):
    """Interface for selecting examples to include in prompts."""

    @abstractmethod
    def select_examples(self, input_variables: Dict[str, str]) -> List[dict]:
        """Select which examples to use based on the inputs."""
```

它只需要暴露一个 `select_examples` 方法。该方法接收输入变量并返回一个示例列表。具体如何选择这些示例取决于每个具体实现。

LangChain的示例选择器是一个用于从一组示例中动态选择部分示例以构建提示（prompt）的重要组件。在LangChain中，有多种不同类型的示例选择器，包括自定义样例选择器、长度样例选择器、MMR样例选择器、n-gram重叠度样例选择器和相似度样例选择器。以下是这些示例选择器的简要介绍和格式清晰的回答：

1. 自定义样例选择器
   - 允许用户根据自己的业务逻辑和需求来定义样例的选择方式。
   - 至少需要实现两个方法：`add_example`（用于添加新示例）和`select_examples`（基于输入变量返回一个样例列表）。
   - 用户可以通过继承`BaseExampleSelector`类并实现所需的方法来创建自定义样例选择器。
2. 长度样例选择器
   - 根据输入的长度来选择要使用的示例。对于较长的输入，它会选择较少的示例，而对于较短的输入，则会选择更多示例。
   - 这在构建提示时需要控制上下文窗口长度时特别有用。
   - 使用时，可以导入`LengthBasedExampleSelector`类，并传入示例列表来创建长度样例选择器。
3. MMR样例选择器
   - MMR（Maximum Marginal Relevance）是一种常用于信息检索和推荐系统的排序算法，也适用于样例选择。
   - MMR样例选择器通过计算示例与输入之间的相关性以及示例之间的不相似性来选择样例。
   - 具体的实现细节可能因库或框架而异，但通常用户需要指定计算相关性和不相似性的方法。
4. n-gram重叠度样例选择器
   - 基于输入和示例之间的n-gram重叠度来选择样例。
   - n-gram是一种用于表示文本中连续n个词或字符的序列的模型。
   - 通过计算输入和示例之间的n-gram重叠度，可以选择与输入内容最相关的样例。
5. 相似度样例选择器
   - 基于输入和示例之间的相似度来选择样例。
   - 相似度可以使用各种方法来计算，如余弦相似度、Jaccard相似度等。
   - 选择与输入内容最相似的样例可以帮助语言模型更好地理解prompt，并给出更准确的回答。

**归纳**：

LangChain的示例选择器为构建有效的提示提供了灵活的工具。用户可以根据具体的应用场景和需求选择合适的示例选择器。无论是根据长度、MMR算法、n-gram重叠度还是相似度来选择样例，都可以帮助提高语言模型的理解能力和回答准确性。同时，用户还可以根据自己的业务逻辑自定义样例选择器，以实现更精细的样例选择。

#### 5.1.2自定义示例选择器

我们将创建一个自定义示例选择器，该选择器从给定的示例列表中选择每个交替示例。

`ExampleSelector` 必须实现两个方法：

1. `add_example` 方法，接受一个示例并将其添加到 ExampleSelector 中
2. `select_examples` 方法，接受输入变量（用于用户输入）并返回要在 few shot prompt 中使用的示例列表。

代码实现

1.新建一张表

标题    简单描述

流感       发烧、咳嗽、喉咙痛、身体酸痛  

2.写一个vue页面，搜索框，输入标题

3.写一个接口，在接口中获取到输入信息，用自定义选择器实现，查询数据库中的数据构造examples,

4.生成prompt,调用大模型，返回结果

5.vue展示，sse流式显示



~~~python
from typing import List, Dict, Any  
from langchain.prompts.example_selector.base import BaseExampleSelector  
# 导入通义大模型
from langchain_community.llms import Tongyi
  
class MedicalExampleSelector(BaseExampleSelector):  
    def __init__(self, examples: List[Dict[str, str]]):  
        """  
        初始化医疗示例选择器  
  
        :param examples: 医疗相关的示例列表，每个示例是一个字典，包含输入和输出  
        """  
        self.examples = examples  

    def add_example(self, example: Dict[str, str]) -> None:
        """将新示例添加到存储中的键。"""
        self.examples.append(example)
  
    def select_examples(self, input_variables: Dict[str, str]) -> List[Dict[str, str]]:  
        """  
        根据输入变量选择医疗示例  
  
        :param input_variables: 包含选择条件（如疾病名称、症状等）的字典  
        :return: 符合条件的示例列表  
        """  
        # 假设我们根据疾病名称来选择示例  
        disease_name = input_variables.get("disease_name", None)  
        if disease_name is None:  
            return []  # 如果没有提供疾病名称，则返回空列表  
  
        selected_examples = [  
            example for example in self.examples  
            if disease_name.lower() in example["input"].lower()  
        ]  
  
        return selected_examples  
  
# 示例数据  
examples = [  
   {"input":"流感症状","output":"发烧、咳嗽、喉咙痛、身体酸痛。"},
{"input":"糖尿病治疗","output":"饮食控制、运动、药物"},
{"input":"新冠肺炎症状","output":"发烧、咳嗽、疲劳、味觉或嗅觉丧失。"},
{"input":"糖尿病症状","output":"口渴、尿频、体重减轻。"}, 
]  
  
# 创建医疗示例选择器实例  
medical_example_selector = MedicalExampleSelector(examples)  
  
# 选择与疾病名称 "diabetes" 相关的示例  
selected_examples = medical_example_selector.select_examples({"disease_name": "糖尿病"})  
  
# 打印选择的示例  
# print(selected_examples)

# medical_example_selector.add_example({"input":"头晕症状","output":"头晕、眼睛模糊。"})

# # 选择与疾病名称 "diabetes" 相关的示例  
# selected_examples = medical_example_selector.select_examples({"disease_name": "头晕症状"})  
  
# # 打印选择的示例  
# print(selected_examples)

# 实例化通义大模型

prompt =  '\n'.join(f"{item['input']}: {item['output']}" for item in selected_examples)  
 

print(prompt)
tongyi = Tongyi()
ret = tongyi.invoke(prompt)
print(ret)

~~~

#### 5.1.3根据长度选择

这个示例选择器根据长度选择要使用的示例。当您担心构建的提示会超过上下文窗口的长度时，这是非常有用的。对于较长的输入，它会选择较少的示例进行包含，而对于较短的输入，它会选择更多的示例。

~~~python
from langchain.prompts import PromptTemplate  
from langchain.prompts import FewShotPromptTemplate  
from langchain.prompts.example_selector import LengthBasedExampleSelector 
# 导入通义大模型
from langchain_community.llms import Tongyi


examples = [  
    {"input": "患者如何在家测量血压？", "output": "患者可以在家使用电子血压计测量血压，遵循说明书上的步骤，通常在早上和晚上各测量一次。"},  
    {"input": "糖尿病患者的饮食应该注意什么？", "output": "糖尿病患者应该注意饮食中的糖分和碳水化合物摄入，多食用蔬菜、全谷物和瘦肉，避免高糖和高脂肪食物。"},  
    {"input": "儿童发烧时应该如何处理？", "output": "儿童发烧时，应首先测量体温，如果超过38.5°C，可以使用退烧药，并给孩子多喝水，保持通风，适当减少衣物。"}  
]  

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}",
)
# 定义计算长度的函数  
def calculate_text_length(text):  
    return len(re.split("\n| ", text))  
    
example_selector = LengthBasedExampleSelector(
    # 这些是可供选择的示例。
    examples=examples,
    # 这是用于格式化示例的PromptTemplate。
    example_prompt=example_prompt,
    # 这是格式化示例的最大长度。
    # 长度由下面的get_text_length函数测量。
    max_length=10,
    
)
dynamic_prompt = FewShotPromptTemplate(
    # 我们提供一个ExampleSelector而不是示例。
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="根据描述确定病情",
    suffix="输入: {adjective}\n输出:",
    input_variables=["adjective"],
)

# 一个输入较小的示例，因此它选择所有示例。
prompt = dynamic_prompt.format(adjective="糖尿病患者的饮食")

# 一个输入较长的示例，因此它只选择一个示例。
# long_string = "big and huge and massive and large and gigantic and tall and much much much much much bigger than everything else"
# print(dynamic_prompt.format(adjective=long_string))

# 您还可以将示例添加到示例选择器中。
# new_example = {"input": "big", "output": "small"}
# dynamic_prompt.example_selector.add_example(new_example)
# print(dynamic_prompt.format(adjective="enthusiastic"))

tongyi = Tongyi()
print(prompt)
ret = tongyi.invoke(prompt)
print(ret)
~~~

#### 5.1.4最大边际相关性（MMR）选择

~~~
推荐系统
基于物品的推荐
分类表
id name

商品表
id  name  catesid

把用户id和物品存在浏览记录表，查询浏览记录表，根据商品id查询对应的分类，查询分类下销量最高的进行推荐

商品id  属性
1       休闲、舒适
2       商务


基于用户的推荐
  1.收集数据，userid  goodsid写入浏览记录表
  2.用户分层，计算用户相似度，查找和当前用户相似度最高的用户
  3.查询相似度最高的用户购买的商品和用户购买的商品取差集推荐


mmr实现基于物品的推荐
1.创建商品表，id  name  price  content sales  特征，添加测试数据
2.展示列表
A商品  100   点击标题进入详情页
B商品   200
3.在详情页写入用户浏览记录表
userid  goodid  addtime
4.在首页推荐商品
  (1)message = [{"id":1,"特征":....}]
  (2)根据用户id查询浏览记录表，查询最近的5条，获取特征
  (3)用特征做为输入条件
  (4)返回所有符合条件的id,用idlist和用户已经浏览过的差集
  (5)根据差集的id查询商品表sales排序，显示在首页
~~~



`MaxMarginalRelevanceExampleSelector`根据示例与输入之间的相似性以及多样性进行选择。它通过找到与输入具有最大余弦相似度的嵌入示例，并在迭代中添加它们，同时对已选择示例的接近程度进行惩罚来实现这一目标。

\- MMR是一种在信息检索中常用的方法，它的目标是在相关性和多样性之间找到一个平衡

\- MMR会首先找出与输入最相似（即余弦相似度最大）的样本

\- 然后在迭代添加样本的过程中，对于与已选择样本过于接近（即相似度过高）的样本进行惩罚

\- MMR既能确保选出的样本与输入高度相关，又能保证选出的样本之间有足够的多样性

\- 关注如何在相关性和多样性之间找到一个平衡

余弦相似度（Cosine Similarity）是一种常用的度量两个非零向量之间相似度的方法，广泛应用于文本挖掘、推荐系统、信息检索等领域。其原理及公式如下：

原理

余弦相似度通过计算两个向量之间的夹角的余弦值来评估它们的相似度。在向量空间中，两个向量的夹角越小，说明它们的方向越接近，从而相似度越高。余弦相似度与向量的长度无关，仅与向量的方向有关。



~~~python
from langchain.prompts import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.llms import Tongyi

#假设已经有这么多的提示词示例组：
examples =  [  
    {"id": "1", "features": ', '.join(["时尚", "运动鞋", "跑步"])},  
    {"id": "2", "features": ', '.join(["休闲", "运动鞋", "篮球"])}, 
    {"id": "3", "features": ', '.join(["商务", "皮鞋", "正装"])}, 
    {"id": "4", "features": ', '.join(["户外", "徒步鞋", "探险"])}, 
    {"id": "5", "features": ', '.join(["时尚", "板鞋", "滑板"])}, 
]  


#构造提示词模板
example_prompt = PromptTemplate(
    input_variables=["id","features"],
    template="id：{id}\n描述：{features}"
)

#调用MMR
example_selector = SemanticSimilarityExampleSelector.from_examples(
    #传入示例组
    examples,
    #使用阿里云的dashscope的嵌入来做相似性搜索
    DashScopeEmbeddings(),
    #设置使用的向量数据库是什么
    FAISS,
    #结果条数
    k=3,
)

#使用小样本提示词模版来实现动态示例的调用
dynamic_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="查询和features相似度最高的id",
    suffix="关键词为：{word}",
    input_variables=["word"]
)

print(dynamic_prompt.format(word="时尚"))

# qq = dynamic_prompt.format(word="时尚")
# llm = Tongyi()
# llm.invoke(qq)
~~~

sklearn最大余弦相似度

案例1：推荐模块

~~~python
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.metrics.pairwise import cosine_similarity  
from typing import List, Dict  
import numpy as np
  
# 假设的商品数据，每个商品由多个标签（特征）组成  
products = [  
    {"id": 1, "features": ["时尚", "运动鞋", "跑步"]},  
    {"id": 2, "features": ["休闲", "运动鞋", "篮球"]},  
    {"id": 3, "features": ["商务", "皮鞋", "正装"]},  
    {"id": 4, "features": ["户外", "徒步鞋", "探险"]},  
    {"id": 5, "features": ["时尚", "板鞋", "滑板"]},  
]  
  
# 将商品特征转换为文本，用于TF-IDF向量化  
def product_to_text(product):  
    return " ".join(product["features"])  
  
# 文本向量化  
vectorizer = TfidfVectorizer()  
product_texts = [product_to_text(p) for p in products]  
product_vectors = vectorizer.fit_transform(product_texts)  
  
# 余弦相似度计算函数  
def recommend_products(query_features: List[str], k: int = 2) -> List[Dict]:  
    query_text = " ".join(query_features)  
    query_vector = vectorizer.transform([query_text])  
      
    # 计算查询与所有商品的余弦相似度  
    similarities = cosine_similarity(query_vector, product_vectors).ravel()  
      
    # 获取最相似的k个商品的索引  
    top_indices = np.argsort(-similarities)[:k]  
      
    # 返回推荐的商品列表  
    return [products[idx] for idx in top_indices]  
  
# 示例查询  
query_features = ["时尚", "休闲"]  
recommended_products = recommend_products(query_features)  
print(recommended_products)  
~~~



- 一种常见的相似度计算方法

- 它通过计算两个向量（在这里，向量可以代表文本、句子或词语）之间的余弦值来衡量它们的相似度

- 余弦值越接近1，表示两个向量越相似

- 主要关注的是如何准确衡量两个向量的相似度

  

### 5.2综合案例

#### 5.2.1案例背景

假设我们正在构建一个基于`LangChain`的文本生成系统，该系统需要根据用户输入的关键词生成相关的故事或描述。为了提高生成的准确性和相关性，我们决定使用示例选择器来动态选择最佳的示例，这些示例将被包含在Prompt中以引导模型进行生成。

示例选择器选择

在`LangChain`中，有多种示例选择器可供选择，每种都有其特定的用途和优势。在这个案例中，我们假设选择了以下两种示例选择器：

1. **LengthBasedExampleSelector**：基于输入的长度来选择示例。当输入较长时，选择较少的示例以避免Prompt过长；当输入较短时，选择更多的示例以提供更多的上下文。
2. **SemanticSimilarityExampleSelector**：基于输入与示例之间的语义相似性来选择示例。这种方法能够确保选择的示例与输入高度相关，从而提高生成的准确性。

案例步骤

1. **定义示例列表**：
   首先，我们需要定义一个包含多个示例的列表。每个示例都应该是一个包含输入和输出的字典
2. **创建PromptTemplate**：
   接下来，我们创建一个`PromptTemplate`，该模板将用于格式化输入和输出示例，以构建最终的Prompt
3. **创建示例选择器**：
   然后，我们创建之前提到的两种示例选择器。这里，为了简化案例，我们仅展示如何使用`LengthBasedExampleSelector`，但你可以根据需要添加`SemanticSimilarityExampleSelector`。
4. **动态选择示例并构建Prompt**：
   最后，当用户输入关键词时，我们使用示例选择器动态选择示例，并使用`PromptTemplate`构建最终的Prompt。

通过结合使用`PromptTemplate`和示例选择器（如`LengthBasedExampleSelector`和`SemanticSimilarityExampleSelector`），我们能够根据输入动态选择最佳的示例，并将它们包含在Prompt中以引导模型进行生成。这种方法能够提高生成的准确性和相关性，使生成的文本更加符合用户的期望。

场景分析

1.写一张病情特征表

~~~python
id  name       特征
1    心脏病     心慌、
2    脑梗       心慌

~~~

2.用表构建 examples

3.用户通过vue页面输入 心慌

4.接口获取用户输入

修改模板

~~~python
examples =  [  
    {"name": "心脏病", "features": ""},  
    {"name": "脑梗", "features": ""}, 
   
]  

#构造提示词模板
example_prompt = PromptTemplate(
    input_variables=["name","features"],
    template=''{name}+","'
)


res = str.split(",")
for i in res:
    name = "..."
    #重新构造prompt
    prompt = "你是一个很，请帮我查询{name}治疗方案"
    invoke(prompt)
    res
     
class Goods(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    sales = models.IntegerField()
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.title
        
        
from langchain.prompts import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.llms import Tongyi
           
class TestSMM(APIView):
    def get(self,request):
        goods = Goods.objects.all()
        #假设已经有这么多的提示词示例组：
        examples =  [{"id": str(i.id), "features": i.tags} for i in goods]
       
        # #构造提示词模板
        example_prompt = PromptTemplate(
            input_variables=["id","features"],
            template="{id},"
        )
       
        # #调用MMR
        example_selector = SemanticSimilarityExampleSelector.from_examples(
            #传入示例组
            examples,
            #使用阿里云的dashscope的嵌入来做相似性搜索
            DashScopeEmbeddings(),
            #设置使用的向量数据库是什么
            FAISS,
            #结果条数
            k=3,
        )

        # #使用小样本提示词模版来实现动态示例的调用
        dynamic_prompt = FewShotPromptTemplate(
            example_selector=example_selector,
            example_prompt=example_prompt,
            prefix="",
            suffix="",
            input_variables=["word"]
        )
        #查询用户浏览记录表，获取前5条 tags
        res = dynamic_prompt.format(word="时尚")
        items = res.split(',')
        ids = [int(item.strip()) for item in items if item.strip()]
        # #查询我游览过的[3,2,1]
        vlist = [1,2,4]
        difference = list(filter(lambda x: x not in vlist, ids))
        print(difference)  # 输出: [1]
        goods = Goods.objects.filter(id__in=difference).all()
        
        return Response({"code":200})
    
~~~



#### 5.2.2vue综合案例实现

流程分析

1.写一个vue页面，获取用户输入的关键词

2.定义示例列表

3.创建PromptTemplate

4.创建示例选择器

5.当用户输入关键词时，我们使用示例选择器动态选择示例，并使用`PromptTemplate`构建最终的Prompt

6.结果返回给客户端展示

vue代码

~~~
<!-- StreamEvents.vue -->
<template>
  <div>
    <h2>Server-Sent Events Example</h2>

     <el-form :inline="true"  class="demo-form-inline">
  <el-form-item label="问题">
    <el-input v-model="askmes" placeholder="请输入问题"></el-input>
  </el-form-item>
  
  <el-form-item>
    <el-button type="primary" @click="connectToStream">查询</el-button>
  </el-form-item>
</el-form>

    <ul>
     
      <div id="notifications">{{resmes}}</div>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      askmes:'',
      source: null,
      resmes:''
    };
  },
  mounted() {
    // this.connectToStream();
  },
  beforeDestroy() {
    this.disconnectStream();
  },
  methods: {
    connectToStream() {
      
       this.source = new EventSource("http://localhost:8000/ssetest/?ask="+this.askmes);

        this.source.onmessage = (event=> {
          this.resmes = this.resmes + event.data
        });

        this.source.onerror = (error=> {
            console.error('EventSource failed:', error);
            this.source.close();
            this.source = null;
        });
    },
    disconnectStream() {
      if (this.source) {
        this.source.close();
        this.source = null;
      }
    },
  },
};
</script>
~~~

django接口

~~~python
from django.http import StreamingHttpResponse
from django.views.decorators.http import require_GET

from typing import List, Dict, Any  
from langchain.prompts.example_selector.base import BaseExampleSelector  
# 导入通义大模型
from langchain_community.llms import Tongyi


class MedicalExampleSelector(BaseExampleSelector):  
    def __init__(self, examples: List[Dict[str, str]]):  
        """  
        初始化医疗示例选择器  
  
        :param examples: 医疗相关的示例列表，每个示例是一个字典，包含输入和输出  
        """  
        self.examples = examples  

    def add_example(self, example: Dict[str, str]) -> None:
        """将新示例添加到存储中的键。"""
        self.examples.append(example)
  
    def select_examples(self, input_variables: Dict[str, str]) -> List[Dict[str, str]]:  
        """  
        根据输入变量选择医疗示例  
  
        :param input_variables: 包含选择条件（如疾病名称、症状等）的字典  
        :return: 符合条件的示例列表  
        """  
        # 假设我们根据疾病名称来选择示例  
        disease_name = input_variables.get("disease_name", None)  
        if disease_name is None:  
            return []  # 如果没有提供疾病名称，则返回空列表  
  
        selected_examples = [  
            example for example in self.examples  
            if disease_name.lower() in example["input"].lower()  
        ]  
  
        return selected_examples  
    
    
def generate_sse(prompt):
    llm=Tongyi(
        model="qwen-turbo",
        temperature=0,
        max_tokens=512,
    )
   
    for chunk in llm.stream(prompt):
        print(chunk)
        # ret = llm.invoke(prompt)
        data = f"data: {chunk}\n\n"
        if chunk:
             yield data.encode('utf-8')
        else:
            return "no mes"

@require_GET
def sse_notifications(request):
    user_input = request.GET.get('ask')  # 调用函数获取用户输入   
    
    # 示例数据  
    examples = [  
    {"input":"流感症状","output":"发烧、咳嗽、喉咙痛、身体酸痛。"},
    {"input":"糖尿病治疗","output":"饮食控制、运动、药物"},
    {"input":"新冠肺炎症状","output":"发烧、咳嗽、疲劳、味觉或嗅觉丧失。"},
    {"input":"糖尿病症状","output":"口渴、尿频、体重减轻。"}, 
    ]  
    
    # 创建医疗示例选择器实例  
    medical_example_selector = MedicalExampleSelector(examples)  
    
    # 选择与疾病名称 "diabetes" 相关的示例  
    selected_examples = medical_example_selector.select_examples({"disease_name": user_input})  
    
    # 实例化通义大模型

    prompt =  '\n'.join(f"{item['input']}: {item['output']}" for item in selected_examples)  
      
    response = StreamingHttpResponse(
        generate_sse(prompt),
        content_type="text/event-stream",
    )
    response["Cache-Control"] = "no-cache"
    return response
~~~

### 5.3输出解析器

#### 5.3.1介绍

LangChain输出解析器是LangChain框架中的一个重要组成部分，它负责将自然语言模型（如ChatGPT、GPT系列等）的输出从文本形式转换为结构化的数据格式，以便进行进一步的分析或操作。以下是对LangChain输出解析器的详细解析：

一、定义与功能

LangChain输出解析器是一种特殊的自然语言处理（NLP）技术，其核心功能是将非结构化的自然语言文本转换为结构化的数据，如JSON对象、列表等。这种转换使得输出更加易于程序理解和处理，提高了数据处理的效率和准确性。

二、工作原理

LangChain输出解析器的工作原理通常包括以下几个步骤：

1. **文本预处理**：对输入的自然语言文本进行预处理，包括去除停用词、标点符号等无意义字符，以及对文本进行分词、词性标注等操作。
2. **特征提取**：将预处理后的文本转换为向量表示，以便进行后续处理。这可以通过词袋模型、TF-IDF、Word2Vec等方法实现。
3. **模型解析**：将处理后的文本输入到训练好的输出解析器模型中，模型根据预设的规则或算法将文本解析为结构化的数据格式。
4. **输出结果**：输出解析器将解析后的结构化数据以特定的格式（如JSON、列表等）返回给调用者。

三、类型与实现

LangChain提供了多种类型的输出解析器，以满足不同的需求。这些解析器包括但不限于：

1. **结构化输出解析器**：将文本解析为JSON对象等结构化数据格式。
2. **CSV解析器**：将文本解析为CSV格式的数据，便于进行表格化处理。
3. **日期时间解析器**：专门用于处理日期和时间相关的输出，确保输出的日期和时间格式正确。
4. **枚举解析器**：将文本中的特定词汇映射为枚举类型的值，适用于处理有限集合的数据。
5. **Pydantic解析器**：利用Pydantic库的功能，将文本解析为符合特定数据模式的Python对象。

四、应用场景

LangChain输出解析器在多个领域都有广泛的应用，包括但不限于：

1. **问答系统**：从用户的问题中抽取关键信息，并将其作为查询条件在知识库中进行搜索。
2. **机器翻译**：将源语言文本解析为目标语言文本中的实体、关系等信息，以提高翻译的准确性和流畅性。
3. **摘要生成**：从原始文本中抽取关键信息，并将其组合成一个简洁的摘要。
4. **数据分析**：将自然语言形式的数据转换为结构化数据，以便进行进一步的数据分析和挖掘。

五、总结

LangChain输出解析器是LangChain框架中一项强大的功能，它能够将自然语言模型的输出转换为结构化的数据格式，为后续的处理和分析提供了极大的便利。通过不同的解析器类型，LangChain能够满足不同领域和场景下的需求，为构建高效的自然语言处理应用程序提供了有力的支持。

#### 5.3.2列表解析器

当您想要返回逗号分隔的项目列表时，可以使用此输出解析器。也可以作为CVS解析器。

~~~python
from langchain_core.output_parsers import CommaSeparatedListOutputParser,NumberedListOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate



# 定义列表解析器
output_parser = CommaSeparatedListOutputParser()

format_instructions = output_parser.get_format_instructions()



promptTemplate = PromptTemplate(
    template="列出五种{subject}。\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": format_instructions},
)

prompt=promptTemplate.format(subject="水果")

from langchain_community.llms import Tongyi
tongyi = Tongyi()
ret = tongyi.invoke(prompt)
print(ret)
output_parser.parse(ret)
~~~

#### 5.3.3日期时间解析器

这个OutputParser展示了如何将LLM的输出解析为日期时间格式。

~~~python
from langchain_community.llms import Tongyi
from langchain.prompts import PromptTemplate
from langchain.output_parsers.datetime import DatetimeOutputParser

# 1\实例化
output_parser = DatetimeOutputParser()

template = """请按下面要求回答问题:

{question}

{format_instructions}"""

# 2、定义模板
promptTemplate = PromptTemplate.from_template(
    template,
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)

# 3、生成prompt
prompt = promptTemplate.format(question="新中国成立的日期是什么？")


llm= Tongyi()
# 4、提交大模型
output = llm.invoke(prompt)
print(output)

# # 5、解析
res = output_parser.parse(output)
print(res)
~~~

#### 5.3.4 枚举解析器

**枚举解析器在 LangChain 中的可能实现和功能**：

1. 定义
   - 枚举解析器可能是 LangChain 输出解析器的一个特定实现，专门用于处理枚举类型的数据或输出。
2. 功能
   - **识别枚举值**：从模型输出中识别并提取枚举值。
   - **格式化输出**：将提取的枚举值转换为指定的数据结构或格式。
   - **验证**：可能还包括对提取的枚举值进行验证，以确保其符合预期的枚举类型。
3. 核心方法
   - `get_format_instructions`：返回指导如何格式化枚举类型输出的字符串。
   - `parse_enum`（假设的方法名）：接受一个字符串（模型输出），并尝试从中解析出枚举值。
   - `validate_enum`（假设的方法名）：验证解析出的枚举值是否有效。
4. 实现
   - 枚举解析器可能需要预定义或动态加载一个枚举类型的定义（如 Python 中的 `Enum` 类），以便能够正确解析和验证枚举值。
   - 它可能会使用正则表达式、字符串匹配或其他 NLP 技术来从模型输出中提取枚举值。
5. 使用场景
   - 当模型输出中包含枚举类型的数据时，枚举解析器可以确保这些数据被正确地提取、格式化和验证。
   - 这在处理具有固定选项集（如颜色、状态、类别等）的数据时特别有用。

~~~python
from langchain.output_parsers.enum import EnumOutputParser
from enum import Enum

class Colors(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

parser = EnumOutputParser(enum=Colors)
print(parser.parse("red"))
# -> <Colors.RED: 'red'>

# 包括空格也可以
print(parser.parse(" green"))
# -> <Colors.GREEN: 'green'>

# 包括\n\t也可以
print(parser.parse("blue\n\t"))
# -> <Colors.BLUE: 'blue'>

# 其他字符不可以
print(parser.parse("yellow"))
# -> <Colors.BLUE: 'blue'>
~~~

#### 5.3.5 Pydantic 解析器

要使用 Pydantic 解析器，必须保证大模型的输出是可靠的Json格式。

这个解析器将大模型输出的Json字符串解析为Pydantic模型。在信息提取的场景中很有用。

~~~python
from typing import List

from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator

# 定义您期望的数据结构。
class Joke(BaseModel):
    joke: str = Field(description="设置笑话的问题部分",title="笑话")
    answer: str = Field(description="解答笑话的答案部分")

# 设置一个解析器 + 将指令注入到提示模板中。
parser = PydanticOutputParser(pydantic_object=Joke)



promptTemplate = PromptTemplate(
    template="回答用户的问题：\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

prompt = promptTemplate.format(query="讲一个中文的笑话。")

ret = llm.invoke(prompt)
print(ret)

~~~



## **四、本单元知识总结**

```python
1.示例选择器的类型
2.prompts和示例选择器综合案例应用
3.输出解析器的各种类型及应用

```

