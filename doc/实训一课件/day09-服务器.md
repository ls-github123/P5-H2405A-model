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

   

