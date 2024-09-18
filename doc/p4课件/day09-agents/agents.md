# 第九单元  agents

## **一、昨日知识点回顾**

```python

1.项目需求分析
2.项目流程实现
3.文件上传
4.向量数据库使用
```

------

## **二、考核目标**

```
1.当日考核目标1
2.当日考核目标2
```

------

## **三、本单元知识详讲**

### 9.1 agents

#### 9.1.1 agents介绍

Agents 是一个具有智能功能的智能体，它使用 LLM 和工具来执行任务。

Agents 核心思想是使用LLM来选择要采取的一系列动作。在链式结构中，一系列动作是硬编码的（在代码中）。 在 Agents 中，使用语言模型作为推理引擎来确定要采取的动作及其顺序。

Agents 包括几个关键组件：

\- ***\*Agent\****: 用于生成指令和执行动作的代理。

\- ***\*Tool\****: 用于执行动作的函数。

\- ***\*Memory\****: 用于存储历史对话和生成的指令。

\- ***\*LLM\****: 用于生成指令和执行动作的 LLM。

有些应用程序不仅需要预先确定的LLM（语言模型）/其他工具的调用链，还可能需要依赖用户输入的未知链条。在这些类型的链条中，有一个代理程序可以访问一套工具。根据用户的输入，代理程序可以决定是否调用这些工具中的任何一个。

目前，有两种主要类型的代理程序：

动作代理：这些代理程序决定要采取的动作，并逐个执行这些动作。

计划和执行代理：这些代理程序首先制定一套要采取的行动计划，然后逐个执行这些行动。

何时使用每种类型的代理程序？动作代理更为传统，适用于小型任务。对于更复杂或长时间运行的任务，初始的规划步骤有助于保持长期目标和专注。然而，这样做通常会增加调用次数和延迟。这两种代理程序也不是互斥的 - 实际上，通常最好由动作代理负责计划和执行代理的执行。

动作代理的高级伪代码如下：

1. 接收用户输入。
2. 代理程序决定是否使用某个工具，以及工具的输入应该是什么。
3. 使用该工具以工具输入进行调用，并记录观察结果（调用的输出）。
4. 将工具、工具输入和观察结果的历史传递回代理程序，并由代理程序决定下一步操作。
5. 重复上述步骤，直到代理程序决定不再需要使用工具，然后直接向用户做出响应。

代理程序涉及的不同抽象概念如下：

- 代理程序（Agent）：这是应用程序的逻辑所在。代理程序提供一个接口，接受用户输入以及代理程序已经执行的步骤列表，并返回代理动作（AgentAction）或代理结束（AgentFinish）。
  - 代理动作（AgentAction）：对应要使用的工具以及该工具的输入。
  - 代理结束（AgentFinish）：表示代理程序已经完成，并包含向用户返回的信息。
- 工具（Tools）：代理程序可以执行的操作。您向代理程序提供哪些工具高度取决于您希望代理程序执行的任务。
- 工具包（Toolkits）：这些是为特定用例设计的工具组合。例如，为了使代理程序能够以最佳方式与SQL数据库交互，它可能需要访问一个工具来执行查询和另一个工具来检查表格。
- 代理执行器（Agent Executor）：它包装了一个代理程序和一组工具。它负责循环地迭代运行代理程序，直到满足停止条件为止。



LangChain Agent 是 LangChain 框架中的一个重要组成部分，它代表了智能合约的实例或具有特定功能的软件程序，旨在与现实世界进行交互并执行任务。以下是对 LangChain Agent 的详细解析：

一、LangChain Agent 的基本概念

LangChain 是一个开源的语言模型集成框架，旨在简化使用大型语言模型（LLM）创建应用程序的过程。Agent 在 LangChain 中扮演着核心角色，它利用语言模型（LLM）作为推理引擎，根据实时情况决定如何调用工具并执行任务。

#### 9.1.2 LangChain Agent 的工作原理

1. **接收任务**：用户给出一个任务（Prompt），这是 Agent 工作的起点。
2. **思考（Thought）**：Agent 使用语言模型进行推理，制定解决问题的计划，并确定下一步需要采取的行动。
3. **行动（Action）**：Agent 根据计划调用相应的工具（如搜索引擎、计算器、API等），并执行必要的操作。
4. **观察（Observation）**：Agent 观察操作的结果，并将其作为新的上下文信息，用于后续的思考和行动。

