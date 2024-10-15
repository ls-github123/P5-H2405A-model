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

