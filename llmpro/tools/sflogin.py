from abc import ABC,abstractmethod

#抽像工厂
class Product(ABC):
    @abstractmethod
    def geturl(self):
        pass
    @abstractmethod
    def callback(self):
        pass


class Dingding(Product):
    def __init__(self) -> None:
        self.api_key = '234234'
        
    
    def geturl(self):
        url = "dingding.com/"
        return url
    
    def callback(self):
        #钉钉操作
        uid='23'
        token='22'
        retoken='222'
        return uid,token,retoken
    



class Weibo(Product):
    def __init__(self) -> None:
        self.api_key = '234234'
        
    
    def geturl(self):
        url = "weibo.com/"
        return url
    
    def callback(self):
        #weibo操作
        uid='23'
        token='22'
        retoken='222'
        return uid,token,retoken
    
    
class Factory():
    def create_factory(self,params):
        if params == 'dingding':
            return Dingding()
        
        elif params == 'weibo':
            return Weibo()
        
        
        
factory = Factory()

