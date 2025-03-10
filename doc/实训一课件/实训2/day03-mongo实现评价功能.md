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
db.集合名.insert({'id':1,'title':'12','name':'sdfsd'})
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

my_collection = my_db["my_collection"] # 没有往集合里面保存文档之前，mongdb不会真正创建集合!

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
query = { "mobile": {"$regex": "^130"} }
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

评价

~~~
视频详页面
id videoid  userid  title  add_time  pid
 1    1       2      这了看  23        0
 2    1       5      夺      43       1
~~~



~~~
对标的进行评价
评论
输入评论信息，写入mongo
点击标地能查看所有评论，从mongo中查询，支持分页

商品一  1000
张三 这个商品好吗    2020-10-10   回复
      李四  这个商品很好           回复
              。。。。。          回复
李四  。。。。。。


评价表设计
id  userid  username content  create_time dish_id  pid

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

