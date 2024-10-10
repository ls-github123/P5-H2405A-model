# 第十单元  LCEL

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
```

------

## **三、本单元知识详讲**

### 10.1 LangChain表达式 (LCEL)

#### 10.1.1LCEL介绍

LangChain表达式语言，或者LCEL，是一种声明式的方式，可以轻松地将链条组合在一起。 LCEL从第一天开始就被设计为支持将原型放入生产中，不需要改变任何代码，从最简单的“提示+LLM”链到最复杂的链(我们已经看到人们成功地在生产中运行了包含数百步的LCEL链)。

LCEL的特征：

\- 流式支持 当你用LCEL构建你的链时，你可以得到最佳的首次到令牌的时间(输出的第一块内容出来之前的时间)。对于一些链，这意味着例如我们直接从LLM流式传输令牌到一个流式输出解析器，你可以以与LLM提供者输出原始令牌相同的速率得到解析后的、增量的输出块。

\- 异步支持 任何用LCEL构建的链都可以通过同步API(例如在你的Jupyter笔记本中进行原型设计时)以及异步API(例如在LangServe服务器中)进行调用。这使得可以使用相同的代码进行原型设计和生产，具有很好的性能，并且能够在同一台服务器中处理许多并发请求。

\- 并发支持 无论何时，你的LCEL链有可以并行执行的步骤(例如，如果你从多个检索器中获取文档)，我们都会自动执行，无论是在同步接口还是异步接口中，以获得最小可能的延迟。

\- 重试和回退 为你的LCEL链的任何部分配置重试和回退。这是一种使你的链在大规模下更可靠的好方法。我们目前正在努力为重试/回退添加流式支持，这样你就可以在没有任何延迟成本的情况下获得增加的可靠性。

\- 访问中间结果 对于更复杂的链，通常在最终输出产生之前就能访问中间步骤的结果是非常有用的。这可以用来让最终用户知道正在发生什么，甚至只是用来调试你的链。你可以流式传输中间结果，它在每个LangServe服务器上都可用。

\- 输入和输出模式 输入和输出模式为每个LCEL链提供了从你的链的结构中推断出来的Pydantic和JSONSchema模式。这可以用于验证输入和输出，是LangServe的一个重要部分。

案例

~~~python
from langchain_community.llms.tongyi import Tongyi
from langchain_community.chat_models.tongyi import ChatTongyi

llm = Tongyi()
chat = ChatTongyi()

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

chain.invoke({"topic": "冰激凌"})


~~~

#### 10.1.2 执行流程

| 符号类似于 unix 管道操作符，它将不同的组件链接在一起，将一个组件的输出作为下一个组件的输入。

在这个链条中，用户输入被传递给提示模板，然后提示模板的输出被传递给大模型，然后模型的输出被传递给输出解析器。下面逐个组件地看一下，以真正理解发生了什么。

Prompt

prompt 是一个 BasePromptTemplate，这意味着它接受一个模板变量的字典并生成一个 PromptValue。PromptValue 是一个包装完成的提示的包装器，可以传递给 LLM（它以字符串作为输入）或 ChatModel（它以消息序列作为输入）。它可以与任何语言模型类型一起使用，因为它定义了生成 BaseMessage 和生成字符串的逻辑。

~~~
prompt_value = prompt.invoke({"topic": "冰激凌"})
prompt_value
~~~

~~~
prompt_value.to_messages()
~~~

~~~
prompt_value.to_string()
~~~

**model**

然后将 PromptValue 传递给 model。在这种情况下，我们的 model 是一个 ChatModel，这意味着它将输出一个 BaseMessage。

**Output parser**

 Output parser的输入BaseMessage，输出是结果字符串

~~~
output_parser.invoke(message)
~~~

### 10.2 **RAG Search Exampl**

不包括文档加载，分割等功能。

\- 建立向量数据

\- 使用RAG增强

~~~python

from operator import itemgetter

from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough,RunnableParallel
from langchain_community.embeddings.dashscope import DashScopeEmbeddings

vectorstore = FAISS.from_texts(
    ["张三在北京工作,工资是3000每月"], embedding=DashScopeEmbeddings()
)
retriever = vectorstore.as_retriever()

template = """根据下面的内容回答问题:
{context}

问题: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    | prompt
    | llm
    | StrOutputParser()
)

chain.invoke(input="张三在哪工资挣多少钱")
~~~

### 10.3 自定义输入变量

~~~python
template = """请使用{language}，根据下面的内容回答问题:
{context}

问题: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    {
        "context": itemgetter("question") | retriever,
        "question": itemgetter("question"),
        "language": itemgetter("language"),
    }
    | prompt
    | llm
    | StrOutputParser()
)

chain.invoke({"question": "张三在哪工作", "language": "英文"})
~~~

### 10.4流式响应

~~~python
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi


chat = ChatTongyi()

prompt = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话")


chain = prompt | chat


for s in chain.stream({"topic": "熊"}):
    print(s.content, end="", flush=True)
~~~

batch同步

~~~
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi


chat = ChatTongyi()

prompt = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话")


chain = prompt | chat 

print(chain.batch([{"topic": "熊"}, {"topic": "猫"}, {"topic": "狗"}]))
~~~

### 10.5并发支持

并发批处理，适用于大量生成

使用RunnableParallel类

~~~python
from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.tongyi import Tongyi

llm = Tongyi()

chain1 = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话") | llm
chain2 = ChatPromptTemplate.from_template("写一篇关于{topic}的诗歌") | llm
combined = RunnableParallel(joke=chain1, poem=chain2)


print(combined.invoke([{"topic": "熊"}, {"topic": "猫"}]))
~~~

### 10.6典型用法

#### 10.6.1 Prompt+LLM

基本构成：

PromptTemplate / ChatPromptTemplate -> LLM / ChatModel -> OutputParser

~~~python

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.tongyi import Tongyi

llm = Tongyi()

prompt = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话")

# 标准用法
chain = prompt | llm
print(chain.invoke({"topic": "狗熊"}))

# 加入停止符
chain = prompt | llm.bind(stop=["\n"])
chain.invoke({"topic": "狗熊"})

# 加入function_call

functions = [
    {
        "name": "joke",
        "description": "讲笑话",
        "parameters": {
            "type": "object",
            "properties": {
                "setup": {"type": "string", "description": "笑话的开头"},
                "punchline": {"type": "string","description": "爆梗的结尾"},
            },
            "required": ["setup", "punchline"],
        },
    }
]
chain = prompt | llm.bind(function_call={"name": "joke"}, functions=functions)
print(chain.invoke({"topic": "狗熊"}))
~~~

#### **Prompt+LLM+OutputParser**

~~~python

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.tongyi import Tongyi

llm = Tongyi()

prompt = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话")


from langchain_core.output_parsers import StrOutputParser

chain = prompt | llm | StrOutputParser()
print(chain.invoke({"topic": "狗熊"}))
~~~

#### **## Chains+Chains**



一个链的输出作为下一个链的输入

**### 使用Runnables来连接多链结构**

以下3个方式是等效的，功能就是取输入中的变量的值

{"context": retriever, "question": RunnablePassthrough()}

RunnableParallel(context=retriever, question=RunnablePassthrough())

RunnableParallel({"context": retriever, "question": RunnablePassthrough()})

下面的语句功能也是取输入中的变量的值

itemgetter("question") # 取输入的变量

~~~python

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.tongyi import Tongyi

llm = Tongyi()

from operator import itemgetter #获取可迭代对象中指定索引或键对应的元素

from langchain.schema import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt1 = ChatPromptTemplate.from_template("{person}来自于哪个城市?")
prompt2 = ChatPromptTemplate.from_template("{city}属于哪个省? 用{language}来回答")

chain1 = prompt1 | llm | StrOutputParser()

chain2 = (
    {"city": chain1, "language": itemgetter("language")} #获取invoke中的language
    | prompt2
    | llm
    | StrOutputParser()
)
print(chain1.invoke({"person": "马云"}))
print(chain2.invoke({"person": "马云", "language": "中文"}))
~~~

#### **### 多链执行与结果合并**

​      输入

​      / \

​     /   \

 分支1   分支2

​     \   /

​      \ /

​    合并结果

~~~python

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.tongyi import Tongyi
from langchain.schema import StrOutputParser

llm = Tongyi()
from langchain_core.runnables import RunnablePassthrough

prompt1 = ChatPromptTemplate.from_template(
    "生成一个{attribute}属性的颜色。除了返回这个颜色的名字不要做其他事:"
)
prompt2 = ChatPromptTemplate.from_template(
    "什么水果是这个颜色:{color},只返回这个水果的名字不要做其他事情:"
)
prompt3 = ChatPromptTemplate.from_template(
    "哪个国家的国旗有这个颜色:{color},只返回这个国家的名字不要做其他事情:"
)
prompt4 = ChatPromptTemplate.from_template(
    "请问{country}有{fruit}吗？"
)

model_parser = llm | StrOutputParser()

# 生成一个颜色
chain_color_generator = {"attribute": RunnablePassthrough()} | prompt1 | {"color": model_parser}

chain_color_to_fruit = prompt2 | model_parser
chain_color_to_country = prompt3 | model_parser

chain_question_generator = chain_color_generator | {"fruit": chain_color_to_fruit, "country": chain_color_to_country} | prompt4
prompt = chain_question_generator.invoke("红色")
prompt.to_string()
chain = chain_question_generator | llm | StrOutputParser()
print(chain.invoke("红色"))
~~~

案例2

~~~

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.tongyi import Tongyi
from langchain.schema import StrOutputParser
from operator import itemgetter

llm = Tongyi()

from langchain_core.runnables import RunnableLambda, RunnablePassthrough,RunnableParallel



planner = (
    ChatPromptTemplate.from_template("生成一个关于{input}的论点")
    | llm
    | StrOutputParser()
    | {"base_response": RunnablePassthrough()}
)

arguments_for = (
    ChatPromptTemplate.from_template(
        "列出以下内容的优点或积极方面:{base_response}"
    )
    | llm
    | StrOutputParser()
)
arguments_against = (
    ChatPromptTemplate.from_template(
        "列出以下内容的缺点或消极方面:{base_response}"
    )
    | llm
    | StrOutputParser()
)

final_responder = (
    ChatPromptTemplate.from_messages(
        [
            ("ai", "{original_response}"),
            ("human", "积极:\n{results_1}\n\n消极:\n{results_2}"),
            ("system", "根据评论生成最终的回复"),
        ]
    )
    | llm
    | StrOutputParser()
)

chain = (
    planner
    | {
        "results_1": arguments_for,
        "results_2": arguments_against,
        "original_response": itemgetter("base_response"),
    }
    | final_responder
)

print(planner.invoke("是否有外星人"))

pp = (planner
    | {
        "results_1": arguments_for,
        "results_2": arguments_against,
        "original_response": itemgetter("base_response"),
    })
print(pp.invoke("是否有外星人"))
print(chain.invoke({"input": "是否有外星人"}))
~~~

#### Memory

~~~python


from langchain_community.llms.tongyi import Tongyi
llm = Tongyi()


from operator import itemgetter

from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个乐于助人的机器人"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)
memory = ConversationBufferMemory(return_messages=True)
memory.load_memory_variables({})

chain = (
    RunnablePassthrough.assign(
        history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
    )
    | prompt
    | llm
)

inputs = {"input": "你好我是张三"}
response = chain.invoke(inputs)

#保存记忆
memory.save_context(inputs, {"output": response})
memory.load_memory_variables({})

inputs = {"input": "我叫什么名字?"}
response = chain.invoke(inputs)
print(response)
~~~

#### agent案例

~~~python


from langchain_community.llms.tongyi import Tongyi
llm = Tongyi()

from langchain import hub
from langchain.agents import AgentExecutor, tool
from langchain.agents.output_parsers import XMLAgentOutputParser

#可用工具
@tool
def search(query: str) -> str:
    """当需要了解最新的天气信息的时候才会使用这个工具。"""
    return "晴朗,32摄氏度,无风"
tool_list = [search]
tool_list

#提示词模版
# https://smith.langchain.com/hub
# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/xml-agent-convo")

def convert_intermediate_steps(intermediate_steps):
    log = ""
    for action, observation in intermediate_steps:
        log += (
            f"<tool>{action.tool}</tool><tool_input>{action.tool_input}"
            f"</tool_input><observation>{observation}</observation>"
        )
    return log

#将工具列表插入到模版中
def convert_tools(tools):
    return "\n".join([f"{tool.name}: {tool.description}" for tool in tools])

# 定义agent
agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: convert_intermediate_steps(
            x["intermediate_steps"]
        ),
    }
    | prompt.partial(tools=convert_tools(tool_list))
    | llm.bind(stop=["</tool_input>", "</final_answer>"])
    | XMLAgentOutputParser()
)

#执行agent
agent_executor = AgentExecutor(agent=agent, tools=tool_list, verbose=True)

print(agent_executor.invoke({"input": "北京今天的天气如何?"}))
~~~



## **四、本单元知识总结**

```python
1.当日知识点总结1
2.当日知识点总结2

```

