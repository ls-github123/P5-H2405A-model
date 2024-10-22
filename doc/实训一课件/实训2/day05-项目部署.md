docker安装

CentOS 7 安装 Docker 的步骤如下：

1. 卸载旧版本的 Docker（如果有）:

```
sudo yum remove docker \                  docker-client \                  docker-client-latest \                  docker-common \                  docker-latest \                  docker-latest-logrotate \                  docker-logrotate \                  docker-engine
```

1. 安装 Docker 依赖的软件包:

```
sudo yum install -y yum-utils
```

1. 设置 Docker 仓库:

```
sudo yum-config-manager \    --add-repo \    https://download.docker.com/linux/centos/docker-ce.repo
```

1. 安装 Docker Engine-Community:

```
sudo yum install docker-ce docker-ce-cli containerd.io
```

1. 更新镜像

   ~~~
   sudo mkdir -p /etc/docker
   sudo tee /etc/docker/daemon.json <<-'EOF'
   {
     "registry-mirrors": ["https://gt8iqili.mirror.aliyuncs.com"]
   }
   EOF
   sudo systemctl daemon-reload
   sudo systemctl restart docker
   ~~~

   

2. 启动 Docker 服务:

```
sudo systemctl start docker
```

1. 验证 Docker 是否正确安装:

```
sudo docker run hello-world
```

这些命令应以 root 用户或使用 sudo 执行。每一步都需要网络连接以从 Docker 仓库下载所需的包。



### **4.1** nginx

~~~
https://www.jd.com->首页
通过域名解析服务器-》把域名和ip绑定-》服务器上安装服务-》nginx-》反向代理-》代理服务-》wsgi或者guinio服务启动django\flask-》找到首页返回
~~~

#### 4.1.1nginx介绍

