# 导入所需的模块和类
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings.dashscope import DashScopeEmbeddings

from langchain_text_splitters import CharacterTextSplitter
 
# 实例化向量嵌入器
embeddings = DashScopeEmbeddings()
 
# 初始化缓存存储器
store = LocalFileStore("./cache/")
 
# 创建缓存支持的嵌入器
cached_embedder = CacheBackedEmbeddings.from_bytes_store( embeddings, store, namespace=embeddings.model)
 
# 加载文档并将其拆分成片段
doc = TextLoader("./doc/NBA新闻.txt",encoding='utf-8').load()
spliter = CharacterTextSplitter("\n",chunk_size=200, chunk_overlap=0)
chunks = spliter.split_documents(doc)
 # 创建向量存储
db = FAISS.from_documents(chunks, cached_embedder)
res = db.similarity_search("NBA冠军球队是哪个", k=3)
print(res)