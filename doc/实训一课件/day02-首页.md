

![image-20240108083310103](/Users/hanxiaobai/Library/Application Support/typora-user-images/image-20240108083310103.png)

~~~
首页涉及到的表
分类表（id  name）
insert into recomand_cates() values()

视频表（code  分类id  图片  url  publishid  pushlishname  puhlishpic  collections ）
insert into 

来源 fastapi
publish1           publish1             cates
id title colletions cateid  (取前10个)放入分类表中
获取这10个分类的前20个视频放入视频表


~~~





### 1.轮播图

~~~
1.显示默认图片 0.jpg

获取图片列表
[1.jpg,2.jpg,3.jpg]

setInterval(()=>{
//遍历列表，当前显示的和列表中的相同，取下一个
//取第一个，已经是最后一个，取第一个

	
},1000)

{code:200,'piclist':[1.jpg],'small':'http:///1.jpg'}
~~~

2.分类及商品列表

~~~
地址:v1/catesgoods/
方式:get
参数：{'ordering':'price'}
响应：{"code":200,"clist":[{"id":1,"name":'','son':[],'lastson':[],'glist':[]},{},{}]}
~~~

详情页实现

redis

~~~
REmote DIctionary Server(Redis) 是一个由 Salvatore Sanfilippo 写的 key-value 存储系统，是跨平台的非关系型数据库。

Redis 是一个开源的使用 ANSI C 语言编写、遵守 BSD 协议、支持网络、可基于内存、分布式、可选持久性的键值对(Key-Value)存储数据库，并提供多种语言的 API。

写 8万次 ，读取11 万次



redis nosql  非关系型数据库，内存型数据库。单线程，io多路复用模型中的epoll实现（select、poll、epoll）
select：事件处理轮询，把所有事件放到一个队列中，从第一个开始读，判断有没有响应，如果执行返回，如果没有，有1024限制
poll和select 取消了限制
epoll：要处理的事件加一个监听，当事件获取到数据，把已经准备好的任务放到就绪队列中，执行的时候只需要执行就绪队列

Redis 通常被称为数据结构服务器，因为值（value）可以是字符串(String)、哈希(Hash)、列表(list)、集合(sets)和有序集合(sorted sets)等类型。

字符串：key->键  value
r.set(key,value) 
r.get(key)
r.setnx(key,value)

hash对象
user  age  10
      name '张三'
      
list  1,2,3,3




~~~

如何保证缓存和数据库的一致

~~~
时时变化的数据不适合缓存
延时双删
：数据更新前删除缓存，更新数据，删除缓存
~~~

~~~
手机
   华为
      meta
          meta11  
                    meta111
                              手机
                              
      note
          meta11  
                    meta111
                              手机
   小米
       小米2系统
                 小米2系统
                      小米2系统
                               手机
                               
     def getids(ids):                         
    	 cates = cates.objects.filter(pid__in=ids).values('id')
    	 if cates:
    	    return getids([2,3])
    	 else:
    	    return ids
    	      
     
~~~



