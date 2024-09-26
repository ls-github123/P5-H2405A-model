class TextLoad():
    def __init__(self) -> None:
        pass
    
    def md_load(self,url):
        from langchain_community.document_loaders import TextLoader
        loader = TextLoader(url)
        return loader.load()
    
    def csv_load(self,url):
        from langchain_community.document_loaders.csv_loader import CSVLoader

        loader = CSVLoader(file_path=url,source_column="Location")
        data = loader.load()
        return data
    
    def json_load(self,url):
        from langchain_community.document_loaders import JSONLoader

        loader = JSONLoader(
            file_path = url,jq_schema=".template",text_content=True
        )
        data = loader.load()
        return data

obj = TextLoad()   
def getdoc(filepath):
    print(filepath)
    arr = filepath.split(".")
    filename = arr[1]+"_load"
    method = getattr(obj,filename)
    return method(filepath)
