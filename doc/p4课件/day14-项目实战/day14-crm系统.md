# 第十二单元  rag项目

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

在CRM系统中，Agent利用RAG技术进行客户筛选的具体业务需求可以非常多样化，这取决于企业的实际运营目标和客户的特性。以下是一些常见的业务需求示例，展示了Agent和RAG技术如何协同工作来满足这些需求：

### 1. 客户细分与分层

**需求描述**：企业需要根据客户的购买历史、消费能力、活跃度等因素，将客户细分为不同的群体，以便进行更有针对性的营销策略制定。“高价值客户”、“近期活跃客户”，“高价值客户”推荐价格在1000以上的销量前5名的商品。“近期活跃客户”送优惠卷。

**Agent与RAG应用**：

- Agent识别用户输入的筛选条件，如“高价值客户”、“近期活跃客户”等。
- RAG技术根据这些条件，在CRM数据库中检索相关字段（如购买金额、购买频率、最近登录时间等），并自动筛选出符合条件的客户列表。
- Agent将筛选结果呈现给用户，并可能提供进一步的建议或行动指南，如为这些客户推荐特定的产品或服务。

1.设计表

~~~
用户表
id  mobile 

订单表 （一个月内容订单总金额）
id  userid  money  pay_status  add_time 
登录记录表
userid  login_time
优惠卷表
id  title  man  jian  总数  s_time   e_time

用户优惠卷表
userid  couponid  title  man  jian  总数  s_time   e_time

商品表


~~~

2.写agent，三个tools，一个toos高价值客户推荐商品。第二个tools近期活跃客户送优惠卷。第三个问答走rag流程

~~~
from langchain.agents import initialize_agent,Tool
from langchain_community.llms import Tongyi
from langchain.agents import AgentType
llm = Tongyi()

#查询关于订单的问题
def search_order(input:str)->str:
    #查询订单表上个月1号到今天总价格在10000以上的用户
    #orders  money  userid  add_time  
    #查询商品价格在10000以上并且销量排名前10
    #给用户发邮件


#查询近期活跃
def recommend_product(input:str)->str:
    #查询用户表统计每个用户的总访问次数，排名前10
    #从优惠卷表中随机获取给用户分配
    return "裙子"

#模拟问电商faq
def faq(input:str)->str:
    #查询faiss
    return "7天无理由退货"

tools=[
    Tool(name="search order",func=search_order,
    description = "高价值客户"),
    Tool(name="recommend product",func=recommend_product,
    description = "近期活跃客户"),
    Tool(name="faq",func=faq,
    description = "咨询模crm系统问题用这个工具回答"),
]
agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
res = agent.invoke("查询订单，订单号为1001")
print(res)
~~~

发送邮件功能

1.settings中的配制

~~~

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
#发送邮件的邮箱
EMAIL_HOST_USER = '18210208326@163.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'JZiJ6JbUgzfgt7s3'
#收件人看到的发件人
EMAIL_FROM = 'A公司<18210208326@163.com>'
~~~

2.发送代码

~~~python
from django.core.mail import send_mail  
from llmpro import settings
def send_email_view(mail):  
    subject = '测试邮件主题'  
    message = '这是测试邮件的内容。'  
    from_email = settings.EMAIL_HOST_USER  # 可以是 settings.py 中的 EMAIL_FROM  
    to_email = [mail]  # 收件人邮箱地址列表  
  
    # 发送邮件  
    send_status = send_mail(subject, message, from_email, to_email, fail_silently=False)  
    print(send_status)
    return send_status
    
class CrmManager(APIView):
    def get(self,request):
        # 按客户分组并计算每个客户的总订单金额  
        # now = datetime.now()
        # pre = now - timedelta(days=9)
        # print(pre)
        # cates = Cates.objects.filter(add_time__lt=now,add_time__gt=pre).values('userid').annotate(total_amount=Sum('numbers')).order_by('total_amount')
        # for i in cates:
        #     print(i)
        send_email_view("763005825@qq.com")
        return Response({"code":200}) 

~~~

~~~python
from langchain_community.llms.tongyi import Tongyi
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import json,re

# # 初始化语言模型
llm = Tongyi()

# # 工具函数
def top_users(input: str) -> str:
    # 查询高价值客户
    list1 = [{"id": 3, "name": "王五"}, {"id": 4, "name": "赵六"}]
    return json.dumps(list1)

def active_users(input: str) -> str:
    # 查询近期活跃客户
    return json.dumps([{"id": 3, "name": "王五"}, {"id": 4, "name": "赵六"}])

def send_survey(users: list) -> str:
    # 发送问卷给指定客户
    userlist =json.loads(users)
    for i in userlist:
        print("***")
        print(i['id'])
  
    return "问卷已发送成功"

def collect_responses(input: str) -> str:
    # 收集客户的问卷反馈
    # responses = [{'id': 1, 'name': '张三', 'satisfaction': 4, 'feedback': '服务很好，但价格偏高'}]
    return json.dumps([{'id': 1, 'name': '张三', 'satisfaction': 4, 'feedback': '服务很好，但价格偏高'}])

