from langchain_community.llms.tongyi import Tongyi
# from langchain.agents import initialize_agent, Tool
# from langchain.agents import AgentType
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# import json

# # 初始化语言模型
llm = Tongyi()

# # 工具函数
# def top_users(input: str) -> str:
#     # 查询高价值客户
#     return json.dumps([{'id': 1, 'name': '张三'},{'id': 2, 'name': '张三222'}])

# def active_users(input: str) -> str:
#     # 查询近期活跃客户
#     return json.dumps([{"id": 3, "name": "王五"}, {"id": 4, "name": "赵六"}])

# def send_survey(users: list) -> str:
#     # 发送问卷给指定客户
#     userlist =json.loads(users)
#     for i in userlist:
#         print("***")
#         print(i['id'])
  
#     return "问卷已发送成功"

# def collect_responses(input: str) -> str:
#     # 收集客户的问卷反馈
#     # responses = [{'id': 1, 'name': '张三', 'satisfaction': 4, 'feedback': '服务很好，但价格偏高'}]
#     return json.dumps([{'id': 1, 'name': '张三', 'satisfaction': 4, 'feedback': '服务很好，但价格偏高'}])

# def analyze_feedback(responses: list) -> str:
#     # 使用 RAG 技术分析反馈
#     responses_list = json.loads(responses)
   
#     feedback_texts = [response["feedback"] for response in responses_list]
#     feedback_summary = "\n".join(feedback_texts)
    
#     prompt = PromptTemplate(
#         input_variables=["feedback_summary"],
#         template="请分析以下客户反馈，提取关键信息，包括满意度评分和改进建议:\n{feedback_summary}"
#     )
    
#     chain = LLMChain(llm=llm, prompt=prompt)
#     analysis = chain.run({"feedback_summary": feedback_summary})
#     return analysis

# # 定义工具
# tools = [
#     Tool(name="top users", func=top_users, description="查询高价值客户,结果直接返回不处理"),
#     Tool(name="active users", func=active_users, description="查询近期活跃客户"),
#     Tool(name="send survey", func=send_survey, description="发送问卷给指定客户"),
#     Tool(name="collect responses", func=collect_responses, description="收集客户的问卷反馈"),
#     Tool(name="analyze feedback", func=analyze_feedback, description="分析客户反馈")
# ]

# # 初始化代理
# agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# # # 查询高价值客户
# # res = agent.invoke("查询高价值客户")
# # print(res)

# # # 发送问卷
# # top_users_data = agent.invoke("查询高价值客户")
# # send_survey_result = agent.invoke(f"发送问卷给 {top_users_data}")
# # print(send_survey_result)

# # 收集反馈
# responses = agent.invoke("收集客户的问卷反馈")
# print(responses)

# # 分析反馈
# analysis_result = agent.invoke(f"分析客户反馈 {responses}")
# print(analysis_result)

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

loader = TextLoader("/Users/hanxiaobai/Downloads/dxb/h2405a/llmpro/static/upload/a.txt",encoding='utf-8')
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