这个过程会循环进行，直到语言模型认为已经找到最终答案或达到预设的迭代次数。

LangChain Agent 的类型

LangChain 提供了多种类型的 Agent，以适应不同的应用场景和需求。主要包括以下几种类型：

1. **动作代理人（Action Agents）**：在每个时间步上，使用所有先前动作的输出决定下一个动作。这类 Agent 适用于小任务或需要实时响应的场景。
2. **计划执行代理人（Plan-and-execute Agents）**：预先决定所有动作的完整顺序，然后按照计划执行，而不更新计划。这类 Agent 适用于复杂或长时间运行的任务，需要保持长期目标和重点。

LangChain Agent 的应用示例

LangChain Agent 可以应用于各种任务，如文本生成、文档问答、聊天机器人、调用特定的 SaaS 服务等。以下是一个简单的应用示例：

~~~python
from langchain.agents import initialize_agent, load_tools  
from langchain_community.llms.tongyi import Tongyi
from langchain.memory import ConversationBufferMemory  
  
# 初始化 OpenAI 语言模型  
llm = Tongyi()  
  
# 加载工具，例如数学计算工具  
tools = load_tools(["llm-math"], llm=llm)  
  
# 创建会话缓冲内存，用于保存对话历史  
memory = ConversationBufferMemory(memory_key="chat_history")  
  
# 初始化 Agent，指定代理类型和工具  
agent = initialize_agent(  
    agent="conversational-react-description",  
    tools=tools,  
    llm=llm,  
    verbose=True,  
    max_iterations=3,  
    memory=memory,  
)  
  
# 与 Agent 交互  
output_1 = agent.invoke("when you add 4 and 5 the result comes 10.")  
output_2 = agent.invoke("4 + 5 is ")  
  
print(output_1)  
print(output_2)
~~~

LangChain Agent 是一种强大的工具，它利用语言模型作为推理引擎，通过调用各种工具来执行复杂任务。不同类型的 Agent 适用于不同的应用场景，可以根据具体需求进行选择和配置。随着 LangChain 的不断发展和完善，Agent 的功能和性能也将不断提升，为开发者提供更加便捷和高效的解决方案。

#### 9.1.3 搭建工具

\- serpai是一个聚合搜索引擎，需要安装谷歌搜索包以及申请账号 https://serpapi.com/manage-api-key

\- llm-math是一个封装好的数学计算链

pip install google-search-results

~~~python
import os 
os.environ["SERPAPI_API_KEY"] = 'db166b810c6b85674b6ceab3bd4e10d5048e1ba837db1c0d962ad91b34558805'
from langchain_community.llms.tongyi import Tongyi
llm = Tongyi()
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

tools = load_tools(["serpapi","llm-math"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,#这里有不同的类型
    verbose=True,#是否打印日志
)
res = llm.invoke("请问2023年的美国总统是谁？他的年龄的除以2是多少?")
print(res)
~~~

#### 9.1.4 memory和agents配合使用

~~~python
import os 
os.environ["SERPAPI_API_KEY"] = 'db166b810c6b85674b6ceab3bd4e10d5048e1ba837db1c0d962ad91b34558805'
from langchain_community.llms.tongyi import Tongyi
llm = Tongyi()
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from langchain.memory import ConversationBufferMemory
#记忆组件
memory = ConversationBufferMemory(
    memory_key="chat_history",
)

# 定义tool
tools = load_tools(["serpapi","llm-math"],llm=llm)

# 定义agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,#记忆组件
    verbose=True,
)
print(agent)
print(agent.agent.llm_chain.prompt.template)
agent.invoke("我是张三，今年18岁，性别女，现在在深圳工作，工作年限1年，月薪5000元")
print(agent.invoke("我的名字是什么?"))
~~~

tools工具类

~~~python
import langchain
langchain.debug = True
from langchain.agents import initialize_agent, Tool
from langchain_community.llms.tongyi import Tongyi
llm = Tongyi()
from langchain.agents import AgentType

def buy_xlb(days: int):
    
    return "感冒发烧了"


def buy_jz(input: str):
    #调用天气预报接口
    res = requests.get("?city="+input)
    data = json.loads(res.text)
    return "今天35度北京"


