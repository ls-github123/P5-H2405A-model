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


from langchain_community.llms.tongyi import Tongyi
from langchain_community.chat_models.tongyi import ChatTongyi

llm = Tongyi()
chat = ChatTongyi()

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

res = chain.invoke({"topic": "冰激凌"})
print(res)


