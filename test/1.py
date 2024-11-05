from langchain_community.llms.tongyi import Tongyi
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
import json

# # 初始化语言模型
llm = Tongyi()

# # 工具函数
def submit_request(input: str) -> str:
    # 用户提交一个任务，把任务存在任务列表
    task = json.loads(input)
    #读取出任务的信息生成任务写入任务表，返回任务id
    return "1001"
    
def assign_approver(input: str) -> str:
    # 分配审批者
    print("###"+input)
   

def make_decision(users: list) -> str:
    # 审批者决策
    pass

def update_status(input: str) -> str:
    # 更新状态
    pass


# 定义工具
tools = [
    Tool(name="submit_request", func=submit_request, description="提交请求,返回任务编号"),
    Tool(name="assign_approver", func=assign_approver, description="分配审批者"),
    Tool(name="make_decision", func=make_decision, description="审批者决策"),
    Tool(name="update_status", func=update_status, description="更新状态")
]


# 初始化代理
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# # 查询高价值客户
data = {"id":1001,"title":"张三请假"}
res = agent.invoke("提交请求，请求信息为"+json.dumps(data))
audit = agent.invoke(res['output']+"分配审批者")
print(audit)
