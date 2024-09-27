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
       
    def add(self,chunks,key):
            # 创建向量存储
            db = FAISS.from_documents(chunks, self.cached_embedder)
            #以索引的方式保存
            db.save_local(key)
    def search(self,ask,key,count):
        db = FAISS.load_local(key,self.cached_embedder,allow_dangerous_deserialization=True)
        res = db.similarity_search(ask, k=count)
        return res
    
faissdb = DB()