xlb = Tool.from_function(func=buy_xlb,
                         name="buy_xlb",
                         description="当用户咨询的是关于医疗问题的时候，使用这个工具，返回值为这个函数返回的结果"
                         )
jz = Tool.from_function(func=buy_jz,
                        name="buy_jz",
                        description="当用户咨询的是关于天气问题的时候，使用这个工具，返回值为这个函数返回的结果"
                        )

tools = [xlb,jz]

llm = Tongyi()


agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

res3 = agent.run(
    "今天多少度"
)
print(res3)
~~~



### 9.2Agents 的类型

\- ZERO_SHOT_REACT_DESCRIPTION                   零样本反应描述

\- CHAT_ZERO_SHOT_REACT_DESCRIPTION              聊天零样本反应描述

\- CONVERSATIONAL_REACT_DESCRIPTION              会话反应描述

\- CHAT_CONVERSATIONAL_REACT_DESCRIPTION         聊天会话反应描述

\- STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION   聊天结构化零样本反应描述

\- STRUCTURED_ZERO_SHOT_REACT_DESCRIPTION        结构化零样本反应描述

#### 9.2.1 ZERO_SHOT_REACT_DESCRIPTION

即在没有示例的情况下可以自主的进行对话的类型。

应用场景：

主要用于即时响应描述性任务，这些任务可能不需要复杂的对话上下文，而是直接针对某个问题或请求给出描述性回答。

适用于那些需要快速生成准确描述的场景，如产品特性说明、数据报告解读等。

交互方式：

通常以单轮问答的形式进行，用户输入一个问题或请求，系统直接返回相应的描述性回答。

不涉及复杂的对话历史或会话管理。

生成内容特点：

生成的回答侧重于直接、准确的描述，可能不包含过多的对话性语言或上下文依赖。

~~~
from langchain.agents import load_tools
# 定义tools
tools = load_tools(["serpapi","llm-math"],llm=llm)

# 定义agent--（tools、agent、llm、memory）
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# print(agent)
# print("------------------------")
# print(agent.agent.llm_chain.prompt.template)

agent.invoke("现在美国总统是谁？他的年龄除以2是多少？")
~~~

#### 9.2CHAT_ZERO_SHOT_REACT_DESCRIPTION 

零样本增强式生成，即在没有示例的情况下可以自主的进行对话的类型。

应用场景：

专为聊天和对话场景设计，能够处理多轮对话，并在对话过程中生成连贯、自然的回答。

适用于需要与用户进行交互、理解用户意图并给出相应反应的场景，如聊天机器人、客服系统等。

交互方式：

支持多轮对话，能够处理用户的连续输入，并根据对话历史生成更加准确的回答。

可能需要管理对话状态、跟踪用户意图和上下文信息。

生成内容特点：

生成的回答更加自然、流畅，能够适应用户的语言风格和对话习惯。

可能包含对话性语言、问候语、确认信息等，以增强用户体验。

~~~
tools = load_tools(["serpapi","llm-math"],llm=llm)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
# print(agent)
# print("------------------------")
# print(agent.agent.llm_chain.prompt.messages[0].prompt.template)
# print("------------------------")
agent.invoke("现在美国总统是谁？他的年龄除以2是多少？")
~~~

#### 9.3 CONVERSATIONAL_REACT_DESCRIPTION

一个对话型的agent，这个agent要求与memory一起使用

~~~
from langchain.memory import ConversationBufferMemory
#记忆组件
memory = ConversationBufferMemory(
    memory_key="chat_history",
)

# 定义tool
tools = load_tools(["serpapi","llm-math"],llm=llm)

# 定义agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,#记忆组件
    verbose=True,
)
print(agent)
print(agent.agent.llm_chain.prompt.template)
agent.run("我是张三，今年18岁，性别女，现在在深圳工作，工作年限1年，月薪5000元")
agent.run("我的名字是什么?")
agent.run("有什么好吃的泰国菜可以推荐给我吗?")
agent.run("这些我都没吃过！我名字的最后一个字母是什么？1998年的世界杯谁夺冠了？")
agent.run("中国陕西西安现在的气温多少？截止目前我们聊了什么？")
~~~

#### 9.4 CHAT_CONVERSATIONAL_REACT_DESCRIPTION 使用了chatmodel

