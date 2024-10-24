# 第十一单元  大模型基础

## **一、昨日知识点回顾**

```python
1. 昨日知识点1
2. 昨日知识点2
```

------

## **二、考核目标**

```
1.当日考核目标1
2.当日考核目标2

把上一单元的agent8.1放到这
```

------

## **三、本单元知识详讲**

LangChain 是一个构建应用程序的框架，这些应用程序能够利用语言模型来生成内容。它特别设计用于与大型语言模型（LLMs）结合使用，以便于开发者能够更容易地构建和部署应用，这些应用可以执行诸如回答问题、创建文档或执行其他涉及自然语言处理的任务。

LangChain 框架提供了一系列工具和服务，帮助开发者连接到不同的语言模型 API，管理数据源，并创建能够执行复杂任务的代理（agents）。这些代理可以被编程为执行特定的工作流程，例如从多个数据源收集信息，处理该信息，并以有用的方式呈现结果。

如果您想创建一个使用 LangChain 的代理，您需要定义几个关键组件：

1. **Language Model** - 您打算使用的语言模型。LangChain 支持多种模型，包括 OpenAI 的模型等。
2. **Prompts** - 这些是用来引导模型生成响应的指令或问题。它们对于定制模型输出至关重要。
3. **Memory** - 在某些情况下，您可能希望您的代理具有某种形式的记忆功能，以便它可以记住以前的对话或者在多个步骤的任务中保持上下文。
4. **Tools** - 这些是代理可以用来获取信息或与外部系统交互的任何工具或API。
5. **Chains** - 这是指一系列的步骤或操作，代理按照预定的顺序执行，以完成某个任务。



在 LangChain 中，自定义工具（Tools）是扩展框架功能的一种方式，允许您将外部 API 或服务集成到您的应用中，从而让您的语言模型能够执行更多任务。下面是如何创建自定义工具的一个基本概述：

1. **定义工具类**： 创建一个类，这个类应该继承自 `Tool` 类（或 LangChain 提供的任何相关基类），并且实现必要的方法，比如 `run` 方法，它会在工具被调用时执行。
2. **实现 `run` 方法**： 在这个方法中，您需要定义当工具被触发时应当执行的具体逻辑。这可能包括调用外部 API，查询数据库，执行系统命令等等。
3. **设置工具描述**： 您需要提供一个清晰的描述，告诉语言模型这个工具的作用是什么，以及如何正确地使用它。这有助于语言模型理解何时以及如何调用您的工具。
4. **集成到 LangChain 链条中**： 完成工具定义后，您可以将其添加到 LangChain 的链条（Chain）中，这样语言模型就可以在适当的场景下使用它了。

### prompt案例

~~~python
from langchain.chains.llm import LLMChain

from langchain_community.llms import Tongyi
from langchain.prompts.prompt import PromptTemplate

llm = Tongyi()
multiple_choise="""请针对>>>和<<<中间的用户问题，选择一个合适的工具去回答它的问题，只要用A、B、C的选项字母告诉我答案，如果你觉得不合适，请选D.
>>>{question}<<<
我们有的工具包括：
A、一个能够查询商品信息，为用户进行商品导航的工具
B、一个能够查询订单信息，获取最新的订单情况的工具
C、一个能够搜索商家的退换货政策、运费、物流时长、支付渠道、覆盖国家的工具
D、都不合适
"""
promptTemplate = PromptTemplate.from_template(template=multiple_choise)


# 多个参数
chain = LLMChain(
    llm=llm, 
    prompt= promptTemplate,
    verbose=True,#打开日志
)
question = "我想买一件衣服，不知道哪个好看，你能推荐一下吗？"
ret = chain(question)

def goods():
     return "返回推荐的商品"
if ret == 'A':
     goods()
 
    
     
print(ret['text'])
~~~

### tools案例

~~~python
from langchain.agents import initialize_agent,Tool
from langchain_community.llms import Tongyi
from langchain.agents import AgentType
llm = Tongyi()

#查询关于订单的问题
def search_order(input:str)->str:
    print("订单号为:",input)
    #查询mysql数据库 requests.get(url,params={"weather":input})
    orders = Orders.objects.filter(order_no=input).first()
    olist={"1":"生成","2":"已支付","3":"已发货"}
    status = olist[orders.status]
    time = orders.update_time
    return "订单状态："+status+"，发货日期:"+time


#查询关于推荐产品
def recommend_product(input:str)->str:
    #查询mysql数据库
    return "裙子"

