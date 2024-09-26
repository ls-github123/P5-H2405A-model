import re
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
def extract_toc(page_content):
    toc = []
    pattern = re.compile(r'^(#{1,6})\s*(.*)$', re.MULTILINE)
    matches = pattern.findall(page_content)
    
    for match in matches:
        level = len(match[0])
        title = match[1].strip()
        toc.append((level, title))
    
    return toc

class TextLoad():
    def __init__(self) -> None:
        pass
    
    def  md_load(self,path):
        #使用loader来加载markdown文本
        from langchain_community.document_loaders import TextLoader
        loader = TextLoader(path)
        documents = loader.load()
        return extract_toc(documents[0].page_content)
         
    
    def  csv_load(self,path):
        #使用loader来加载cvs文件
        from langchain_community.document_loaders.csv_loader import CSVLoader

        loader = CSVLoader(file_path=path,source_column="Location")
        data = loader.load()
        return data
    
    def json_load(self,path):
        #使用loader来加载json文件
        from langchain_community.document_loaders import JSONLoader

        loader = JSONLoader(
            file_path = path,jq_schema=".template",text_content=True
        )
        data = loader.load()
        return data

def get_docment(obj, filename, *args, **kwargs):
    try:
        filearr = filename.split(".")
        # 获取方法
        method = getattr(obj, filearr[1]+"_load")
        # 调用方法
        return method(*args, **kwargs)
    except AttributeError:
        print(f"Method '{filename}' not found")

load = TextLoad()
# 动态调用方法
filename = "1.md"
filepath = "/Users/hanxiaobai/Downloads/dxb/h2405a/llmpro/tools/1.md"
mes = get_docment(load, filename,filepath)
print(mes)