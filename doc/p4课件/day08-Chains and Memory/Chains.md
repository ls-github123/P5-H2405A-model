# 第八单元  Chains and Memory

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

8.1  8.2  8.8
```

------

## **三、本单元知识详讲**

### 8.1 Chains

#### 8.1.1 **什么是链**

在简单应用中，单独使用LLM是可以的，但更复杂的应用需要将LLM进行链接。例如，我们可以创建一个链，该链接收用户输入，使用PromptTemplate对其进行格式化，然后将格式化后的响应传递给LLM。链允许我们将多个组件组合在一起创建一个单一的、连贯的应用。

四个常用的链：

\- LLMChain：一个链，将一个LLM和一个PromptTemplate组合在一起。

\- SimpleSequentialChain：一个简单的链，将一个链的输出作为下一个链的输入。

\- SequentialChain：一个更复杂的链，允许我们定义多个链，并将它们链接在一起。

\- ConversationChain：一个链，将一个LLM和一个ConversationPromptTemplate组合在一起。

### 8.2 LLMChain

#### 8.2.1 LLMChain介绍

LLMChain是一个在语言模型周围添加功能的简单链，它被广泛地应用于LangChain中，包括其他链和代理。以下是关于LLMChain的详细解释：

1. 定义与结构
   - LLMChain由一个PromptTemplate和一个语言模型（LLM或聊天模型）组成。
   - 它接受用户输入，使用PromptTemplate进行格式化，然后将格式化后的响应传递给LLM。
2. 应用背景
   - 在LangChain这样的框架中，LLMChain被用作构建基于大语言模型（LLM）应用程序的重要组件。
   - LangChain旨在简化LLM应用程序的开发过程，并提供了一系列模块和工具来支持常见的用例。
3. 使用场景
   - LLMChain的使用场景广泛，包括但不限于聊天机器人、智能问答工具、文档分析和摘要、代码分析等。
   - 开发人员可以使用LLMChain来构建上下文感知、推理应用程序，实现从原型到生产环境的快速转化。
4. 优势与特点
   - 模块化设计：LLMChain作为LangChain框架的一部分，采用模块化设计，使得开发者能够更加便捷地进行模块化的开发和维护。
   - 易用性强：LangChain框架提供了丰富的API和文档，让开发者可以更加便捷地进行LLM应用的开发。
   - 高性能：LangChain框架在底层进行了优化，保证了LLM应用的高性能，使得开发者可以在保证性能的前提下，更加专注于业务逻辑的实现。
5. 工作原理
   - 当用户输入一个提示时，LLMChain首先使用PromptTemplate对输入进行格式化。
   - 然后，它将格式化后的提示传递给LLM（如ChatGPT），由LLM生成相应的回答或响应。
   - 最后，LLMChain将LLM生成的响应返回给用户。
6. 集成与合作
   - LLMChain可以与其他LangChain组件（如Agents、Chains、Memory等）进行集成，以构建更复杂、更强大的LLM应用程序。
   - 它还可以与各种LLM和聊天模型进行配合，如OpenAI的GPT系列模型，以实现更丰富的功能和更高的性能。
7. 发展趋势
   - 随着人工智能技术的不断发展，LLMChain和LangChain等框架将继续在LLM应用开发领域发挥重要作用。
   - 未来，这些框架可能会进一步优化性能、提升易用性，并扩展更多的应用场景和功能。

#### 8.2.2 LLMChain案例

~~~python
from langchain.chains.llm import LLMChain

from langchain_community.llms import Tongyi
from langchain.prompts.prompt import PromptTemplate

llm = Tongyi()
promptTemplate = PromptTemplate.from_template("你是起名大师，我家是{sex}宝，姓{firstName}，请起3个好养的名字？")


# 多个参数
chain = LLMChain(
    llm=llm, 
    prompt= promptTemplate,
    verbose=True,#打开日志
)
ret = chain.invoke({'sex': "男",'firstName': "王"})

print(ret)
~~~

### 8.3 SimpleSequentialChain

#### 8.3.1 SimpleSequentialChain介绍

只支持固定的链路

SimpleSequentialChain是Langchain框架中的一种顺序链类型，它的主要特点是每个步骤都具有单一输入/输出，并且一个步骤的输出是下一个步骤的输入。以下是关于SimpleSequentialChain的详细解释：

1. 定义与结构
   - SimpleSequentialChain是顺序链的最简单形式，它允许用户将多个单输入/单输出链连接成一个链。
   - 在这种链中，每个步骤的输出都会直接传递给下一个步骤作为输入。
2. 特点
   - **单一输入输出**：每个步骤都接受一个输入并产生一个输出，这个输出将作为下一个步骤的输入。
   - **顺序执行**：步骤按照定义的顺序依次执行，确保数据按照预期的方式流动。
   - **易于理解**：由于其简单性，SimpleSequentialChain易于理解和实现，特别适用于简单的场景。
3. 使用场景
   - SimpleSequentialChain适用于那些需要按顺序执行多个单输入/单输出步骤的场景。
   - 例如，在一个文本处理任务中，可能需要先对文本进行分词，然后对每个词进行词性标注，最后进行命名实体识别。这些步骤可以作为一个SimpleSequentialChain来执行。
4. 与SequentialChain的区别
   - SequentialChain是更通用的顺序链形式，它允许多个输入/输出，并且步骤之间可以有更复杂的依赖关系。
   - 相比之下，SimpleSequentialChain更加简单和直接，适用于那些不需要复杂依赖关系的场景。
5. 示例
   - 假设我们有一个简单的文本处理任务，需要先将文本转换为小写，然后去除标点符号，最后进行分词。这三个步骤可以作为一个SimpleSequentialChain来执行。
   - 在这个示例中，第一个步骤的输入是原始文本，输出是转换为小写的文本；第二个步骤的输入是转换为小写的文本，输出是去除标点符号的文本；第三个步骤的输入是去除标点符号的文本，输出是分词后的结果。

#### 8.3.2案例

~~~python
from langchain.chains.llm import LLMChain
from langchain_community.llms import Tongyi

llm = Tongyi()

from langchain.prompts import ChatPromptTemplate
from langchain.chains.sequential import SimpleSequentialChain

#chain 1
first_prompt = ChatPromptTemplate.from_template("帮我给{product}的公司起一个响亮容易记忆的名字?")

chain_one = LLMChain(
    llm=llm,
    prompt=first_prompt,
    verbose=True,
)

#chain 2
second_prompt = ChatPromptTemplate.from_template("用5个词来描述一下这个公司名字：{company_name}")

chain_two = LLMChain(
    llm=llm,
    prompt=second_prompt,
    verbose=True,
)

# 实例化
simple_chain = SimpleSequentialChain(
    chains=[chain_one, chain_two],
    verbose=True,#打开日志
)

simple_chain.invoke("智能机器人")
~~~

医疗平台

~~~
加载文档-》翻译成中文-》提取摘要-》基于摘要自动生成5条好评，用摘要去调用大模型查询治疗方案
~~~



### 8.4 SequentialChain

#### 8.4.1介绍

支持多个链路的顺序执行

SequentialChain是LangChain库中的一个重要概念，它允许用户将多个链（Chain）按照特定的顺序连接起来，形成一个处理流程。以下是关于SequentialChain的详细解释：

定义与结构

- **SequentialChain**：它是一种链式结构，可以将多个LLMChain（或其他类型的Chain）按照特定的顺序连接起来。这种结构使得一个大任务可以被分解为多个小任务，并依次执行。
- **结构特点**：SequentialChain允许用户定义任务的执行顺序，并且每个任务的输出可以作为下一个任务的输入。这种机制非常适合处理具有依赖关系的任务序列。

特点

1. **顺序执行**：SequentialChain中的任务按照用户定义的顺序依次执行，确保数据按照预期的方式流动。
2. **灵活组合**：用户可以根据需要自由组合不同的Chain，形成复杂的处理流程。
3. **可扩展性**：SequentialChain的设计允许用户轻松地添加新的任务或修改现有任务的顺序。
4. **数据传递**：SequentialChain支持任务之间的数据传递，即一个任务的输出可以作为下一个任务的输入。

类型

- **SimpleSequentialChain**：这是SequentialChain的最简单形式，其中每个步骤都具有单一输入/输出，并且一个步骤的输出是下一个步骤的输入。
- **SequentialChain**：更通用形式的顺序链，允许多个输入/输出，可以处理更复杂的场景。

使用场景

- **文本处理**：例如，将一个长文本首先进行文本清洗，然后进行情感分析，最后生成摘要。这三个任务可以按照顺序连接成一个SequentialChain。
- **问答系统**：在处理复杂问题时，可以将问题解析、信息检索和答案生成等任务连接成一个SequentialChain，实现自动化的问答功能。

示例

假设我们有一个任务是将用户输入的文本转换为小写，然后统计其中的单词数。这个任务可以分解为两个子任务：文本转小写和单词计数。这两个子任务可以连接成一个SequentialChain：

1. **文本转小写Chain**：接收用户输入的文本作为输入，输出转换为小写后的文本。
2. **单词计数Chain**：接收小写文本作为输入，输出文本中的单词数。

通过将这两个Chain按照顺序连接起来，我们就可以形成一个完整的SequentialChain来处理用户的输入文本了。

总之，SequentialChain是LangChain库中一个非常强大的工具，它允许用户将多个任务连接成一个处理流程，并按照特定的顺序执行这些任务。这种机制可以大大提高任务的执行效率和准确性。

#### 8.4.2案例

~~~python
from langchain.chains.llm import LLMChain
from langchain_community.llms import Tongyi

llm = Tongyi()

from langchain.prompts import ChatPromptTemplate
from langchain.chains.sequential import SequentialChain

#chain 1 任务：翻译成中文
first_prompt = ChatPromptTemplate.from_template("把下面内容翻译成中文:\n\n{content}")
chain_one = LLMChain(
    llm=llm,
    prompt=first_prompt,
    verbose=True,
    output_key="Chinese_Rview",
)

#chain 2 任务：对翻译后的中文进行总结摘要 input_key是上一个chain的output_key
second_prompt = ChatPromptTemplate.from_template("用一句话总结下面内容:\n\n{Chinese_Rview}")
chain_two = LLMChain(
    llm=llm,
    prompt=second_prompt,
    # verbose=True,
    output_key="Chinese_Summary",
)

#chain 3 任务:智能识别语言 input_key是上一个chain的output_key
third_prompt = ChatPromptTemplate.from_template("根据下面内容写5条评价信息:\n\n{Chinese_Summary}")
chain_three = LLMChain(
    llm=llm,
    prompt=third_prompt,
    # verbose=True,
    output_key="Language",
)

#chain 4 任务:针对摘要使用指定语言进行评论 input_key是上一个chain的output_key   
fourth_prompt = ChatPromptTemplate.from_template("请使用指定的语言对以下内容进行回复:\n\n内容:{Chinese_Summary}\n\n语言:{Language}")
chain_four = LLMChain(
    llm=llm,
    prompt=fourth_prompt,
    verbose=True,
    output_key="Reply",
)

#overall 任务：翻译成中文->对翻译后的中文进行总结摘要->智能识别语言->针对摘要使用指定语言进行评论
overall_chain = SequentialChain(
    chains=[chain_one, chain_two, chain_three, chain_four],
    verbose=True,
    input_variables=["content"],
    output_variables=["Chinese_Rview", "Chinese_Summary", "Language"],
)

content = "I am a student of Cumulus Education, my course is artificial intelligence, I like this course, because I can get a high salary after graduation"
ret = overall_chain.invoke(content)
~~~

### 8.5 RouterChain

#### 8.5.1介绍

RouterChain 是一个特殊的 Chain，它可以根据输入动态选择下一个 Chain。

RouterChain 由两个组件组成:

RouterChain (负责选择下一个要调用的链条)

destination_chains: 路由器链条可以路由到的链条

RouterChain 包括不同类型的路由链条。下面的例子是 MultiPromptChain 中的使用方式，以创建一个问答链条，该链条根据给定的问题选择最相关的提示，并使用该提示回答问题。

RouterChain在LangChain库中扮演着重要的角色，它主要用于实现基于条件判断的路由功能，使得智能体或应用能够根据输入内容动态地选择不同的处理流程。以下是关于RouterChain的详细解释：

定义

RouterChain，也称为分支链，它能够根据输入内容动态地选择并调用下一个链。在智能体的可视化编排流程中，RouterChain扮演着决策中心的角色，通过灵活的意图配置和链连接点，为智能体提供了强大的决策能力。

特点

1. **条件判断**：RouterChain的核心功能是根据输入的提示词或指令进行条件判断，以确定下一步应该调用哪个链。
2. **动态选择**：基于判断结果，RouterChain能够动态地选择一个或多个目标链进行调用，从而实现不同的处理流程。
3. **意图配置**：RouterChain允许用户定制决策逻辑，包括传入对话历史记录、输出关键词等配置项，以满足不同的应用场景需求。
4. **链连接点**：RouterChain具有链输入连接点和链输出连接点，这些连接点是其决策功能的实现基础。链输入连接点允许RouterChain与其他任意链相连，接收输入信息；链输出连接点需要配置意图，每个意图对应一个链输出连接点。

工作原理

1. **输入接收**：RouterChain接收来自用户的输入，该输入可以是文本、语音或其他形式的数据。
2. **条件判断**：根据用户输入的内容，RouterChain会调用内置的AI模型进行条件判断。这些判断可以基于关键词匹配、语义理解等多种算法实现。
3. **目标链选择**：基于判断结果，RouterChain会选择一个或多个目标链进行调用。这些目标链可以是预先定义好的处理流程，也可以是用户自定义的链。
4. **输出传递**：RouterChain将用户输入传递给选定的目标链，并等待目标链的处理结果。一旦目标链处理完成，RouterChain会将结果返回给用户或传递给下一个处理环节。

应用场景

RouterChain在多个领域都有广泛的应用，包括但不限于：

- **智能客服**：在智能客服系统中，RouterChain可以根据用户的问题类型选择不同的回复模板或处理流程，提高客服效率和用户体验。
- **推荐系统**：在推荐系统中，RouterChain可以根据用户的兴趣和行为数据选择不同的推荐算法或模型，实现更精准的个性化推荐。
- **自然语言处理**：在自然语言处理领域，RouterChain可以根据文本内容选择不同的分析器或处理流程，实现更复杂的文本理解和处理任务。

总结

RouterChain是LangChain库中一个重要的组件，它通过条件判断和动态选择机制实现了智能体的决策功能。在实际应用中，RouterChain可以根据不同的输入内容和应用场景灵活配置决策逻辑和链连接点，为智能体提供了强大的决策能力和适应性。

#### 8.5.2案例

~~~python
from langchain.chains.llm import LLMChain
from langchain_community.llms import Tongyi

llm = Tongyi()
from langchain.prompts import PromptTemplate
from langchain.chains.conversation.base import ConversationChain
from langchain.chains.router.llm_router import LLMRouterChain,RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE
from langchain.chains.router import MultiPromptChain

#物理链
physics_template = """您是一位非常聪明的物理教授.\n
您擅长以简洁易懂的方式回答物理问题.\n
当您不知道问题答案的时候，您会坦率承认不知道.\n
下面是一个问题:
{input}"""
physics_prompt = PromptTemplate.from_template(physics_template)

# 物理的任务
physicschain = LLMChain( llm=llm,prompt=physics_prompt)

#数学链
math_template = """您是一位非常优秀的数学教授.\n
您擅长回答数学问题.\n
您之所以如此优秀，是因为您能够将困难问题分解成组成的部分，回答这些部分，然后将它们组合起来，回答更广泛的问题.\n
下面是一个问题:
{input}"""

math_prompt = PromptTemplate.from_template(math_template)

###数学的任务
mathschain = LLMChain(llm=llm, prompt=math_prompt,)

# 默认任务
default_chain = ConversationChain(
    llm = llm,
    output_key="text"
)

# 组合路由任务
destination_chains = {}  
destination_chains["physics"] = physicschain
destination_chains["math"] = mathschain

# 定义路由Chain
router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations="physics:擅长回答物理问题\n math:擅长回答数学问题")
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser()
)
router_chain = LLMRouterChain.from_llm(
    llm,
    router_prompt
)
chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain,
    verbose=True
)
# question = "什么是牛顿第一定律?"
# print(router_chain.invoke(question))
# chain.run(question)

question = "2+2等于几?"
print(router_chain.invoke(question))
print(chain.run("2+2等于几?"))

~~~

### 8.6 TransformChain

#### 8.6.1介绍

通用的转换链。下面的例子是创建一个虚拟转换，它接收一个超长的文本，将文本过滤为仅保留前三个段落，然后将其传递给 LLMChain 进行摘要生成。

TransformChain在LangChain库中是一个重要的组件，主要用于处理chains之间的输入和输出数据，以便于chains之间的数据传输。以下是关于TransformChain的详细解释：

定义

TransformChain是一个框架或工具，它允许用户定义自定义的转换函数，这些函数可以应用于chains之间的数据。这意味着，当数据从一个chain传递到另一个chain时，TransformChain可以提供一个或多个转换步骤，以修改或格式化数据，使其符合下一个chain的输入要求。

特点

1. **自定义转换**：TransformChain支持用户定义自己的转换函数，这些函数可以根据具体需求对输入数据进行处理。
2. **数据处理**：TransformChain的主要作用是对chains之间的数据进行处理，确保数据在传递过程中满足下一个chain的输入要求。
3. **灵活性**：由于支持自定义转换函数，TransformChain具有很高的灵活性，可以适应各种复杂的数据处理场景。

工作原理

- **数据接收**：TransformChain接收来自上一个chain的输出数据。
- **数据转换**：TransformChain应用用户定义的转换函数对接收到的数据进行处理。这些转换函数可以是简单的数据清洗、格式化，也可以是复杂的逻辑处理。
- **数据输出**：经过转换的数据被传递给下一个chain作为输入。

#### 8.6.2案例

~~~python
from langchain.chains.llm import LLMChain
from langchain_community.llms import Tongyi

llm = Tongyi()
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.transform import TransformChain
from langchain.chains.sequential import SimpleSequentialChain



# 第一个任务
def transform_func(inputs:dict) -> dict:
    text = inputs["text"]
    shortened_text = "\n".join(text.split("\n")[:3])
    return {"output_text":shortened_text}

#文档转换链
transform_chain = TransformChain(
    input_variables=["text"],
    output_variables=["output_text"],
    transform=transform_func
)

# 第二个任务
template = """对下面的文字进行总结:
{output_text}

总结:"""

prompt = PromptTemplate(
    input_variables=["output_text"],
    template=template
)
llm_chain = LLMChain(
    llm = Tongyi(),
    prompt=prompt
)

#使用顺序链连接起来
squential_chain = SimpleSequentialChain(
    chains=[transform_chain,llm_chain],
    verbose=True
)

with open("doc/NBA新闻.txt",encoding='utf-8') as f:
    letters = f.read()
squential_chain.invoke(letters)
~~~

### 用户发布模块

~~~
用户发布动态，系统审核，审核通过后显示
百度人工智能平台-》审核
1.vue页面，用户输入发布信息
2.获取到发布信息-》调用百度人工智能平台敏感词过滤
3.对敏词处理-》写入发布表，审核状态（1没审核  2通过  3通过）
4.显示页面

qps限制问题
1.百度企业账号qps 10，
2.队列解决 redis list
3.把任务放到队列中
4.celery启一个定时任务，每秒执行一次，一次取10个处理，处理完异步更新到数据库
~~~

![image-20241009162804435](images/image-20241009162804435.png)

百度开放平台注册

https://qianfan.cloud.baidu.com/?track=56a2658099dba724c98ea24abdff90718ec8ffb931f2295f

创建应用

https://console.bce.baidu.com/ai/?_=1728455908238#/ai/antiporn/app/list

百度api封装

~~~python
import requests,json
class BDapi():
    def __init__(self) -> None:
        self.API_KEY = "tDGnh7BmUWauc0xocyfmG4qS"
        self.SECRET_KEY = "onMC9tZvQwrxdM2Dv1iEnTzeLsIC7ivS"
    def get_access_token(self):
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        """
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": self.API_KEY, "client_secret": self.SECRET_KEY}
        return str(requests.post(url, params=params).json().get("access_token"))
    
    def audit_mes(self,mes):
        url = "https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined?access_token=" + self.get_access_token()
        
        payload='text='+mes
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
       
        if data['conclusion'] == '合规':
            return mes
        else:
            return "内容不合法"
        
bdapi = BDapi()
~~~

代码实现

~~~python
from tools.bdapi import bdapi
from langchain.chains.llm import LLMChain
from langchain_community.llms import Tongyi

llm = Tongyi()
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.transform import TransformChain
from langchain.chains.sequential import SimpleSequentialChain


 # 第一个任务
def transform_func(inputs:dict) -> dict:
    text = inputs["text"]
    mes=bdapi.audit_mes(text)
    return {"output_text":mes}
               
class TestBd(APIView):
    def get(self,request):
        mes = request.GET.get('mes')

        #文档转换链
        transform_chain = TransformChain(
            input_variables=["text"],
            output_variables=["output_text"],
            transform=transform_func
        )

        # 第二个任务
        template = """对下面的文字进行处理:
        如果内容为内容不合法直接返回这几个字，如果是别的
        内容请对内容做优化处理后返回,返回时只返回内容不返回描述信息,内容为
        {output_text}

        # # """
        # template = """对下面的文字进行总结:
        # {output_text}

        # 总结:"""

        prompt = PromptTemplate(
            input_variables=["output_text"],
            template=template
        )
        llm_chain = LLMChain(
            llm = Tongyi(),
            prompt=prompt
        )

        #使用顺序链连接起来
        squential_chain = SimpleSequentialChain(
            chains=[transform_chain,llm_chain],
            verbose=True
        )

        res = squential_chain.invoke(mes)
        return Response({"code":200,'data':res})
~~~

qps限制问题

~~~
每秒能处理的请求数
5qps，20qps
队列、锁
队列：每个请求都不一样，都需要处理，用队列解决,数据结构，先进先出
锁：所有用户的请求返回的结果是一样的
队列：异步、削峰、解耦
问题：任务重复消费、任务丢失
~~~

实现步骤

~~~
1.接口中获取到发布内容，发布内容存入队列中，写入发布表，审核状态为1（等待审核）
2.celery定时任务，每秒执行一次从队列中读取5条数据处理，调用百度接口，根据结果做业务操作，更新表的状态

~~~

celery配制

### 1.celery介绍

~~~
celery是一个异步任务框架，没有队列。redis,rabbitmq

task  产生任务     
beat  定时任务配制
broker  任务调用器，将任务放入队列
worker  监听队列变化，执行任务
backend  将任务结果存入到结果队列中
~~~

<img src="images/26.png">

~~~
list1=[4,5,6,7,8]

list2=[7,8]
1,2,3

4
更新订单表
查询 4对应的订单的状态
update set status=2
更新积分
del
~~~

~~~
pip uninstall celery
pip intall -U celery
~~~

2.在settings中配制

~~~python
# Celery配置
# from kombu import Exchange, Queue
# 设置任务接受的类型，默认是{'json'}
CELERY_ACCEPT_CONTENT = ['application/json']
# 设置task任务序列列化为json
CELERY_TASK_SERIALIZER = 'json'
# 请任务接受后存储时的类型
CELERY_RESULT_SERIALIZER = 'json'
# 时间格式化为中国时间
CELERY_TIMEZONE = 'Asia/Shanghai'
# 是否使用UTC时间
CELERY_ENABLE_UTC = False
# 指定borker为redis 如果指定rabbitmq CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
# 指定存储结果的地方，支持使用rpc、数据库、redis等等，具体可参考文档 # CELERY_RESULT_BACKEND = 'db+mysql://scott:tiger@localhost/foo' # mysql 作为后端数据库
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
# 设置任务过期时间 默认是一天，为None或0 表示永不过期
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# 设置worker并发数，默认是cpu核心数
# CELERYD_CONCURRENCY = 12
# 设置每个worker最大任务数
CELERYD_MAX_TASKS_PER_CHILD = 100


# 指定任务的位置
CELERY_IMPORTS = (
    'base.tasks',
)
# 使用beat启动Celery定时任务
# schedule时间的具体设定参考：https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html
CELERYBEAT_SCHEDULE = {
    'getbaidu-1-seconds': {
        'task': 'base.tasks.getbaidu',
        'schedule': 1,
        
    },
   'getbaidu-1-seconds': {
        'task': 'base.tasks.getbaidu',
        'schedule': 3,
        
    },
}

~~~

在settings同级目录下新celery.py

~~~python
# from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mall.settings')
app = Celery('mall',broker='redis://127.0.0.1:6379/1',  # 任务存放的地方 
             backend='redis://127.0.0.1:6379/15')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

platforms.C_FORCE_ROOT = True


~~~

在settings同级目录__init__.py中

~~~python
# from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)

~~~

在项目目录下创建base文件夹，在base下新建tasks.py文件

~~~
# from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time
from tools.mredis import mredis
from tools.bdapi import bdapi
# 1导入prompt的类
from langchain.prompts import PromptTemplate
# 导入通义大模型
from langchain_community.llms import Tongyi

@shared_task
def getbaidu():
   print("调用百度api接口")
   #每秒执行一次从队列中读取5条数据处理，调用百度接口，根据结果做业务操作，更新表的状态
   ids = mredis.list_lrange('dblist',0,4)
   for i in ids:
       print(i)
       code = i.decode()
       publish = Publish.objects.filter(id=code).first()
       res = bdapi.audit_mes(publish.content)
       if res == '1':
           Publish.objects.filter(id=code).update(status=3)
       else:
            # 定义一个模板
            pp = "对文章{mes}进行优化处理"
            # 实例化模板类
            promptTemplate = PromptTemplate.from_template(pp)
            # 生成prompt
            prompt = promptTemplate.format(mes=publish.content)

            # 实例化通义大模型
            tongyi = Tongyi()
            ret = tongyi.invoke(prompt)
            Publish.objects.filter(id=code).update(status=2,content=ret)
        mredis.list_lrem('dblist',code)
       
       


~~~

启动任务

~~~
启动worker
celery -A llmpro  worker -l info

windows下启动 worker
celery -A mall  worker -l info -P eventlet 
启动定时beat
celery -A medical beat -l info 
~~~



### 8.7 四种文档处理链

####  8.7.1 StuffDocumentsChain

这种链最简单直接，是将所有获取到的文档作为 context 放入到 Prompt 中，传递到 LLM 获取答案。这种方式可以完整的保留上下文，调用 LLM 的次数也比较少，建议能使用 stuff 的就使用这种方式。其适合文档拆分的比较小，一次获取文档比较少的场景，不然容易超过 token 的限制。

StuffDocumentsChain在LangChain框架中是一个用于处理文档的关键组件，它主要用于将多个文档组装成一个提示（prompt），并将这个提示传递给大模型（LLM）。以下是关于StuffDocumentsChain的详细解释：

1. 作用
   - StuffDocumentsChain的主要作用是将多个文档的内容整合到一个单一的提示中，然后将其传递给大模型。这样做可以确保需要的信息都被传递，进而从大模型中获取所需的上下文和响应。
2. 使用场景
   - 当需要处理多个文档，并且这些文档的内容需要一起作为输入传递给大模型时，可以使用StuffDocumentsChain。例如，在处理一个包含多篇相关文章的文档集合，并希望将这些文章的内容作为一个整体输入给大模型进行摘要、问答等任务时。
3. 优点
   - 简单易用：StuffDocumentsChain提供了一种简单的方式，将多个文档的内容合并成一个提示，从而简化了与大模型的交互。
   - 保持上下文完整性：通过将多个文档的内容整合到一个提示中，可以确保大模型在处理时能够考虑到这些文档之间的上下文关系。
4. 注意事项
   - 当文档的数量或长度非常大时，可能会超出大模型的上下文窗口限制，导致信息丢失或模型性能下降。因此，在使用StuffDocumentsChain时，需要注意文档的数量和长度，并考虑是否需要进行适当的分割或简化。
5. 与其他组件的协同
   - StuffDocumentsChain通常与其他LangChain组件一起使用，如LLM（大模型）加载器、文档加载器等，以构建一个完整的文档处理流程。例如，可以使用文档加载器从外部数据源加载文档，然后使用StuffDocumentsChain将文档整合成提示，最后传递给大模型进行处理。

综上所述，StuffDocumentsChain是LangChain框架中一个重要的文档处理组件，它通过将多个文档的内容整合到一个提示中，并传递给大模型，从而简化了与大模型的交互，并保持了上下文的完整性。

代码实现

~~~python
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader,TextLoader
from langchain.text_splitter import CharacterTextSplitter

# 1 定义prompt模板
prompt_template = """对以下文字做简洁的总结:
{text}
简洁的总结:"""
prompt = PromptTemplate.from_template(prompt_template)

# 2 定义任务
llm_chain = LLMChain(llm=llm, prompt=prompt)

# 3、定义chain
stuff_chain = StuffDocumentsChain(
    llm_chain=llm_chain,
    document_variable_name="text",
)

# loader = PyPDFLoader("doc/demo.pdf")
loader = TextLoader("doc/NBA新闻.txt",encoding='utf-8')
docs = loader.load()

# split = CharacterTextSplitter("\n",chunk_size = 200)
# text = split.split_documents(docs)

print(stuff_chain.run(docs))
~~~

#### 8.7.2 RefineDocumentsChain

通过迭代更新的方式获取答案。先处理第一个文档，作为 context 传递给 llm，获取中间结果 intermediate answer。然后将第一个文档的中间结果以及第二个文档发给 llm 进行处理，后续的文档类似处理。Refine 这种方式能部分保留上下文，以及 token 的使用能控制在一定范围。

RefineDocumentsChain是LangChain框架中的一个重要组件，它用于顺序地处理多个文档，并通过迭代的方式改进生成的答案。以下是关于RefineDocumentsChain的详细解释：

1. 基本概念

- **作用**：RefineDocumentsChain的主要作用是基于第一个文档生成初始答案，然后循环处理其余文档以改进该答案。它鼓励在多个文档之间进行信息传递，以产生更准确和完整的回答。
- **使用场景**：当需要处理多个文档，并且希望生成的答案能够综合所有文档的信息时，可以使用RefineDocumentsChain。例如，在问答系统中，当用户的问题涉及多个文档时，可以使用RefineDocumentsChain来生成一个综合所有文档信息的答案。

2. 工作原理

- **顺序处理**：RefineDocumentsChain按照顺序处理文档，首先基于第一个文档生成初始答案。
- **迭代改进**：然后，它循环处理其余文档，每次使用当前文档的内容和之前生成的答案作为上下文，生成一个新的答案。这个过程不断迭代，直到处理完所有文档。
- **信息传递**：RefineDocumentsChain鼓励在多个文档之间进行信息传递。这意味着，在处理一个文档时，它会考虑之前文档的内容和处理结果，以确保生成的答案能够综合所有文档的信息。

3. 优点

- **准确性**：由于RefineDocumentsChain能够综合多个文档的信息，因此生成的答案通常更准确和全面。
- **可解释性**：由于RefineDocumentsChain的处理过程是顺序和可迭代的，因此可以更容易地理解和解释生成的答案是如何从多个文档中得出的。

4. 注意事项

- **文档数量**：虽然RefineDocumentsChain可以处理多个文档，但当文档数量非常大时，处理时间可能会增加。因此，在实际应用中需要根据具体情况考虑是否需要对文档进行筛选或合并。
- **上下文窗口限制**：与所有基于大模型的方法一样，RefineDocumentsChain也受到大模型上下文窗口的限制。如果文档的总长度超过了模型的上下文窗口大小，可能需要考虑对文档进行分割或选择更合适的方法来处理。

5. 示例

假设有一个问答系统，用户的问题涉及三个文档A、B和C。使用RefineDocumentsChain处理这些文档时，首先基于文档A生成初始答案。然后，在处理文档B时，会将文档B的内容和之前生成的答案作为上下文，生成一个新的答案。最后，在处理文档C时，同样会将文档C的内容和之前生成的答案作为上下文，生成最终的答案。这样，最终的答案就能够综合文档A、B和C的信息。

代码实现

~~~python
from langchain.chains.combine_documents.refine import RefineDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms.tongyi import Tongyi
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

# 加载问答
# loader = PyPDFLoader("doc/demo.pdf")
loader = TextLoader("doc/NBA新闻.txt",encoding='utf-8')
docs = loader.load()

#split
text_splitter = CharacterTextSplitter(separator="\n",chunk_size=400, chunk_overlap=0)
split_docs = text_splitter.split_documents(docs)

prompt_template = """对以下文字做简洁的总结:
{text}
简洁的总结:"""

prompt = PromptTemplate.from_template(prompt_template)

refine_template = (
    "你的任务是产生最终摘要\n"
    "我们已经提供了一个到某个特定点的现有回答:{existing_answer}\n"
    "我们有机会通过下面的一些更多上下文来完善现有的回答(仅在需要时使用).\n"
    "------------\n"
    "{text}\n"
    "------------\n"
    "根据新的上下文，用中文完善原始回答.\n"
    "如果上下文没有用处，返回原始回答。"
)

refine_prompt = PromptTemplate.from_template(refine_template)

chain = load_summarize_chain(
    llm=llm,
    chain_type="refine",
    question_prompt=prompt,
    refine_prompt = refine_prompt,
    return_intermediate_steps=True,
    input_key = "documents",
    output_key = "output_text",
)
result = chain.invoke({"documents":split_docs})
print(result)
print(result["output_text"])
print("\n\n".join(result["intermediate_steps"][:3]))
~~~

#### 8.7.3 MapReduceDocumentsChain

先通过 LLM 对每个 document 进行处理，然后将所有文档的答案在通过 LLM 进行合并处理，得到最终的结果。

MapReduce 的方式将每个 document 单独处理，可以并发进行调用。但是每个文档之间缺少上下文。

MapReduceDocumentsChain是LangChain框架中的一个组件，它结合了MapReduce的思想来处理文档数据。以下是关于MapReduceDocumentsChain的详细解释：

1. 基本概念

- **作用**：MapReduceDocumentsChain主要用于处理大规模的文档数据。它首先通过Map操作将每个文档传递给大语言模型（LLM），然后利用Reduce操作对处理后的文档进行简化和聚合。
- **使用场景**：当需要处理大量文档，并且文档之间可以并行处理时，MapReduceDocumentsChain是一个有效的选择。它适用于文档数量众多，且可以分割成多个独立部分进行并行计算的情况。

2. 工作原理

- Map阶段

  ：

  - 将输入的文档集合分割成多个块（blocks），每个块可以并行处理。
  - 将每个文档块传递给LLM进行处理，提取关键信息或生成初步结果。

- Reduce阶段

  ：

  - 收集Map阶段生成的所有初步结果。
  - 使用ReduceDocumentsChain或其他组件对初步结果进行简化、聚合或进一步处理。
  - 最终生成一个综合了所有文档信息的输出。

3. 优点

- **并行处理**：MapReduceDocumentsChain利用MapReduce的并行处理特性，可以显著提高处理大规模文档数据的效率。
- **简化文档**：通过ReduceDocumentsChain的简化操作，可以将复杂的文档数据简化为更易于理解和处理的格式。
- **灵活性**：MapReduceDocumentsChain可以与其他LangChain组件结合使用，构建出更复杂、更强大的文档处理流程。

4. 注意事项

- **文档数量**：虽然MapReduceDocumentsChain适用于处理大量文档，但当文档数量过于庞大时，可能需要考虑更高效的分割和并行处理策略。
- **上下文窗口限制**：由于LLM的上下文窗口限制，对于过长的文档或文档集合，可能需要采取分块处理或其他策略来避免信息丢失。

5. 与其他组件的协同

- **LLM**：MapReduceDocumentsChain依赖于LLM进行文档处理。LLM的选择和配置将直接影响MapReduceDocumentsChain的性能和效果。
- **ReduceDocumentsChain**：MapReduceDocumentsChain的Reduce阶段通常使用ReduceDocumentsChain或其他组件来简化和聚合初步结果。这些组件的选择和配置将影响最终输出的质量和准确性。

总之，MapReduceDocumentsChain是一个强大的文档处理组件，它结合了MapReduce的并行处理特性和LangChain的文档处理能力，适用于处理大规模、复杂的文档数据。

案例

~~~python
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.combine_documents.reduce import ReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
from langchain.chains.llm import LLMChain
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

#load pdf
# loader = PyPDFLoader("doc/demo.pdf")
loader = TextLoader("doc/NBA新闻.txt",encoding='utf-8')
docs = loader.load()

text_splitter = CharacterTextSplitter(separator="\n",chunk_size=400, chunk_overlap=0)
split_docs = text_splitter.split_documents(docs)

#map chain
map_template = """对以下文字做简洁的总结:
"{content}"
简洁的总结:"""
map_prompt = PromptTemplate.from_template(map_template)

# 定义任务
map_chain = LLMChain(
    llm=llm, #llm
    prompt=map_prompt,
)

#reduce chain
reduce_template = """以下是一个摘要集合:
{doc_summaries}
将上述摘要与所有关键细节进行总结.
总结:"""
reduce_prompt = PromptTemplate.from_template(reduce_template)

# 定义reduce任务
reduce_chain = LLMChain(
    prompt=reduce_prompt,
    llm=llm,
)

# stuff chain
stuff_chain = StuffDocumentsChain(
    llm_chain=reduce_chain,
    document_variable_name="doc_summaries",
)

# reduce chain
reduce_final_chain = ReduceDocumentsChain(
    combine_documents_chain=stuff_chain,
    #超过4000个token就会切入到下一个stuff_chain
    collapse_documents_chain=stuff_chain,
    token_max=4000,
)

# map reduce chain
map_reduce_chain = MapReduceDocumentsChain(
    llm_chain=map_chain,
    document_variable_name="content",
    reduce_documents_chain=reduce_final_chain,
)

# 默认使用了hugging face上的 GPT-2 模型，下载有问题会报错

summary = map_reduce_chain.invoke(split_docs)
print(summary)
~~~

#### 8.7.4 MapRerankDocumentsChain

MapRerankDocumentsChain 和 MapReduceDocumentsChain 类似，先通过 LLM 对每个 document 进行处理，每个答案都会返回一个 score，最后选择 score 最高的答案。MapRerank 和 MapReduce 类似，会大批量的调用 LLM，每个 document 之间是独立处理。

~~~python
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain_community.document_loaders import TextLoader
from langchain.chains.combine_documents.reduce import ReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
from langchain.chains.llm import LLMChain
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

#load
# loader = PyPDFLoader("doc/demo.pdf")

loader = TextLoader("doc/NBA新闻.txt",encoding='utf-8')
docs = loader.load()
#split
text_splitter = CharacterTextSplitter(separator="\n",chunk_size=200, chunk_overlap=0)
split_docs = text_splitter.split_documents(docs)

chain = load_qa_with_sources_chain(
    llm, 
    chain_type="map_rerank", 
    metadata_keys=['source'], 
    return_intermediate_steps=True
)
print(chain)
query = "中文回答这篇文章的主要内容是什么？"
result = chain.invoke({"input_documents":split_docs,"question":query})
result
~~~

#### 8.7.5 自定义链

当通用链不满足的时候，可以自行构建来实现特定的目的。

~~~python
from typing import List, Dict, Any, Optional
from langchain.callbacks.manager import CallbackManagerForChainRun
from langchain.chains.base import  Chain
from langchain.prompts.base import BasePromptTemplate
from langchain.base_language import  BaseLanguageModel

class wiki_article_chain(Chain):
    """开发一个wiki文章生成器"""
    prompt:BasePromptTemplate
    llm:BaseLanguageModel
    out_key:str="text"

    @property
    def input_keys(self) -> List[str]:
        """将返回Prompt所需的所有键"""
        return self.prompt.input_variables
    
    @property
    def output_keys(self) -> List[str]:
        """将始终返回text键"""
        return [self.out_key]
    
    def _call(
        self,
        inputs:Dict[str,Any],
        run_manager:Optional[CallbackManagerForChainRun]=None,
    ) -> Dict[str,Any]:
        """运行链"""
        prompt_value = self.prompt.format_prompt(**inputs)
        #print("prompt_value:",prompt_value)
        response = self.llm.generate_prompt(
            [prompt_value],callbacks=run_manager.get_child() if run_manager else None
        )
        #print("response:",response)
        if run_manager:
            run_manager.on_text("wiki article is written")
        return {self.out_key:response.generations[0][0].text}
    
    @property
    def _chain_type(self) -> str:
        """链类型"""
        return "wiki_article_chain"
        
        
from langchain_community.llms.tongyi import Tongyi
from langchain.prompts import  PromptTemplate

prompt=PromptTemplate(
    template="写一篇关于{topic}的维基百科形式的文章",
    input_variables=["topic"]
)

chain = wiki_article_chain(
    llm = llm,
    prompt = prompt
)


~~~

### 8.8 Memory

#### 8.8.1 memory介绍

默认情况下，Chains（链）和Agents（代理）是无状态的，这意味着它们将每个传入的查询视为独立的（底层的LLM和聊天模型也是如此）。在某些应用程序中（聊天机器人就是一个很好的例子），记住先前的交互非常重要，无论是短期还是长期。Memory（记忆）正是为此而设计的。 LangChain提供两种形式的记忆组件。首先，LangChain提供了用于管理和操作先前聊天消息的辅助工具。无论如何使用，这些工具都被设计为模块化和有用。其次，LangChain提供了将这些工具轻松整合到链中的方法。

通常情况下，对于每种类型的记忆，有两种理解使用记忆的方法。一种是独立的函数，从一系列消息中提取信息，另一种是在链中使用这种类型的记忆的方法。

记忆可以返回多个信息（例如，最近的 N 条消息和所有先前消息的摘要）。返回的信息可以是字符串或消息列表。

ChatMessageHistory

在大多数（如果不是全部）记忆模块的核心实用类之一是 `ChatMessageHistory` 类。这是一个超轻量级的包装器，提供了保存人类消息、AI 消息以及获取所有消息的便捷方法。

如果您在链外管理记忆，则可以直接使用此类。

```python