#模拟问电商faq
def faq(input:str)->str:
    #查询faiss
    return "7天无理由退货"

tools=[
    Tool(name="search order",func=search_order,
    description = "当用户咨询关于订单的问题用这个工具回答"),
    Tool(name="recommend product",func=recommend_product,
    description = "当用户咨询关于推荐产品问题用这个工具回答"),
    Tool(name="faq",func=faq,
    description = "当用户咨询模拟问电商faq用这个工具回答"),
]
agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
res = agent.invoke("查询订单，订单号为1001")
print(res)
~~~

基于医疗平台的问答

需求首页有一个问答功能，用户可以问查询药品订单、在线咨询病情（Rag增强）、查询医生

1.创建表 医生表、订单表（发货表orderno）、下载一个医疗文章的pdf

2.文件上传功能。把pdf文件上传存入向量数据库

3.搜索功能实现

​     1.写三个tools，第一个查询订单表，获取订单号去订单表中查询状态发货表中查询发货时间

​     2.查询医生，查询医生表模糊查询返回

​     3.在线咨询病情，查询faiss，写prompt调用模型返回结果



### tools基于Faiss检索

faq.txt

~~~
{"question":"请问可以送到三亚吗","answer":"可以送的，大概需要5天时间"},
{"question":"请问可以送到北京吗","answer":"可以，需要1天时间"}
~~~



~~~python
from langchain_community.vectorstores import FAISS
from langchain.embeddings.dashscope import DashScopeEmbeddings
from langchain.text_splitter import SpacyTextSplitter
# from langchain import VectorDBQA
from langchain.chains import RetrievalQA
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_community.document_loaders import TextLoader


from langchain_text_splitters import CharacterTextSplitter

from langchain_community.llms.tongyi import Tongyi
llm = Tongyi()

# 实例化向量嵌入器
embeddings = DashScopeEmbeddings()
 
# 初始化缓存存储器
store = LocalFileStore("./cache/")
 
# 创建缓存支持的嵌入器
cached_embedder = CacheBackedEmbeddings.from_bytes_store( embeddings, store, namespace=embeddings.model)
 
# 加载文档并将其拆分成片段
doc = TextLoader("./doc/faq.txt",encoding='utf-8').load()
spliter = CharacterTextSplitter("\n",chunk_size=200, chunk_overlap=0)
chunks = spliter.split_documents(doc)

 # 创建向量存储
docsearch = FAISS.from_documents(chunks, cached_embedder)
# 创建检索器
retriever = docsearch.as_retriever()
faq_chain= RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

from langchain.agents import tool
from langchain.agents import initialize_agent,Tool
from langchain.agents import AgentType

@tool("FAQ")
def faq(input:str)->str:
    """
    当你需要回答关于商品问题的时候使用，比如咨询等问题
    """
    
    return faq_chain.run(input)

#查询关于订单的问题
def search_order(input:str)->str:
    print("订单号为****:",input)
    if input.strip() == "1001":
        return "订单号为1001的商品已经到达天津"
    return "订单状态：已发货，发货日期:2023-10-01"


#查询关于推荐产品
def recommend_product(input:str)->str:
    return "裙子"



tools=[
    Tool(name="search order",func=search_order,
    description = "当用户咨询订单问题的时候使用这个工具，从用户输入中提取订单号根据订单号查询,输入只要订单号后面的码不要订单号三个字"),
    Tool(name="recommend product",func=recommend_product,
    description = "当用户咨询关于推荐产品问题用这个工具回答"),
    faq
]
agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
res = agent.invoke("我有一个订单，订单号是 1001,请帮我查询一下?")
print(res) 
~~~

### prompt优化

~~~
description = "一个帮助用户查询最新订单状态的工具，并且能处理以下情况：1.在用户没有输入订单号的情况，会询问用户订单号 2 在用户输入的订单号查询不到的时候，会让用户二次确认订单号是否正确")
~~~

### 正则验证订单号

~~~python
#查询关于订单的问题
def search_order(input:str)->str:
    pattern = r"\d+[A-Z]"
    match = re.search(pattern,input)
    if match:
        order_number=match.group(0)
        return "订单号已经处理完成，正在发货"
    else:
        return "请问您的订单号是多少？"
~~~

### 订单查询多轮对话

支持多轮对话，因为用户不一定是在第一轮提问的时候就给出了订单号。

