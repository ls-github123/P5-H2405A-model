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

llm.invoke(prompt.format(topic="冰激凌"))
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













## **四、本单元知识总结**

```python
1.当日知识点总结1
2.当日知识点总结2

```