def analyze_feedback(responses: list) -> str:
    # 使用 RAG 技术分析反馈
    responses_list = json.loads(responses)
   
    feedback_texts = [response["feedback"] for response in responses_list]
    feedback_summary = "\n".join(feedback_texts)
    
    prompt = PromptTemplate(
        input_variables=["feedback_summary"],
        template="请分析以下客户反馈，提取关键信息，包括满意度评分和改进建议:\n{feedback_summary}"
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    analysis = chain.run({"feedback_summary": feedback_summary})
    return analysis

# 定义工具
tools = [
    Tool(name="top users", func=top_users, description="查询高价值客户。根据工具的结果返回json"),
    Tool(name="active users", func=active_users, description="查询近期活跃客户"),
    Tool(name="send survey", func=send_survey, description="发送问卷给指定客户"),
    Tool(name="collect responses", func=collect_responses, description="收集客户的问卷反馈"),
    Tool(name="analyze feedback", func=analyze_feedback, description="分析客户反馈")
]


# 初始化代理
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# # 查询高价值客户
# res = agent.invoke("查询近期活跃客户")
# print(res)

# # 发送问卷
top_users_data = agent.invoke("查询高价值客户")
print(top_users_data)

# 使用正则表达式匹配JSON对象（这里假设JSON对象之间只有一个逗号分隔，且没有空格）  
json_pattern = r'\{.*?\}'  
matches = re.findall(json_pattern, top_users_data['output'])  
  
# 由于匹配到的JSON对象字符串是独立的，我们需要将它们放入一个数组中（用方括号包围）来形成一个有效的JSON字符串  
# 但在这个例子中，我们直接解析每个JSON对象字符串为Python字典  
customer_list = []  
for match in matches:  
    try:  
        # 解析JSON对象字符串为Python字典  
        customer_dict = json.loads(match)  
        # 将字典添加到列表中  
        customer_list.append(customer_dict)  
    except json.JSONDecodeError:  
        # 如果解析失败，可以打印错误信息或进行其他处理  
        print(f"Failed to decode JSON: {match}")  
  
# 输出结果  
print(customer_list)

# send_survey_result = agent.invoke(f"发送问卷给 {top_users_data}")
# # print(send_survey_result)

# # 收集反馈
# responses = agent.invoke("收集客户的问卷反馈")
# print(responses)

# # 分析反馈
# analysis_result = agent.invoke(f"分析客户反馈 {responses}")
# print(analysis_result)
~~~



### 2. 潜在客户挖掘

**需求描述**：企业希望从现有客户中识别出具有潜在购买意向的客户，以便进行精准营销。

**Agent与RAG应用**：

- Agent分析用户输入的潜在客户需求，如“对新产品感兴趣”、“曾咨询过类似产品”等。
- RAG技术在CRM数据库中检索相关记录，如客户的浏览历史（excel pandas读取）、咨询记录、购买意向等。
- Agent结合RAG的检索结果，自动筛选出潜在客户，并可能提供个性化的营销建议
- 图表显示，柱状图显示意向客户

### 3. 客户流失预警

**需求描述**：企业希望提前识别出可能流失的客户，以便采取挽留措施。

**Agent与RAG应用**：

- Agent识别用户输入的流失预警条件，如“长时间未购买”、“购买频率下降”等。
- RAG技术在CRM数据库中检索客户的购买历史、互动记录等，分析客户的活跃度变化。
- Agent根据RAG的检索和分析结果，自动筛选出可能流失的客户，并可能触发预警机制，如发送挽留邮件或安排客服人员跟进。

~~~python
from langchain_community.llms.tongyi import Tongyi
llm = Tongyi()

from langchain.agents import initialize_agent,Tool
from langchain.agents import AgentType

#查询高价值客户用这个工具处理
def top_users(input:str)->str:
    #
    return [{"id":1,"name":"张三"},{"id":2,"name":"abc"}]

#查询近期活跃客户用这个工具处理
def active_users(input:str)->str:
    return [{"id":3,"name":"a"},{"id":4,"name":"b"}]

tools=[
    Tool(name="top users",func=top_users,
    description = "当查询高价值客户用这个工具处理"),
    Tool(name="active users",func=active_users,
    description = "当查询近期活跃客户用这个工具处理"),
]
agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
res = agent.invoke("高价值客户")
print(res) 
~~~

### 4. 客户满意度调查与反馈

**需求描述**：企业希望了解客户对产品和服务的满意度，以便改进服务质量。

**Agent与RAG应用**（虽然这更多涉及文本分析而非筛选，但仍是CRM中的重要环节）：

- Agent可以协助用户设计满意度调查问卷，并自动发送给目标客户群体。
- 客户填写问卷后，Agent利用RAG技术对问卷数据进行文本分析，提取关键信息（如满意度评分、改进建议等）。
- Agent将分析结果呈现给用户，帮助用户了解客户的反馈和需求，以便制定改进措施。



### 5. 定制化报表生成

**需求描述**：企业希望根据特定的筛选条件生成定制化的报表，以便进行业务分析和决策。

**Agent与RAG应用**：

- Agent识别用户输入的报表需求，如“按销售额排序的前10名客户”、“本月新增客户数量”等。
- RAG技术在CRM数据库中检索相关数据，并根据用户的筛选条件进行排序和汇总。
- Agent将检索和汇总的结果以报表的形式呈现给用户，帮助用户快速了解业务状况。

这些业务需求展示了Agent和RAG技术在CRM系统中的广泛应用潜力。通过结合两者的优势，企业可以更加高效地管理客户关系，提升客户满意度和忠诚度，进而实现业务增长和成功。

## **四、本单元知识总结**

```python
1.当日知识点总结1
2.当日知识点总结2

```

