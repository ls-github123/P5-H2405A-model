from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain.prompts import StringPromptTemplate
from langchain import SerpAPIWrapper
from langchain.chains import LLMChain
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
    