from langchain.agents import initialize_agent, Tool  
# from langchain.agents.agent_toolkits.transformers import TransformersToolkit  
# from langchain.chains import Chain  
from langchain.chains.llm import LLMChain
# from langchain.schemas import AgentExec, AgentAction  
  
# 假设你有一个工具可以获取和更新审批请求的状态  
# class ApprovalTool(Tool):  
#     # def __init__(self, api_client):  
#         # self.api_client = api_client  
  
#     def get_approval_request(self, request_id: str) -> dict:  
#         # 调用你的 API 获取审批请求  
#         print("调用apid")
          
  
#     def update_approval_status(self, request_id: str, status: str, approver: str) -> dict:  
#         # 调用你的 API 更新审批状态  
#         print("更新审批状态")


#查询关于订单的问题
def approval_tool(input:str)->str:
    print("订单号为****:",input)
    if input.strip() == "1001":
        return "订单号为1001的商品已经到达天津"
    return "订单状态：已发货，发货日期:2023-10-01"


#查询关于推荐产品
def approval_tool(input:str)->str:
    return "裙子"
 
approval_tool = [
    Tool(name="approval_tool",func=approval_tool,
    description = "获取审批请求"),
    Tool(name="approval_tool",func=approval_tool,
    description = "更新状态时使用"),
   
] 
  
# 定义 Agent 的行为链  
def create_approval_chain(approval_tool):  
    return LLMChain(  
        [  
            {  
                "function": "get_approval_request",  
                "tool": approval_tool,  
                "inputs": {"request_id": "${input.request_id}"},  
            },  
            {  
                "function": "transformers_toolkit.llm.generate_text",  
                "inputs": {  
                    "prompt": """  
                    审批请求:  
                    {  
                        lambda: approval_tool.get_approval_request("${input.request_id}")["details"]  
                    }  
  
                    请决定批准还是拒绝该请求。  
                    """,  
                    "max_tokens": 50,  
                },  
            },  
            {  
                "function": "update_approval_status",  
                "tool": approval_tool,  
                "inputs": {  
                    "request_id": "${input.request_id}",  
                    "status": "${action.choice}",  # 假设生成文本的输出中包含 "choice" 字段  
                    "approver": "${agent.user_id}",  # 假设有方法获取当前审批者的 ID  
                },  
            },  
        ]  
    )
    
from langchain_community.llms import Tongyi 
llm = Tongyi()   
# 初始化 Agent  
# toolkit = TransformersToolkit(llm_model=llm)  
agent = initialize_agent(  
    llm,
    # toolkit=toolkit,  
    chain=create_approval_chain(approval_tool),  
    action_store=None,  # 你可以配置一个动作存储来跟踪历史动作  
    observation_store=None,  # 你可以配置一个观察存储来跟踪历史观察  
)  

# agent = initialize_agent(tools,llm,agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,memory=memory,verbose=True)
  
# 运行 Agent  
# action = agent.get_action(  
#     AgentExec(  
#         input_data={"request_id": "12345"},  # 假设这是审批请求的 ID  
#     )  
# )  
action = agent.invoke(input_data={"request_id": "12345"})
print(action)