代理是 LangChain 框架中针对聊天和会话场景设计的一种高级代理类型。它利用 React 框架（在 LangChain 的上下文中，React 框架指的是一种用于决定何时调用哪个工具的逻辑框架，而非前端开发中的 React 库）来动态地选择和执行工具，同时利用会话记忆（如对话历史）来增强交互的连贯性和上下文理解能力。

~~~
from langchain.memory import ConversationBufferMemory
#记忆组件
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)

tools = load_tools(["serpapi","llm-math"],llm=llm)


agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,#记忆组件
    verbose=True,
)
print(agent)
print("1 ------------------------")
print(len(agent.agent.llm_chain.prompt.messages))
print("2 ------------------------")
print(agent.agent.llm_chain.prompt.messages[0].prompt.template)
print("3 ------------------------")
print(agent.agent.llm_chain.prompt.messages[1])
print("4 ------------------------")
print(agent.agent.llm_chain.prompt.messages[2].prompt.template)
print("5 ------------------------")
print(agent.agent.llm_chain.prompt.messages[3])
agent.run("有什么好吃的泰国菜可以推荐给我吗?用中文回答")
~~~

#### 9.2.5 STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION

~~~

from langchain.memory import ConversationBufferMemory
#记忆组件
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)

## 定义tool
tools = load_tools(["serpapi","llm-math"],llm=llm)

# 定义agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, #agent类型 
    memory=memory,#记忆组件
    handle_parsing_errors=True,
    verbose=True,
    
)
# print(agent)
# print(agent.agent.llm_chain.prompt.messages[0].prompt.template)
# print(agent.agent.llm_chain.prompt.messages[1].prompt.template)
agent.run("有什么好吃的泰国菜可以推荐给我吗?用中文回答")
~~~

#### 9.3Tools

langchain预制了大量的tools，基本这些工具能满足大部分需求。 https://python.langchain.com.cn/docs/modules/agents/tools/

\- 加载预制tool的方法

\- 几种tool的使用方式

对输出做了结构化处理

~~~
#添加预制工具的方法很简单
from langchain.agents import load_tools
tool_names = [...]
tools = load_tools(tool_names) #使用load方法

#有些tool需要单独设置llm
from langchain.agents import load_tools
tool_names = [...]
llm = ...
tools = load_tools(tool_names, llm=llm) #在load的时候指定llm
~~~

#### 9.3.1 SerpAPI

最常见的聚合搜索引擎 https://serper.dev/dashboard，支持google\bing

~~~
from langchain.utilities.serpapi import SerpAPIWrapper

# 实例化
search = SerpAPIWrapper()

search.run("美国现在的总统是谁？")
~~~

~~~
# 支持自定义参数，比如将引擎切换到bing，设置搜索语言等
params = {
    "engine": "bing",
    "gl": "us",
    "hl": "en",
}
search = SerpAPIWrapper(params=params)
search.run("美国现在的总统是谁？")
~~~

~~~
tools = load_tools(["serpapi"],llm=llm)
~~~

#### 9.3.2 Dall-E

Dall-E是openai出品的文到图AI大模型

pip install opencv-python scikit-image

~~~
from langchain.agents import initialize_agent, load_tools

tools = load_tools(["dalle-image-generator"])

agent = initialize_agent(
    tools, 
    llm, 
    agent="zero-shot-react-description",
    verbose=True
)

agent.run("Create an image of a halloween night at a haunted museum")
~~~



#### 9.3.4 Eleven Labs Text2Speech

ElevenLabs 是非常优秀的TTS合成API

