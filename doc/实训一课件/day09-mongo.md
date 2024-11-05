### 1.域名访问

~~~
https://www.jd.com/

域名解析服务器，域名，服务器（43.143.162.69）
域名解析服务器将域名和服务ip进行绑定-》通过域名ip地址-》服务器安装nginx服务，以默认80端口启动-》访问到nginx-》location配制指向服务gunico服务-》gunico代理django服务-》访问首页
     -》location指定html文件
~~~

### 2.docker

~~~
轻量级容器，仓库，镜像、容器
仓库：存放镜像文件
从仓库下载镜像文件，启动容器
~~~

### 3.centos7安装docker

1. 更新系统：

   ~~~
   sudo yum update
   ~~~

2. 添加Docker的稳定版本仓库：

   ~~~
   sudo yum install -y yum-utils
   sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
   ~~~

3. 安装Docker Engine：

   ~~~
   sudo yum install docker-ce docker-ce-cli containerd.io
   ~~~

4. 启动Docker服务：start stop restart

   ~~~
   sudo systemctl start docker
   ~~~

5. 设置Docker开机自启动：

   ~~~
   sudo systemctl enable docker
   ~~~

6. 验证安装是否成功：

   ~~~
   sudo docker run hello-world
   ~~~

   ### 4.docker常用命令

   ~~~
   docker search  镜像名  查找镜像
   docker pull           下载镜像
   docker  run           启动镜像
   docker  ps            查询正在运行的镜像
   docker stop/start/restart     
   docker scp            远程拷贝文件
   docker exec -it 镜像名或id    /bin/bash
   docker images      查看下载镜像
   ~~~

   ### 5.docker安装mongo

   ~~~
   docker search mongo
   docker pull mongo
   #运行容器
   docker run -itd --name mongo -p 27017:27017 mongo --auth 
   #进入容器
   docker exec -it mongo mongosh admin
   #使用admin数据
   #创建用户
   db.createUser({ user:'admin',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'},"readWriteAnyDatabase"]});
   
   #配制权限
   db.auth('admin', '123456')
   ~~~

   

### 1.mongdb

~~~
关系型数据库 （功能）：mysql\sqllite\pgsql,用于数据的收集，表之间关系的，一对一，一对多，多对多
nosql（性能）：redis
向量数据库（检索搜索）：es、faiss

~~~

~~~
MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。

MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。
~~~

### 2.概念解析

| SQL术语/概念 | MongoDB术语/概念 | 解释/说明                           |
| :----------- | :--------------- | :---------------------------------- |
| database     | database         | 数据库                              |
| table        | collection       | 数据库表/集合                       |
| row          | document         | 数据记录行/文档                     |
| column       | field            | 数据字段/域                         |
| index        | index            | 索引                                |
| table joins  |                  | 表连接,MongoDB不支持                |
| primary key  | primary key      | 主键,MongoDB自动将_id字段设置为主键 |

### 3.常见的数据类型

##### 3.1 常见类型

- Object ID： ⽂档ID
- String： 字符串， 最常⽤， 必须是有效的UTF-8
- Boolean： 存储⼀个布尔值， true或false
- Integer： 整数可以是32位或64位， 这取决于服务器
- Double： 存储浮点值
- Arrays： 数组或列表， 多个值存储到⼀个键
- Object： ⽤于嵌⼊式的⽂档， 即⼀个值为⼀个⽂档
- Null： 存储Null值
- Timestamp： 时间戳， 表示从1970-1-1到现在的总秒数
- Date： 存储当前⽇期或时间的UNIX时间格式

3.docker 安装

~~~
docker search mongo
docker pull mongo
#运行容器
docker run -itd --name mongo -p 27017:27017 mongo --auth 
#进入容器
docker exec -it mongo mongosh admin
#使用admin数据
#创建用户
db.createUser({ user:'admin',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'},"readWriteAnyDatabase"]});

#配制权限
db.auth('admin', '123456')
~~~

### 4.常用命令

~~~python
#查看已经存在的数据库
show dbs;
#创建数据库
use 数据库名
#删除数据库
db.dropDatabase()
#查看集合
show collections;
#创建集合
db.createCollection("news")
#删除集合
db.runoob.drop()
#添加数据
db.集合名.insert({'id':1,'title':'12'})
db.集合名.insert({'id':1,'title':'12','name':'sdfsd','content':'233'})
#查询所有
db.集合名.find()
#删除数据
db.集合名.remove({"id":1})
#条件查询
db.集合名.find({"id":1})

~~~

### 5.pymongo

安装

~~~
pip install pymongo
~~~

pymongo连接

~~~
import pymongo
from urllib import parse
username = parse.quote_plus('root')   # 对用户名进行编码
password = parse.quote_plus('123456')  # 对密码进行编码
database = "admin" # 数据库名称
host     = "43.143.162.69"
port     = "27017"
mongo = pymongo.MongoClient('mongodb://%s:%s@%s:%s/%s' % ( username, password, host, port, database))
~~~

数据库操作

~~~
import pymongo

# 数据库连接
mongo = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

# 创建数据库
my_db  = mongo["my_db"] # 没有往集合里面保存文档之前，mongdb不会真正创建集合!

# 查看数据库列表
print(mongo.list_database_names()) # 上面的 my_db 因为没有内容，所以没有被创建的。
~~~

集合操作

~~~
import pymongo

mongo = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
my_db = mongo["my_db"]

my_collection = my_db["news"] # 没有往集合里面保存文档之前，mongdb不会真正创建集合!

# 查看集合列表
print(my_db.list_collection_names())

# 删除集合
my_collection.drop() # 删除成功返回true，如果集合不存在，返回false
~~~

添加

~~~
import pymongo
mongo = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
my_db = mongo["my_db"]
my_collection = my_db["my_collection"]

# 添加一个文档
document = { "name": "xiaoming", "mobile": "13012345678","age":16}
ret = my_collection.insert_one(document)
print(ret.inserted_id) # 返回InsertOneResult对象
# 插入文档时，如果没有指定_id，将自动分配一个唯一的id。

# 添加多个文档
document_list = [
  { "name": "xiaoming", "mobile": "13033345678","age":17},
  { "name": "xiaohong", "mobile": "13044345678","age":18},
  { "name": "xiaohei",  "mobile": "13612345678","age":18},
]
ret = my_collection.insert_many(document_list)

# 打印文档_id值列表:
print(ret.inserted_ids)
~~~

删除

~~~
import pymongo

mongo = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
my_db = mongo["my_db"]
my_collection = my_db["my_collection"]

# 删除一个文档
query = {"name":"xiaoming"}
my_collection.delete_one(query)

# 删除多个文档
query = { "mobile": {"$regex": "^130"} }
ret = my_collection.delete_many(query)
print("删除了%d个文档" % ret.deleted_count)

import pymongo
from urllib.parse import quote_plus

from bson import ObjectId

if __name__ == "__main__":
    username = quote_plus("mofang")
    password = quote_plus("123456")
    # 获取数据库连接对象
    mongo = pymongo.MongoClient(f"mongodb://{username}:{password}@127.0.0.1:27017/mofang")
    mofang = mongo["mofang"]
    user_list = mofang["user_list"]

    """删除文档"""
    query = {"_id": ObjectId("60d925e127bd4b7769251002")}
    ret = user_list.delete_one(query)
    print(ret)
    print(ret.deleted_count)
    """删除多个文档"""
    query = {"name": "xiaolan"}
    ret = user_list.delete_many(query)
    print(ret.deleted_count)
~~~

更新

~~~
import pymongo

mongo = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
my_db = mongo["my_db"]
my_collection = my_db["my_collection"]

# 更新一个文档
query = { "name": "xiaoming" }
data = { "$set": { "age": 18 } }
my_collection.update_one(query, data)

# 更新所有文档
query = { "heigh": {"$regex": "^130"} }
data = { "$set": { "age": 18 } }
my_collection.update_many(query, data)
~~~

查询

~~~
import pymongo

mongo = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
my_db = mongo["my_db"]
my_collection = my_db["my_collection"]

# 查看一个文档
ret = my_collection.find_one()
print(ret)

# 查看所有文档
for document in my_collection.find():
    print(document)

# 查看文档部分字段，find和find_one的第二个参数表示控制字段的显示隐藏，1为显示，0为隐藏
for document in my_collection.find({},{ "_id": 0, "name": 1, "mobile": 1 }):
    print(document)

# 条件查询
query = { "age": 18 }
document_list = my_collection.find(query)
for document in document_list:
    print(document)

# 比较运算符
query = { "age": {"$gt":17} }
document_list = my_collection.find(query)
for document in document_list:
    print(document)

# 排序显示
# 单个字段排序：
#         sort("键", 1) 升序
#         sort("键",-1) 降序

# 多个字段排序：
#       sort([("键1",1),("键2",-1)])
document_list = my_collection.find().sort("age")
for document in document_list:
    print(document)
    
# 限制查询结果数量
document_list = my_collection.find().limit(3)
print(document_list)

# 偏移、跳过
#    skip(int)
document_list = my_collection.find().limit(3).skip(3) # 从第3篇文档开始获取3篇文档
print(document_list)

# 自定义条件函数
document_list = my_collection.find({"$where":"this.age==18"})
print(document_list)
~~~

~~~
select o.create_time,o.status,o.account,od.name,od.count,od.price from orders as o inner join detail as od on o.number=od.order_id where userid=o.userid order by o.create_time desc
~~~

评价系统

爬取数据

电影网站，requests+bs4+xpath 存入mongo

Requests三方平台获取数据

评价模块

~~~
手机详细信息

    好评（100）  中评（30） 差评（10）

    张三：  手机不错    2023-10-01
             小明：是我也买了
                。。。
                    。。。
                       。。。
    李四    不好
    王五    。。。。
                1   2  3  4  5
~~~

表设计 

商品表 （mysql）加三个字段    好评（100）  中评（30） 差评（10）

id  name   price     goods_number

1   商品1   10               100

评价表（mongo）

id  评价唯一编号   用户id   商品id   内容   添加时间   级别（ 1好评  2中评  3差评） pid (默认值0 ，代表是评价，不是0回复)

实现流程

~~~
1.在我的订单中展示商品，在商品信息后面加一个评价按钮
2.点击评价，弹出一个框，在框中输入内容，点击提交
3.在接口中接收数据，userid，评价内容，商品id，调用模型去自动判断是1好评  2中评  3差评。写入mongo
4.在商品详情表中展示评价信息。根据商品id分页读取所有的评价信息

id  userid  gooid  comment    pid  topid
1    1     1       很好        0      0
2    3     1       是不错       1      1
3    4     1      .。。        0      0
4    4     1      .。。        2      1

ids = select * from comment order by pid asc limit 0,10;
data = select * from comment where topid in (ids)


[{},{},{}]
很好
   是不错
       。。。。tree  
id  label  chirlden
[{"id":1,'label':comment,'chirlden':[{'chirlden':[{}]},{}]},{},{}]

def xtree(data):
    if len(data)<=0:
        return data 
    #先把列表解析成字典
    dict = {}
    for i in data:
        id = i['id']
        dict[id] = i
        
    #dict = {"1":{"id":1,'label':'234','pid':''},"2":{"id":2,'label':'234','pid':''}}
    rlist=[]
    #遍历，判断如果是类父类加入列表，如果不是放到父类下
    for j in data:
        pid = j['pid']
        if pid == 0:
            rlist.append(j)
        else:
            if 'chirlden' not in dict[pid]:
                dict[pid]['chirlden']=[]
            dict[pid]['chirlden'].append(j)
    return rlist
~~~





### 帖子模块

~~~
id  title  content  userid  username imgurl  datetime type(1发布  2回复)  pid

1游戏很好玩  张三  2020-10-10   0
2    你有账号吗  李四           1
 3            茜茜革要地        2
 
4 周末去天津旅游                0
       我出去                  4


~~~

~~~
短视频平台
点击视频-》详情页-》
~~~

~~~
首页文章-》查看详情-》
文章标题
文章内容
添加时间

添加评价-》用户点击添加评价-》输入标题，内容

评价列表（分页方式显示评价列表）
    张三    这个谙asdf枯顶起枯    2020-10-01
         李四   村奇才顶起顶起     2020-1-01
    小明   苛顶起奇才厅    2020-01-10
               
~~~



![image-20230904150115387](/Users/hanxiaobai/Library/Application Support/typora-user-images/image-20230904150115387.png)

### 作业

~~~
1.总结mongo,mysql,redis区别
2.docker部署mongo
3.pymongo封装
4.pymongo实现添加评论和回复
5.分页展示所有评论
5.展示所有的评论和回复（无限级数据处理、页面tree）
~~~