~~~python
from langchain_community.vectorstores import FAISS
from langchain.embeddings.dashscope import DashScopeEmbeddings
# from langchain import VectorDBQA
from langchain.chains import RetrievalQA
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_community.document_loaders import TextLoader


from langchain_text_splitters import CharacterTextSplitter

from langchain_community.llms.tongyi import Tongyi
llm = Tongyi()

# 实例化向量嵌入器
embeddings = DashScopeEmbeddings()
 
# 初始化缓存存储器
store = LocalFileStore("./cache/")
 
# 创建缓存支持的嵌入器
cached_embedder = CacheBackedEmbeddings.from_bytes_store( embeddings, store, namespace=embeddings.model)
 
# 加载文档并将其拆分成片段
doc = TextLoader("./doc/faq.txt",encoding='utf-8').load()
spliter = CharacterTextSplitter("\n",chunk_size=200, chunk_overlap=0)
chunks = spliter.split_documents(doc)

 # 创建向量存储
docsearch = FAISS.from_documents(chunks, cached_embedder)
# 创建检索器
retriever = docsearch.as_retriever()
faq_chain= RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

from langchain.agents import tool
from langchain.agents import initialize_agent,Tool
from langchain.agents import AgentType
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory
import re,json
#定义prompt
answer_order_info = PromptTemplate(template="请把下面的订单信息回复给用户:\n\n {order}?",input_variables=['order'])
answer_order_llm=LLMChain(llm=llm,prompt=answer_order_info)
@tool("FAQ")
def faq(input:str)->str:
    """
    当你需要回答关于商品问题的时候使用，比如咨询等问题
    """
    return faq_chain.run(input)

#查询关于订单的问题，不经过思考，直接把回答传给用户
@tool("SearchOrder",return_direct=True)
def search_order(input:str)->str:
    """
    请你用订单号回答客户的问题
    """
    pattern = r"\d+[A-Z]"
    match = re.search(pattern,input)
    if match:
        order_number=match.group(0)
        return answer_order_llm.run(json.dumps({"id":order_number,"title":"订单详情"}))
    else:
        return "请问您的订单号是多少？"


#查询关于推荐产品
def recommend_product(input:str)->str:
  
    return "裙子"



tools=[
    search_order,
    Tool(name="recommend product",func=recommend_product,
    description = "当用户咨询关于推荐产品问题用这个工具回答"),
    faq
]
memory = ConversationBufferMemory(memory_key='chat_history',return_message=True)
agent = initialize_agent(tools,llm,agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,memory=memory,verbose=True)
res = agent.invoke("我有一个订单，一直没有收到，能帮我查一下吗？")
print(res) 
res = agent.invoke("我的订单号是100AZ？")
print(res) 
res = agent.invoke("我的订单号是多少？")
print(res) 
print(memory)


~~~

基于医疗平台的问答多轮对话

~~~
1.写一个vue页面，用于获取用户输入问题
2.构造一个txt文件，requests爬取10000条数据，解析{"question":"请问可以送到三亚吗","answer":"可以送的，大概需要5天时间"}存入txt中
3.把文件信息写入向量数据库
4.设计一个agent
   如果问的医疗知识，查询文章表
   如果用户查询总诊订单，查询订单表，如果没支付，如果分配医生，返回医生信息
   其他查询向量数据库
   
5.加上memory，重构memory，提取信息
   
message = ref([])

submit =()=>{
		const mes = {"ask":"用户说:"+mes,'answer':''}
		http.post().then(res=>{
			mes['answer'] = "ai说："+res.data.mes
		
		})
		message.value.push(mes)
}

<ul>
	<li v-for="i in message"> {{i.ask}}{{i.answer}}</li>
</ul>
~~~

客服机器人

在线咨询->点击-》输入框-》我想了解一下上衣-》推荐系统

​                                             订单-》订单系统

​                                             物流-》物流系统

​                                              其他问题-》查询faiss（问答系统获取数据处理）

电影豆瓣

1.requests爬取电影名称，评分，链接，介绍，电影对应的评价

2.bs4或者xpath解析数据，把电影的基本信息存入mysql数据库，电影评论信息存入向量数据库{"id":1,"name":"电影名","comment":['','','']}

3.写一个vue页面，问答-》输入问题

​        1.查看详情，查询电影信息返回电影名称和id,点击详情进入详情页面，显示所有信息

​        2.查看电影评论，第二个tools查询向量数据库，处理成json返回



## **四、本单元知识总结**

```python
1.当日知识点总结1
2.当日知识点总结2

```

