class FileLoad():
    def __init__(self) -> None:
        pass
    
    #使用loader来加载markdown文本
    def markdown_load(self,url):
       
        from langchain_community.document_loaders import TextLoader
        loader = TextLoader(url)
        print(loader.load())
        return loader.load()
    
    #使用loader来加载cvs文件
    def csv_load(self,url):
        from langchain_community.document_loaders.csv_loader import CSVLoader

        loader = CSVLoader(file_path=url,source_column="Location")
        data = loader.load()
        print(data)
        return data
    
    def getdata(self,url,filename):
        #对文件名进行解析，判断后缀是什么调用哪个方法处理
        arr = filename.split('.')
        if arr[1] == 'md':
            return self.markdown_load(url)
        elif arr[1] == 'csv':
            return self.csv_load(url)
        #返回结果
fileload = FileLoad()
# data = fileload.getdata('/Users/hanxiaobai/Downloads/dxb/h2402a/medical/upload/1.md','1.md')
# print(data)