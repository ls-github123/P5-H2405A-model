from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings.dashscope import DashScopeEmbeddings
from langchain_text_splitters import CharacterTextSplitter

class Fdb():
    def __init__(self) -> None:
        
        # 实例化向量嵌入器
        self.embeddings = DashScopeEmbeddings()
        
        # 初始化缓存存储器
        self.store = LocalFileStore("./cache/")
        
        # 创建缓存支持的嵌入器
        self.cached_embedder = CacheBackedEmbeddings.from_bytes_store( self.embeddings, self.store, namespace=self.embeddings.model)
        
        
    def adddb(self,path,size,overlap,index):
        # 加载文档并将其拆分成片段
        doc = TextLoader(path,encoding='utf-8').load()
        spliter = CharacterTextSplitter("\n",chunk_size=size, chunk_overlap=overlap)
        chunks = spliter.split_documents(doc)
        # 创建向量存储
        db = FAISS.from_documents(chunks, self.cached_embedder)
        # 以索引的方式保存
        db.save_local(index)
        
    def search(self,index,size,input):
        db = FAISS.load_local(index,self.cached_embedder,allow_dangerous_deserialization=True)
        res = db.similarity_search(input, k=size)
        return res

fdb = Fdb()
# fdb.adddb('/Users/hanxiaobai/Downloads/dxb/h2405a/llmpro/static/upload/a.txt',30,0,'abc')
# res = fdb.search('abc',2,'我是谁')
# print(res)