### 1.场景需求

~~~
1. 张三中秋快乐         审核
2. 李四茜革柑要要基本面  审核
3
~~~

### 2.websocket

~~~
http一次请求一次响应 https

websocket全双工通讯协议，持久化连接，客户端向服务端发起请求-》通道，基于ws协议 wss

发布视频-》审核分配-》审核员登录-》展示待我审核 ，当有新任务产生不用刷新直接显示信息

~~~

3.百度实名认证

~~~
list 图片Url
定时任务： list   向api接口发起请求-》拿到数据redis key url value 解析出来的名字身份证号

setInterval ->每秒发送一次请求

websocket


发布发布视频-》存入队列 -》定时任务分配客服


审核员登录成功后，进入待审核页面->1.进行websocket连接->接口获取到连接，存入字典 key userid:connection
~~~