from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()
history.add_user_message("你好")
history.add_ai_message("你好?")
history.add_user_message("请问丹麦的首都是哪里?")
history.add_ai_message("哥本哈根")
```

ConversationBufferMemory

现在我们展示如何在链中使用这个简单的概念。首先展示 `ConversationBufferMemory`，它只是一个对 ChatMessageHistory 的包装器，用于提取消息到一个变量中。

我们可以首先将其提取为一个字符串。

```python
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("hi!")
memory.chat_memory.add_ai_message("whats up?")
memory.load_memory_variables({})

```

我们还可以将历史记录作为消息列表获取。

```python
memory = ConversationBufferMemory(return_messages=True)
memory.chat_memory.add_user_message("hi!")
memory.chat_memory.add_ai_message("whats up?")
memory.load_memory_variables({})
  
```

保存消息记录

您可能经常需要保存消息，并在以后使用时加载它们。可以通过将消息首先转换为普通的 Python 字典来轻松实现此操作，然后将其保存（例如，保存为 JSON 格式），然后再加载。以下是一个示例：

```python
import json

from langchain.memory import ChatMessageHistory
from langchain.schema import messages_from_dict, messages_to_dict

history = ChatMessageHistory()

history.add_user_message("hi!")

history.add_ai_message("whats up?")
dicts = messages_to_dict(history.messages)