Nginx 是一个很强大的高性能[Web](https://baike.baidu.com/item/Web/150564)和[反向代理](https://baike.baidu.com/item/反向代理)服务，它具有很多非常优越的特性：

在连接高并发的情况下，Nginx是[Apache](https://baike.baidu.com/item/Apache/6265)服务不错的替代品：Nginx在美国是做虚拟主机生意的老板们经常选择的软件平台之一。能够支持高达 5万 个并发连接数的响应

~~~
1、轮询（默认）
每个请求按时间顺序逐一分配到不同的后端服务器，如果后端服务器down掉，能自动剔除。

upstream backserver {
    server 192.168.0.14;
    server 192.168.0.15;
    server 192.168.0.19;
}


2、权重 weight(服务器性能配制不一样，网络、带宽、内存、硬盘、CPU)
指定轮询几率，weight和访问比率成正比，用于后端服务器性能不均的情况。

upstream backserver {
    server 192.168.0.14 weight=3;
    server 192.168.0.15 weight=7;
}


3、ip_hash（ IP绑定）
上述方式存在一个问题就是说，在负载均衡系统中，假如用户在某台服务器上登录了，那么该用户第二次请求的时候，因为我们是负载均衡系统，每次请求都会重新定位到服务器集群中的某一个，那么已经登录某一个服务器的用户再重新定位到另一个服务器，其登录信息将会丢失，这样显然是不妥的。

我们可以采用ip_hash指令解决这个问题，如果客户已经访问了某个服务器，当用户再次访问时，会将该请求通过哈希算法，自动定位到该服务器。

每个请求按访问ip的hash结果分配，这样每个访客固定访问一个后端服务器，可以解决session的问题。

upstream backserver {
    ip_hash;
    server 192.168.0.14:88;
    server 192.168.0.15:80;
}


4、fair（第三方插件）
按后端服务器的响应时间来分配请求，响应时间短的优先分配。

upstream backserver {
    server server1;
    server server2;
    fair;
}


5、url_hash（第三方插件）
按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器，后端服务器为缓存时比较有效。

upstream backserver {
    server squid1:3128;
    server squid2:3128;
    hash $request_uri;
    hash_method crc32;
}
~~~

#### 4.1.2 nginx反向代理

反向代理服务器决定哪台服务器提供服务。返回代理服务器不提供服务器。只是请求的转发。

<img src="/Users/hanxiaobai/Downloads/python/p8/课件/用所选项目新建的文件夹/images/27.png">

<img src="/Users/hanxiaobai/Downloads/python/p8/课件/用所选项目新建的文件夹/images/28.png">

~~~
用户模块
商品模块
订单

http://localhost:8000/users      192.168.1.1
http://localhost:8000/course     192.168.1.2
http://localhost:8000/orders     192.168.1.3
~~~



centos7部署

nginx部署

~~~
sudo yum install epel-release
sudo yum install nginx
sudo systemctl start nginx
sudo systemctl status nginx


sudo vim /etc/nginx/nginx.conf
sudo systemctl reload nginx
~~~

本地下载压缩包远程拷到服务器



~~~
yum install wget -y
cd /home
mkdir soft
cd soft

直接下载：wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
远程复制：scp Python-3.9.1.tgz root@124.71.227.70:/home/soft


yum install -y gcc patch libffi-devel python-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

tar -zxvf Python-3.9.1.tgz
cd Python-3.9.1

mkdir -p /usr/local/python3


./configure --prefix=/usr/local/python3  # 指定安装目录为/opt/python39
make  &&  make install  # 相当于把源码包里面的代码编译成linux服务器可以识别的代码

#建立软链接
ln -s /usr/local/python3/bin/python3 /usr/bin/python39
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip39

环境变量配制

（1）vim /etc/profile

（2）按“I”，然后贴上下面内容：

# vim ~/.bash_profile

# .bash_profile

# Get the aliases and functions

if [ -f ~/.bashrc ]; then

. ~/.bashrc

fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin:/usr/local/python3/bin

export PATH

:wq保存
为了永久生效path设置，添加到/etc/profile全局环境变量配置文件中 ​ 重载配置文件/etc/profile
source /etc/profile


安装pip3
yum install python3-pip


pip39 install flask

cd /home/web
vi main.py
复制以下内容

from flask import Flask
 
app=Flask(__name__)
 
#定义视图
@app.route('/')
def index():
    return'hello world'
 
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)


pip39 install gunicorn
gunicorn main:app
gunicorn -w 4 -b 0.0.0.0:5000 test:app

nginx配制

vim /etc/nginx/nginx.conf
location / {
        proxy_pass http://124.71.227.70:5000/; #
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    
service nginx restart
docker stop nginx
docker start nginx

如果部署已经存在的项目

requirements.txt可以通过pip命令自动生成和安装，这种情况更适用于此项目是单独的虚拟python环境
生成requirements.txt文件

pip freeze > requirements.txt
pip3 freeze > requirements.txt
安装requirements.txt依赖

pip install -r requirements.txt
pip3 install -r requirements.txt


~~~



三台服务器

~~~python
192.168.0.1  负载均衡

192.168.0.2  自动化运维平台
192.168.0.3  自动化运维平台


1.在3台服务器上安装ngnix
docker pull nginx
docker run --name nginx -p 8080:80 -d nginx

2.在2和3上安装python



yum install wget -y
cd /home
mkdir soft
cd soft

wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz

yum install -y gcc patch libffi-devel python-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

tar -zxvf Python-3.9.1.tgz
cd Python-3.9.1

mkdir -p /usr/local/python3
yum install gcc

./configure --prefix=/usr/local/python3  # 指定安装目录为/opt/python39
make   # 相当于把源码包里面的代码编译成linux服务器可以识别的代码
make install

#建立软链接
ln -s /usr/local/python3/bin/python3 /usr/bin/python39
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip39



（1）vim /etc/profile

（2）按“I”，然后贴上下面内容：

# vim ~/.bash_profile

# .bash_profile

# Get the aliases and functions

if [ -f ~/.bashrc ]; then

. ~/.bashrc

fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin:/usr/local/python3/bin

export PATH

:wq保存
为了永久生效path设置，添加到/etc/profile全局环境变量配置文件中 ​ 重载配置文件/etc/profile
source /etc/profile


安装pip3
yum install python3-pip

tornado
pip3 install tornado

#写tornado代码
#运行

pip3 install flask

pip3 install gunicorn
gunicorn test:app
gunicorn -w 4 -b 0.0.0.0:5000 main:app

docker exec -it nginx /bin/bash 
vim /etc/nginx/conf.d/default.conf
location / {
        proxy_pass http://124.71.227.70:5000/; #
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    
service nginx restart
docker stop nginx
docker start nginx
    
apt-get update && apt-get install procps
ps -aux


~~~

安装django

~~~
pip39 install django
pip39 install pysqlite3-binary
~~~



~~~
docker pull nginx
docker run --name nginx -p 8080:80 -d nginx
docker exec -it 9bb78a31a3c5 /bin/bash

https://www.cnblogs.com/carver/articles/16630831.html
安装vim
更换镜像
mv /etc/apt/sources.list /etc/apt/sources.list.bak
更新
apt-get update
apt-get install -y vim

vim /etc/nginx/conf.d/default.conf
location /api {
        proxy_pass http://43.143.162.69:5000; #
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    
service nginx restart
    
apt-get update && apt-get install procps
ps -aux


requirements.txt可以通过pip命令自动生成和安装，这种情况更适用于此项目是单独的虚拟python环境
生成requirements.txt文件

pip freeze > requirements.txt
pip3 freeze > requirements.txt
安装requirements.txt依赖

pip install -r requirements.txt
pip3 install -r requirements.txt


sudo yum install python3-devel
yum install libevent-devel

yum install python devel

yum install python-gevent
python3 -m pip install --upgrade pip

pip3 install gevent==1.4.0

from flask import Flask
app = Flask("__name__")

@app.route("/")
def test():
    print("hello flask")
if __name__=="__main__":
  app.run()
~~~

安装vim

~~~
更换镜像
mv /etc/apt/sources.list /etc/apt/sources.list.bak
更新apt-get
apt-get update
下载vim
apt-get install -y vim
下载
apt-get update && apt-get install procps
查看
ps -aux
~~~

### vue部署

~~~
scp -r 本地目录 用户@IP地址:文件路径
~~~

```text
npm run build
```

~~~
scp   dist   root@24234324:/home
docker cp dist ngnix:/usr/nignx/
~~~

