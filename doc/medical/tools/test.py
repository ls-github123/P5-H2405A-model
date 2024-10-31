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