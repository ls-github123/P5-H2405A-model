### 1.用户中心

实名认证、内容审核

医疗平台中，添加患者（最多5个），实名认证

实现流程

~~~
1.百度开放平台注册一个账号，成为开发者
2.选择服务-》创建应用-》appid、sercret_key、密码
3.在项目中tools文件夹下封装baiduapi类
4.baiduapi类中  
       init参数
       接口1：获取token的方法
       接口：身份证识别接口
       。。。。
       
5.项目中的应用，上传图片到云服务器，调用baiduapi身份识别接口
6.返回给前端，前端显示
       
~~~

队列去解决qps限制问题

~~~
10qps
20qps
队列、锁
~~~

操作流程

~~~
1.百度开放平台注册一个账号，成为开发者
2.选择服务-》创建应用-》appid、sercret_key、密码
3.在项目中tools文件夹下封装baiduapi类
4.baiduapi类中  
       init参数
       接口1：获取token的方法
       接口：身份证识别接口
       。。。。
       
5.项目中的应用，上传图片到云服务器，把图片url存入队列中（redis list  rabbitmq），返回给页面
6.celery启动一个定时任务，每秒执行一次，从队列中读取10个url地址，调用baiduapi身份识别接口，获取到姓名和身份证号，把姓名和身份证号封装成json {"name":"xm","code":"24234"},json.dumps转成字符串存入redis字符串，以url为key,以json为value
6.vue setInterval开启一个定时器，每秒执行一次，调用接口传递参数图片url，接口中接收到图片url，从redis中获取信息，如果存在，json.loads转换返回，如果不存在返回不存在
7.t = setInterval(()=>{
			根据返回的结果判断，如果获取到用户信息，clearInterval(t)
})
~~~

Baiduapi.py

~~~

import requests,json
class BaiduApi():
    def __init__(self):
        self.API_KEY = "pUuuJK4QPnSL3JJHLVB1aRZ5"
        self.SECRET_KEY = "rv6oVtOXgjbNioRQSRJWk5dF9CbzZotV"


    def get_access_token(self):
        """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": self.API_KEY, "client_secret": self.SECRET_KEY}
        return str(requests.post(url, params=params).json().get("access_token"))

    #身份证验证
    def idcard(self,picurl):
        
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard?access_token=" + self.get_access_token()
    
        # image 可以通过 get_file_content_as_base64("C:\fakepath\1.png",True) 方法获取
        payload='id_card_side=front&url=%s&detect_ps=false&detect_risk=false&detect_quality=false&detect_photo=false&detect_card=false&detect_direction=false'%(picurl)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response

    #文字识别
    def fontmessage(self,picurl):
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + self.get_access_token()
    
        payload='url=%s&detect_direction=false&paragraph=false&probability=false'%(picurl)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        name = data['words_result'][0]['words']
        code = data['words_result'][1]['words']
        return {"name":name,'code':code}

bdapi = BaiduApi()
# data = bdapi.fontmessage("http://shfc1pnzg.hb-bkt.clouddn.com/1.png")
# print(data)
    
~~~

myredis.py

~~~

from redis import Redis, ConnectionPool

class Mredis():
    def __init__(self):
        self.pool = ConnectionPool(host='localhost', port=6379, db=0)
        self.r = Redis(connection_pool=self.pool)
        # self.r = Redis(host='124.71.227.70',port=6379)

    #字符串 添加  获取  删除  自增  自减 
    def set_str(self,key,value):
        return self.r.set(key,value)

    #times单位为秒
    def setex_str(self,key,times,value):
        return self.r.setex(key,times,value)
    
    def setnx_str(self,key,value):
        return self.r.setnx(key,value)
    
    def str_incr(self,key,value):
        return self.r.incr(key,value)

    def get_str(self,key):
        value = self.r.get(key)
        if value:
            value = value.decode()
        return value


    #加
    def incr_str(self,key,count):
        return self.r.incr(key,count)

    def decr_str(self,key,count):
        return self.r.decr(key,count)
    def str_del(self,key):
        return self.r.delete(key)


    #hash,添加
    def hash_add(self,key,field,value):
        return self.r.hset(key,field,value)

    #获取对象的所有属性
    def hash_getall(self,key):
        return self.r.hgetall(key)
    #获取对象的某个属性的值
    def hash_getone(self,key,field):
        return self.r.hget(key,field)
    #删除对象的某个属性
    def hash_hdel(self,key,field):
        return self.r.hdel(key,field)
    #模糊查询
    def get_key(self,key):
        return self.r.keys(key)

    #list
    def list_push(self,key,value):
        return self.r.rpush(key,value)

    def list_pop(self,key):
        return self.r.lpop(key)

    def list_lrange(self,key,min,max):
        return self.r.lrange(key,min,max)

    def list_len(self,key):
        return self.r.llen(key)

    def list_del(self,key,field):
        return self.r.lrem(key,-1,field)

    def list_rpoplpush(self,list1,list2):
        return self.r.rpoplpush(list1,list2)

    #zset
    def zset_zadd(self,key,score,value):
        map={value:score}
        return self.r.zadd(key,mapping=map)

    def zset_zrem(self,key,value):
        return self.r.zrem(key,value)

    def zset_zrangebyscore(self,key,min,max):
        return self.r.zrangebyscore(key,min,max)


    #原子性操作的方法
# import time
r = Mredis()
~~~

