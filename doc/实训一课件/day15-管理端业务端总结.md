1.管理端功能

~~~
1.登录  总管理员（所有的都能操作）     审核员 （用户管理 内容管理）  营销人员（外链）


审核员  zs  123456

用户管理
   普通用户管理
   机构作者管理
内容管理
   视频管理 （列表（审核））
   
   
营销人员  lishi  123456
营销管理
   设置友情链接
   统计
 
admin 123456

用户管理
   普通用户管理
   机构作者管理
内容管理
   视频管理 （列表（审核））
营销管理
   设置友情链接
   统计
权限管理
   用户管理
   角色管理  （列表，配制资源）
   资源管理


~~~

业务端vant 

~~~
登录
实名认证
我要充值
发布视频(加入队列-》协程分配)
~~~

### 审核模块

~~~
频-》内容审核

10万条-》多审核员-》审核员分配
视频发布-》发布将code放入待审核队列中-》定时任务获取到所有客服，遍历客服，每个客服从队列中取出任务，更新任务表中的审核人字段为当前审核人。
双队列保证任务完全被消费-》从审核队列取直接放到正在执行队列-》执行完成从正在执行队列中删除
定时任务每分钟去正在执行队列中查询，重新放入审核队列
~~~

