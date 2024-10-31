from abc import ABC, abstractmethod  
  
class Product(ABC):  
    @abstractmethod  
    def geturl(self):  
        pass
    @abstractmethod
    def callback(self):
        pass
  
# 具体产品类  
class Dingding(Product):  
   def __init__(self) -> None:
       self.client_id = "dingqxjco4n5jjtt7ctj"
       self.clientSecret= "cQJnGlcoMmz6Nnv-r0aFEpQAHqiwVK0t4yf1J_9Do8jQP1AV81iVT2M3GXHWLy53",
            
   def geturl(self):  
        redirect_uri = "http://127.0.0.1:8000/user/dingtalkCallback/"
        client_id = self.client_id
        url = "https://login.dingtalk.com/oauth2/auth?redirect_uri=%s&response_type=code&client_id=%s&scope=openid&state=dddd&prompt=consent"%(redirect_uri,client_id)
        return url
   def callback(self):  
        return "使用产品A"  
  
class Weibo(Product):  
   def geturl(self):  
        redirect_uri = "http://127.0.0.1:8000/user/dingtalkCallback/"
        client_id = self.client_id
        url = "https://login.dingtalk.com/oauth2/auth?redirect_uri=%s&response_type=code&client_id=%s&scope=openid&state=dddd&prompt=consent"%(redirect_uri,client_id)
        return 'http://weibo'
   def callback(self):  
        return "使用产品A" 

    
class Weixin(Product):  
    def __init__(self) -> None:
       self.client_id = "dingqxjco4n5jjtt7ctj"
       self.clientSecret= "cQJnGlcoMmz6Nnv-r0aFEpQAHqiwVK0t4yf1J_9Do8jQP1AV81iVT2M3GXHWLy53",
            
    def geturl(self):  
        
        return "http://weixin"
    def callback(self):  
        return "使用产品A" 
    

   
      
 #创建工厂类
class ProductFactory:  
    def create_product(self, product_type):  
        if product_type == "weixin":  
            return Weixin()  
        elif product_type == "dingding":  
            return Dingding()  
        else:  
            raise ValueError("无效的产品类型")  