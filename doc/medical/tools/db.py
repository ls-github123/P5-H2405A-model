
# 导入所需的模块和类
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings.dashscope import DashScopeEmbeddings

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings.dashscope import DashScopeEmbeddings


class DB:
    def __init__(self):
        # 实例化向量嵌入器
        self.embeddings = DashScopeEmbeddings()
        
        # 初始化缓存存储器
        self.store = LocalFileStore("./cache/")
        
        # 创建缓存支持的嵌入器
        self.cached_embedder = CacheBackedEmbeddings.from_bytes_store( self.embeddings, self.store, namespace=self.embeddings.model)
        
        print(self.cached_embedder)
        self.db=None
    def add(self,chunks):
            # 创建向量存储
            self.db = FAISS.from_documents(chunks, self.cached_embedder)
    def search(self,ask):
        res = self.db.similarity_search(ask, k=3)
        return res
    
db = DB()
doc = TextLoader("/Users/hanxiaobai/Downloads/dxb/h2402a/medical/tools/doc/1.txt",encoding='utf-8').load()
spliter = CharacterTextSplitter("\n",chunk_size=200, chunk_overlap=0)
chunks = spliter.split_documents(doc)
db.add(chunks)
# print(db.search("2024"))