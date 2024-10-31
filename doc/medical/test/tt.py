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