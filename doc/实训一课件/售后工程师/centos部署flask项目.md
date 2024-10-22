### **4.1** ngnix

~~~
http://www.baidu.com
ip 机器  192.168.1.1:8000

tomcat ngnix apache


http://jd.com/ -> 43.143.162.69:5000

安装服务nginx、apache、tomcat

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

### 4.3解决没有权限操作

~~~
所以遇到这种问题便是修改

sudo vim /etc/ssh/sshd_config

增加如下修改

PasswordAuthentication yes

sudo systemctl restart sshd
~~~



### 4.2安装docker

~~~
#升级所有包同时也升级软件和系统内核；
yum -y update 

#删除自带的docker
yum remove docker  docker-common docker-selinux docker-engine

1.安装需要的软件包， yum-util 提供yum-config-manager功能，另两个是devicemapper驱动依赖
yum install -y yum-utils device-mapper-persistent-data lvm2

设置一个yum源，下面两个都可用,选择一个
yum-config-manager --add-repo http://download.docker.com/linux/centos/docker-ce.repo（中央仓库）
 
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo（阿里仓库）

#查看可用版本
yum list docker-ce --showduplicates | sort -r
#安装docker
yum -y install docker-ce-18.03.1.ce

#设置开机启动
systemctl start docker
systemctl enable docker
~~~

### 4.3docker安装nginx

~~~
docker pull nginx
docker run --name nginx -p 8080:80 -d nginx
docker exec -it nginx /bin/bash

docker中安装vim
apt-get update
apt-get install vim

~~~

### 4.4安装python

~~~python

yum install vim

yum install wget -y

wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz

yum install -y gcc patch libffi-devel python-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

tar -zxvf Python-3.9.1.tgz
cd Python-3.9.1

mkdir -p /usr/local/python3
apt-get install gcc

./configure --prefix=/usr/local/python3  # 指定安装目录为/opt/python39
make   # 相当于把源码包里面的代码编译成linux服务器可以识别的代码
make install

#建立软链接
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

并将/usr/local/python3/bin加入PATH

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
为了永久生效path设置，添加到/etc/profile全局环境变量配置文件中  重载配置文件/etc/profile
source /etc/profile

python3
安装pip3
apt-get install python3-pip

pip3 install flask

pip3 install gunicorn
gunicorn test:app
gunicorn -w 4 -b 127.0.0.1:8001 test:app

vim /etc/nginx/conf.d/default.conf
location / {
        proxy_pass http://127.0.0.1:8002; #
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    
service nginx restart
    
apt-get update && apt-get install procps
ps -aux


~~~



~~~
docker pull nginx
docker run --name nginx -p 8080:80 -d nginx
docker exec -it 9bb78a31a3c5 /bin/bash


apt-get update
apt-get install vim

apt-get install wget -y

wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz

apt-get install -y gcc patch libffi-devel python-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

tar -zxvf Python-3.9.1.tgz
cd Python-3.9.1

mkdir -p /usr/local/python3
apt-get install gcc

./configure --prefix=/usr/local/python3  # 指定安装目录为/opt/python39
make   # 相当于把源码包里面的代码编译成linux服务器可以识别的代码
make install

#建立软链接
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

并将/usr/local/python3/bin加入PATH

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
为了永久生效path设置，添加到/etc/profile全局环境变量配置文件中  重载配置文件/etc/profile
source /etc/profile

python3
安装pip3
apt-get install python3-pip

pip3 install gunicorn
gunicorn test:app
gunicorn -w 4 -b 0.0.0.0:8001 test:app

vim /etc/nginx/conf.d/default.conf
location / {
        proxy_pass http://0.0.0.0:8001; #
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



3.在0.1服务器上配制
#user  nobody;
worker_processes  1;
events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;
   upstream webservers{
      server  192.168.0.2;
      server  192.168.0.3;
   }
 
    server {
        listen       80;
        server_name  localhost;
        #location / {
         #   root   html;
          #  index  index.html index.htm;
        #}

        location / {
             #转发到负载服务上
            proxy_pass http://webservers/;
         }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}
~~~