new_messages = messages_from_dict(dicts)
new_messages
   
```

在链中使用

最后，让我们看看如何在链中使用这个模块（设置 `verbose=True` 以便查看提示）。

```python
from langchain_community.llms import Tongyi
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("你好，我是小红")
memory.chat_memory.add_ai_message("小红您好，我是一个医生，可以帮助你吗")
memory.chat_memory.add_user_message("我感觉头晕，眼花，不想吃东西怎么办")
# memory.chat_memory.add_ai_message("小红您好，我是一个医生，可以帮助你吗")
memory.load_memory_variables({})


llm = Tongyi(temperature=0)
conversation = ConversationChain(
    llm=llm, 
    # verbose=True, 
    memory=memory
)
conversation.predict(input="我感觉头晕，眼花，不想吃东西怎么办,请你回答时叫我的名字")
```

#### 8.8.2 prompt和memory

~~~python
import random
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# 初始化 ConversationBufferMemory
memory = ConversationBufferMemory()

class MemoryTest(APIView):
    def get(self,request):
        
        llm = Tongyi()

        # 定义 Prompt 模板
        template = """这是一个成语接龙的游戏，用户输入一个成语，ai根据成语的最后一个字再组成一个成语。用户再根据
        ai的成语最后一个字输入成语，如果用户输入错误，提示用户游戏结果
        User: {input}
        AI: """

        prompt = PromptTemplate(input_variables=["history", "input"], template=template)

        # 初始化 LLMChain
        chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
    
        user_input = request.GET.get('mes')
        memory.chat_memory.add_user_message(user_input)
        
        # 将用户输入和 AI 响应添加到对话历史记录中
        res = chain.run(input=user_input)
        memory.chat_memory.add_ai_message(res)
        print(memory)
        return Response({"code":200,'res':res})
~~~

### 综合案例

~~~
需求请你设计一下成语接龙的游戏，用户输入一个成语，ai根据这个成语的最后一个字生成一个新的成语，用户再根据ai成语的最后一个字输入一个新成语。如果输入的是其他问题，先回答用户的问题，回答完用户问题后提醒用户，我们现在在玩成语接龙的游戏，请你出一个新的成语我们开始吧，添加memory记忆功能，所有的输出采用流式输出。vue页面显示完整的聊天内容
~~~

代码实现

~~~vue
<template>
  <div id="app">
    <h1>Server-Sent Events Example</h1>
    <ul>
      <li v-for="(message, index) in messages" :key="index">{{ message }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: []
    };
  },
  mounted() {
    this.connectToSSE();
  },
  methods: {
    connectToSSE() {
      const eventSource = new EventSource('http://localhost:8000/memoryTest/?ask=小米是谁');

      eventSource.onmessage = (event) => {
        this.messages.push(event.data);
       
      };

      eventSource.onerror = (error) => {
        console.error('EventSource failed:', error);
        eventSource.close();
      };
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
~~~

~~~python

def generate_sse_lc(chunks):
   
    for chunk in chunks:
        data = f"data: {chunk}\n\n"
        if chunk:
            yield data.encode('utf-8')
        else:
            print('____________')
            return 'no mes'
            
import random
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# 初始化 ConversationBufferMemory
memory = ConversationBufferMemory()

@require_GET
def qustions_ask(request):
        
        llm = Tongyi()

        # 定义 Prompt 模板
        template = """这是一个成语接龙的游戏，用户输入一个成语，ai根据成语的最后一个字再组成一个成语。用户再根据
        ai的成语最后一个字输入成语，如果用户输入错误，提示用户游戏结果
        User: {input}
        AI: """

        prompt = PromptTemplate(input_variables=["history", "input"], template=template)

        # 初始化 LLMChain
        chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
       
        user_input = request.GET.get('ask')
       
        memory.chat_memory.add_user_message(user_input)
        
        # 将用户输入和 AI 响应添加到对话历史记录中
        res = chain.run(input=user_input)
        memory.chat_memory.add_ai_message(res)
       
       
        chuns = llm.stream(res)
                   
        response = StreamingHttpResponse(
            generate_sse_lc(chuns),
            content_type="text/event-stream",
        )
        response["Cache-Control"] = "no-cache"
        return response
~~~



## **四、本单元知识总结**

```python
1.当日知识点总结1
2.当日知识点总结2

```