\```

pip install elevenlabs

pip install --upgrade pydantic

\```

~~~
import os

os.environ["ELEVEN_API_KEY"] = "23261e4a3b79697822252a505a169863"
from langchain.tools.eleven_labs import ElevenLabsText2SpeechTool

text_to_speak = "Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!"

tts = ElevenLabsText2SpeechTool(
    voice="Bella",
    text_to_speak=text_to_speak,
    verbose=True
)
~~~

~~~
speech_file = tts.run(text_to_speak)

speech_file = tts.run(text_to_speak)

tts.stream_speech(text_to_speak)
~~~

~~~
from langchain.agents import initialize_agent, load_tools

tools = load_tools(["eleven_labs_text2speech"])

agent = initialize_agent(
    tools, 
    llm, 
    agent="zero-shot-react-description",
    verbose=True
)

agent.run("Create an image of a halloween night at a haunted museum")
~~~

#### 9.3.5 GraphQL

一种api查询语言，类似sql，我们用它来查询奈飞的数据库，查找一下和星球大战相关的电影，API地址https://swapi-graphql.netlify.app/.netlify/functions/index

\```

pip install httpx gql > /dev/null

pip install gql

pip install requests_toolbelt

\```

~~~
### from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.utilities import GraphQLAPIWrapper


tools = load_tools(
    ["graphql"],
    graphql_endpoint="https://swapi-graphql.netlify.app/.netlify/functions/index",
)

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)


~~~

#### 9.4.5 Tookit

tookit是langchain已经封装好的一系列工具，一个工具包是一组工具来组合完成特定的任务

一个python代码机器人

 pip install langchain_experimental==0.0.4

~~~
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools import PythonREPLTool
from langchain_experimental.utilities import PythonREPL
from langchain.agents.agent_types import AgentType

agent_executor = create_python_agent(
    llm=llm,
    tool=PythonREPLTool(),
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    agent_executor_kwargs={"handle_parsing_errors": True},
)

agent_executor.run("生成10个斐波那契数列?")
~~~

~~~
def generate_fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

fibonacci_sequence = generate_fibonacci_sequence(10)
fibonacci_sequence
~~~

#### 9.3.7 SQL Database

使用SQLDatabaseChain构建的agent，用来根据数据库回答一般行动饿问题

~~~
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain_community.chat_models import ChatTongyi

db = SQLDatabase.from_uri("sqlite:///db/Chinook.db")

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)
agent_executor.run("创建用户表，包括用户名和密码两个列")
~~~

### 9.4自定义Agent

\- 定义一个class

\- 工具：默认搜索

\- 提示词：定义agent要做什么任务

\- outparse：约束LLM的行为和输出

\- 不同的LLM不同的质量

自定义tools

~~~python
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain.prompts import StringPromptTemplate
from langchain import SerpAPIWrapper, LLMChain
from typing import List, Union
from langchain.schema import AgentAction, AgentFinish, OutputParserException
from langchain_community.llms.tongyi import Tongyi
import re
import os

class MyAgentTool:
    
    def __init__(self) -> None:    
        os.environ["SERPAPI_API_KEY"] = 'db166b810c6b85674b6ceab3bd4e10d5048e1ba837db1c0d962ad91b34558805'    
        self.serpapi = SerpAPIWrapper()
        
    def tools(self):
        return [
            Tool(
                name="search",
                description="适用于当你需要回答关于当前事件的问题时",
                func=self.serpapi.run,
            )
        ]
s = MyAgentTool()
s.serpapi.run("python")
    
~~~

案例

~~~
from langchain.agents import Tool, tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain.prompts import StringPromptTemplate
from langchain import SerpAPIWrapper, LLMChain
from typing import List, Union
from langchain.schema import AgentAction, AgentFinish, OutputParserException
from langchain_community.llms.tongyi import Tongyi
from langchain_community.embeddings.dashscope import DashScopeEmbeddings
# 引入向量化的类
from langchain_community.vectorstores import Chroma
import re
import os

from typing import Any

#自定义工具类
class MyAgentTool:
    def __init__(self) -> None:
        self.db = Chroma(embedding_function=DashScopeEmbeddings(),
                          persist_directory="./chroma")
        
    def tools(self):
        return [
            Tool(
                name="kg_search",
                description="当你需要回答2024年NBA冠军球队的问题时使用",
                func=self.search
            )
        ]
    
    def search(self, query: str) -> str:
        return self.db.similarity_search(query,k=2)
    
    def getdb(self):
        return self.db.__len__()
    
#可用工具
@tool
def kgg_search(query: str): 
    """当你需要回答2024年NBA冠军球队的问题时才会使用这个工具。"""
    db = Chroma(embedding_function=DashScopeEmbeddings(),persist_directory="./chroma")
    return db.similarity_search(query,k=2)

tool_list = [kgg_search]
    

class MyAgent:
    llm = None
    tools = None
    def __init__(self,llm,tools) -> None:
        #agent的提示词，用来描述agent的功能
        self.template =  """尽你最大可能回答下面问题，你将始终用中文回答. 你在必要时可以使用下面这些工具:
                    {tools}
                    使用下面的格式回答问题:
                    问题: 输入的问题
                    分析: 你对问题的分析，决定是否使用工具
                    动作: 使用工具，工具名称 [{tool_names}]
                    输入: {input}
                    观察: 动作名称
                    ... 
                    分析: 我现在知道答案了
                    答案: 这是最终的答案
                    记住使用中文回答，如果你使用英文回答将回遭到惩罚.
                    问题: {input}
                    {agent_scratchpad}"""
                    
        #定义一个openai的llm
        self.llm = llm
        #工具列表
        self.tools = tools
        #agent的prompt
        self.prompt = self.MyTemplate(
            template=self.template,
            tools=self.tools,
            #输入变量和中间变量
            input_variables=["input", "intermediate_steps"],
        )

        #定义一个LLMChain
        self.llm_chain = LLMChain(
            llm=self.llm,
            prompt = self.prompt
        )
        #工具名称列表
        self.toolnames = [tool.name for tool in self.tools]
        #定义一个agent
        self.agent = LLMSingleActionAgent(
            llm_chain=self.llm_chain,
            allowed_tools=self.toolnames,
            output_parser=self.MyOutputParser(),
            
            stop=["\n观察:"],
        )
    
    #运行agent
    def run(self, input: str) -> str:
        #创建一个agent执行器
        agent_executor = AgentExecutor.from_agent_and_tools(
            agent=self.agent, 
            tools=self.tools, 
            handle_parsing_errors=True,
            verbose=True
        )
        # agent_executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True,handle_parsing_errors=True)
        agent_executor.run(input=input)

    

    #自定义模版渲染类
    class MyTemplate(StringPromptTemplate):
        #渲染模版
        template: str
        #需要用到的工具
        tools:List[Tool]

        #格式化函数
        def format(self, **kwargs: Any) -> str:
            #获取中间步骤
            intermediate_steps = kwargs.pop("intermediate_steps")
            thoughts = ""
            for action, observation in intermediate_steps:
                thoughts += action.log
                thoughts += f"\n观察: {observation}\n想法: "
            #将agent_scratchpad设置为该值
            kwargs["agent_scratchpad"] = thoughts
            # 从提供的工具列表中创建一个名为tools的变量
            kwargs["tools"] = "\n".join([f"{tool.name}: {tool.description}" for tool in self.tools])
            #创建一个提供的工具名称列表
            kwargs["tool_names"] = ", ".join([tool.name for tool in self.tools])
            prompt_ret = self.template.format(**kwargs)
            return prompt_ret


    #自定义输出解析类
    class MyOutputParser(AgentOutputParser):
        #解析函数
        def parse(self, output: str) -> Union[AgentAction, AgentFinish]:
            #检查agent是否应该完成
            if "答案:" in output:
                return AgentFinish(
                # 返回值通常始终是一个具有单个 `output` 键的字典。
                # It is not recommended to try anything else at the moment :)
                return_values={"output": output.split("答案:")[-1].strip()},
                log=output,
                )
            #用正则解析出动作和动作输入
            regex = r"动作\s*\d*\s*:(.*?)\n输入\s*\d*\s*:[\s]*(.*)"
            match = re.search(regex, output, re.DOTALL)
            #如果没有匹配到则抛出异常
            if not match:
                raise OutputParserException(f"Could not parse LLM output: `{output}`")
            action = match.group(1).strip()
            action_input = match.group(2)
            # 返回操作和操作输入
            return AgentAction(tool=action, tool_input=action_input.strip(" ").strip('"'), log=output)

myagent = MyAgent(Tongyi(),tool_list)
myagent.run("2024年NBA冠军球队是哪只?")

# tool = MyAgentTool()
# tool.search("2024年NBA冠军球队是哪只")
~~~

~~~
from langchain.agents import initialize_agent, AgentType

agent = initialize_agent(
    MyAgentTool().tools(),
    Tongyi(),
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
# agent.run("2024年NBA冠军球队是哪只?")
agent.invoke("2024年NBA冠军球队是哪只?")

~~~



## **四、本单元知识总结**

```python
1.当日知识点总结1
2.当日知识点总结2

```

