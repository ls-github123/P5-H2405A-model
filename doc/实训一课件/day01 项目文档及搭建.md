1. 下载项目git

   本地分支：账号创建一个分支，开发分支 

   测试分支

   部署分支

   ~~~
   git clone  
   git branch  
   ~~~

   conda虚拟环境

2.项目开发流程

项目管理软件：禅道 自己公司搭建的内部平台

用户管理

项目管理

​     创建项目

​     项目列表   人员

角色管理

​     开发

​     测试

​     运维。。。

资源管理

​    添加用户

​    订单列表

​    bug管理



### 1.项目中的角色

https://www.axureshop.com/ys/2173349

### 2.功能模块

![image-20241022101401787](images/40.png)



![image-20241022140154226](/Users/hanxiaobai/Library/Application Support/typora-user-images/image-20241022140154226.png)



### 3.数据库字典

用户表（users）

<table>
  <tr><td>字段名</td><td>字段类型</td><td>中文名</td><td>描述</td></tr>
  <tr><td>id</td><td>int</td><td>ID</td><td>主键自增</td></tr>
  <tr><td>mobile</td><td>char(11)</td><td>手机号</td><td>唯一</td></tr>
  <tr><td>types</td><td>char(11)</td><td>类型</td><td>1普通会员  2vip</td></tr>
</table>

工具表

<table>
  <tr><td>字段名</td><td>字段类型</td><td>中文名</td><td>描述</td></tr>
  <tr><td>id</td><td>int</td><td>ID</td><td>主键自增</td></tr>
  <tr><td>title</td><td>char(11)</td><td>手机号</td><td>唯一</td></tr>
  <tr><td>descrip</td><td>char(11)</td><td>类型</td><td>1普通会员  2vip</td></tr>
  <tr><td>url</td><td>char(11)</td><td>类型</td><td>1普通会员  2vip</td></tr>
  <tr><td>picurl</td><td>char(11)</td><td>类型</td><td>1普通会员  2vip</td></tr>
</table>

### 4.接口文档

### 5.在gitee上新建一个仓库, 

### 本地： git clone 下载

Django-admin startproject education

### 搭建项目创建模型类

  用django搭建，settings中的配制

  在项目主目录下新建一个tools文件夹，在tools下封装工具

   Jwt、redis

 创建模型类迁移

My_vue_pro

git add .

git commit -m 'init'

git push













