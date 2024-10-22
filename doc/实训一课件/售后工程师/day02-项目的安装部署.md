### 1.熟练使用Mysql数据库安装部署及简单的sql查询

~~~
mysql是一个关系型数据库，用于基础数据类型的存储。支持索引、外键、事务和锁。

常用命令
创建数据库
create database test123 charset=utf8; 
use test123;
查看所有数据库
show databases;
创建表
create table testabc(
	id int primary key auto_increment,
	name varchar(100) not null default ''
);
单表查询
select * from testabc where name='asdf';
连接查询
left join 、inner join、right join
更新
update testabc set name='zs' where id=1;
~~~

2.熟练应用linux操作系统，部署及常用命令

~~~
1、top：查看内存/显示系统当前进程信息

2、df -h：查看磁盘储存状况 (如果出现磁盘报警和实际有出入，可能因为文件操作符或者文件句柄未释放导致)

3、iotop：查看IO读写（yum install iotop安装）

4、iotop -o：直接查看比较高的磁盘读写程序

5、netstat -tunlp | grep 端口号：查看端口号占用情况（1）

6、lsof -i:端口号：查看端口号占用情况（2）

7、uptime：查看报告系统运行时长及平均负载

8、ps aux：查看进程

9、 free 查看内存交换区



ps：查看进程，ps aux 或者 ps -elf，常和管道符一起使用，查看某个进程或者它的数量；
netstat：查看端口，netstat -lnp用于打印当前系统启动了哪些端口，netstat -an用于打印网络连接状况；
top 以全屏交互式的界面显示进程排名，及时跟踪包括CPU、内存等系统资源占用情况，默认情况下每三秒刷新一次，其作用基本类似于Windows系统中的任务管理器
chmod 改变文件的权限  
chmod -R xyz  文件或文件夹名 比如 755表示该文件所有者对该文件具有读、写、执行权限，该文件所有者所在组用户及其他用户对该文件具有读和执行权限。

date 查看当前时间
shutdown 关机

cd 变换目录
pwd 显示当前所在目录
mkdir 建立新目录
rm 目录或文件名
rm -rf  -r或-R：递归处理，将指定目录下的所有文件与子目录一并处理；-f：强制删除文件或目录；
ls 档案与目录的显示
ls -l
cp 复制档案或目录
mv 移动档案与目录
cat 由第一行开始显示档案内容
tac 从最后一行开始显示
more 一页一页的显示档案内容
less 与 more 类似，但是比 more 更好的是，他可以往前翻页
touch 修改档案时间或新建档案
which 寻找【执行挡】 which 文件名  which -a 文件名目录和文件都显示
whereis 文件名 寻找特定档案
find 寻找特定档案
gzip，zcat 压缩文件和读取压缩文件
tar -zpcv -f 文件名 压缩文件和读取压缩文件
ps aux 查看进程

压缩命令：命令格式：tar  -zcvf   压缩文件名.tar.gz   被压缩文件名

解压缩命令：命令格式：tar  -zxvf   压缩文件名.tar.gz
~~~

#### linux怎么启动定时任务

```
1.首先安装cron服务
sudo apt-get install cron
2.启动与关闭cron服务
service cron start //启动服务
service cron stop //关闭服务
service cron restart //重启服务
service cron reload //重新载入配置
service cron status //查看crontab服务状态
```

#### linux怎么查看端口

```
netstat - atulnp会显示所有端口和所有对应的程序，用grep管道可以过滤出想要的字段

    -a ：all，表示列出所有的连接，服务监听，Socket资料
    -t ：tcp，列出tcp协议的服务
    -u ：udp，列出udp协议的服务
    -n ：port number， 用端口号来显示
    -l ：listening，列出当前监听服务
    -p ：program，列出服务程序的PID
```

#### linux查看进程

```
  ps -l  查看登录有关的进程信息；
  ps -aux  查询[内存](https://so.csdn.net/so/search?q=内存&spm=1001.2101.3001.7020)中进程信息；
  ps -aux | [grep](https://so.csdn.net/so/search?q=grep&spm=1001.2101.3001.7020) ***  查询***进程的详细信息；
  top  查看内存中进程的动态信息；
  kill  pid  杀死进程。
  kill -9强制立即执行

终止linux进程

kill[参数][进程号]杀死进程
```

#### 查看磁盘占用率

~~~
1、df命令

　　df命令全称为disk-free，用于查看Linux系统中的可用和已经使用的磁盘空间，一般有以下几个常用选项：

　　df -h：以可读的格式显示磁盘空间(否则默认显示单位是字节，不直观);

　　df -a：包含全部的文件系统；

　　df -T：显示磁盘使用情况以及每个块的文件系统类型(如xfs、ext2、ext3、btrfs等);

　　df -i：显示已使用和空闲的inode。

　　2、du命令

　　du命令全称为disk useage的缩写，以默认千字节大小显示文件、文件夹等磁盘使用情况，一般有以下几个常用选项：

　　du -h：以可读的格式显示所有目录和子目录的磁盘使用情况；

　　du -a：显示所有文件的磁盘使用情况；

　　du -s：仅显示总计，只列出最后加总的值；

　　3、ls -al命令

　　ls命令大家再熟悉不过了吧，使用ls -al命令可以列出特定目录的全部内容及其大小。

　　4、stat命令

　　stat命令后面可以直接跟上文件或目录，用于显示文件/目录或文件系统的大小和其他统计信息。

　　5、fdisk -l命令

　　fdisk -l：可以显示磁盘大小以及磁盘分区信息。
~~~

### 2.精通tcp/ip协议

#### 2.1.http和https有什么区别？

~~~
 1、https协议需要到ca申请证书，一般免费证书较少，因而需要一定费用。

 2、http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输协议。

 3、http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443。

　4、http的连接很简单，是无状态的；HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。
~~~

#### 2.2.网络七层协议

http在应用层，ip协议在网络层，tcp在传输层。

<img src="images/5.png">

#### 2.3.tcp/udp的区别是什么

~~~
1、TCP面向连接（如打电话要先拨号建立连接）;UDP是无连接的，即发送数据之前不需要建立连接
2、TCP提供可靠的服务。也就是说，通过TCP连接传送的数据，无差错，不丢失，不重复，且按序到达;UDP尽最大努力交付，即不保   证可靠交付
3、TCP面向字节流，实际上是TCP把数据看成一连串无结构的字节流;UDP是面向报文的
  UDP没有拥塞控制，因此网络出现拥塞不会使源主机的发送速率降低（对实时应用很有用，如IP电话，实时视频会议等）
4、每一条TCP连接只能是点到点的;UDP支持一对一，一对多，多对一和多对多的交互通信
5、TCP首部开销20字节;UDP的首部开销小，只有8个字节
6、TCP的逻辑通信信道是全双工的可靠信道，UDP则是不可靠信道
~~~

#### 2.4.说一下三握四挥

~~~
第一次握手
　　A的TCP进程创建TCB（传输控制块），然后向B发出连接请求报文段。段首部中的 同步位SYN=1，同时选择一个初始序列号seq=x；（SYN报文段不能携带数据，但需要消耗一个序列号）这时客户端A进入到 SYN-SENT（同步已发送）状态。

第二次握手
　　B收到连接请求报文段，如果同意建立连接，则向A发送确认。在确认报文段中 同步位SYN=1、确认位ACK=1、确认号ack=x+1（对接收的序列号seq=x的报文段进行确认，并期望接收的下一个报文段的序号seq=x+1），同时也为自己选择一个初始序列号seq=y，这时服务器B进入 SYN-RCVID 状态。

　　注：该报文段是ACK报文段的同时也是SYN报文段，所以该报文段也不能携带数据。

第三次握手
　　A收到B的确认以后，再向B发出确认。确认报文 ACK=1、确认号ack=y+1（对接收的序列号seq=y的报文段进行确认，并期望接收的下一个报文段的序号seq=y+1）。这时A进入到 ESTAB-LISHED 状态。当B接收到A的确认后，也进入 ESTAB-LISHED 状态。连接建立完成

　　注：ACK报文段可以携带数据，但如果不携带数据则不消耗序列号，在这种情况下，下一个报文段的序号不变，seq仍是x+1。
　　
　　
　　第一次挥手：A先发送连接释放报文段，段首部的终止控制位FIN=1，序号seq=u（等于A前面发送数据的最后一个序号加1）；然后A进入 FIN-WAIT-1（终止等待1）状态，等待B的确认。A
　　注：FIN报文段即使不携带数据也要消耗一个序列。

第二次挥手：B收到A的连接释放报文段后，立刻发出确认报文段，确认号ack=u+1，序号seq=v（等于B前面发送数据的最后一个序号加1）；然后B进入CLOSE-WAIT（关闭等待）状态。
　　注：TCP服务器这时会通知高层应用进程，从A到B这个方向的连接就断开了，这时TCP连接处于半关闭（half-close）状态；但B到A这个方向的连接并没有断，B任然可以向A发送数据。

第三次挥手：A收到B的确认报文段后进入到 FIN-WAIT-2（终止等待2）状态，继续等待B发出连接释放报文段；若B已经没有数据要发送，B就会向A发送连接释放报文段，段首部的终止控制位 FIN=1，序号seq=w（半关闭状态可能又发送了一些数据），确认号ack=u+1，这时B进入LAST-ACK（最后确认）状态，等待A的确认。
　　特别注意：确认号ack没有变，仍然为上次发送过的确认号u+1。

第四次挥手：A收到B的连接释放报文段并发出确认，确认段中 确认位ACK=1，确认号ack=w+1，序号seq=u+1；然后A进入到TIME-WAIT（时间等待）状态。当B再接收到该确认段后，B就进入CLOSED状态。
　　注：处于TIME-WAIT状态的A必须等待2MSL时间后，才会进入CLOSED状态。MSL（Maximum Segment Lifetime）最长报文段寿命，RFC 793 建议设为两分钟，对于现在的网络，MSL=2分钟可能太长了一些，我们可根据具体情况使用更小的MSL值。
~~~

#### 2.5.为什么建立连接三次，断开连接四次？

~~~
因为建立连接时，服务器的确认 ACK 和请求同步 SYN 可以放在一个报文里，而断开连接时，服务器可能还有数据要传送，因此，必须先发一个客户端断开连接请求的确认 ACK，以免客户端超时重传，待服务器的数据传送完毕后，再发送一个请求断开连接的报文段。
断开时次数比连接多一次，是因为连接过程，通信只需要处理「连接」，而断开过程，通信需要处理「数据+连接」。
~~~

#### 2.6.http是什么组成的？

~~~
HTTP 请求的组成
         状态行、请求头、消息主体三部分组成。
HTTP 响应的组成
         状态行、响应头、响应正文
~~~

### 4.熟悉shell脚本的编写

#### 4.1介绍

~~~
shell是Linux系统的用户界面，它提供用户与内核的一种交互方式。它接收用户输入的命令，并把它送入内核去执行，是一个命令解释器。
shell脚本就是将命令写入文本中，文本可以被执行。
脚本：本质是一个文件，文件里面存放的是 特定格式的指令，系统可以使用脚本解析器 翻译或解析 指令 并执行（它不需要编译）
shell 既是应用程序，又是一种脚本语言（应用程序 解析 脚本语言）。
~~~

#### 4.2、执行方式

- ./xxx.sh 先按照#！指定的解析器解析，如果找不到使用默认解析
- bash xxx.sh 指定使用bash解析器解析，找不到使用默认解析
- . xxx.sh 直接使用默认解析

#### 4.3shell语法

~~~
1、定义以开头：#!/bin/sh
#!用来声明脚本由什么shell解释，否则使用默认shell

2.变量定义
Shell 变量的命名规范和大部分编程语言都一样：

变量名由数字、字母、下划线组成；
必须以字母或者下划线开头；
不能使用 Shell 里的关键字（通过 help 命令可以查看保留关键字）。
~~~

<img src="images/6.png">

<img src="images/7.png">

shell脚本数据库备份

~~~python
#!/bin/bash
 
#先指定备份路径
BACKUP=/root/backup
 
#显示当前时间
DATATIME=$(date "+%Y-%m-%d_%H%M%S")
 
#运行数据库的主机IP地址（执行备份的主机和运行数据库的主机可能不是同一台，如果同一台填自己IP即可）
HOST=172.19.1.1
 
#登录数据库的用户名
DB_USER=xss
 
#数据库该用户名的密码
DB_PW=pwd@123
 
#备份的数据库名（如需备份所有库，可参考下面步骤直接指定库名为 all）
DATABASE=DT
 
#开始备份数据库提示语，仅提示作用，手动执行时方便判断到了哪一步
echo "开始备份数据库${DATABASE}"
 
#创建备份目录（如果指定的目录不存在，则新建目录，！-d不存在则成立，&&表示左端成立则执行右端动作）
[ ! -d ${BACKUP}/${DATATIME} ] && mkdir -p "${BACKUP}/${DATATIME}"
 
#备份数据库（这里我按项目实际情况指定all-databases，备份所有库）
mysqldump -u${DB_USER} -p${DB_PW} --host=${HOST}  --all-databases  | gzip > ${BACKUP}/${DATATIME}/$DATATIME.sql.gz
 
#将文件压缩成  tar.gz 
cd ${BACKUP}
tar -zcvf $DATATIME.tar.gz ${DATATIME}
 
#删除已备份的目录,由于压缩了文件，压缩前原有的可以删了
rm -rf  ${BACKUP}/${DATATIME}
 
#删除14天前的压缩文件（按实际需求，我这里删除14天前的备份文件）
find ${BACKUP} -atime +14 -name "*.tar.gz" -exec rm -rf {} \;
 
#结束备份数据库提示语，仅提示作用（！e如果该文件存在，则成立，||左端成立，则执行右端，建议加上这个条件，否则即使上面的数据库备份不成功，下面仍然会提示备份成功，这样就没法有效判断）
[ ! -e ${DATATIME}.tar.gz ] || echo "数据库${DATABASE}备份成功!"
 
#推送到钉钉（这个步骤可省略，我根据项目需求想通过钉钉消息，就知道是否备份数据库。！-e数据库文件存在，则执行右端的python脚本，推送消息到钉钉群，钉钉脚本需要填写2个参数，1为用户名（为了不@我，这里填1，也可填自己实际的钉钉号，这样钉钉机器人发消息就会@我）， "DTcenter数据库${DATATIME} 备份成功！"为指定钉钉机器人发送的信息）
[ ! -e ${DATATIME}.tar.gz ] || ./dingding.py 1 test "DTcenter数据库${DATATIME} 备份成功！"
~~~



### 5.熟悉nginx服务器

~~~
http://www.baidu.com
域名通过域名解析服务器-》绑定ip->服务器-》nginx服务-》nginx配制文件中location

Nginx 是一个很强大的高性能服务，它具有很多非常优越的特性：

在连接高并发的情况下，Nginx是apache服务不错的替代品：Nginx在美国是做虚拟主机生意的老板们经常选择的软件平台之一。能够支持高达 5万 个并发连接数的响应
~~~

### 6.熟练使用docker容器式部署

~~~
docker images 来列出本地主机上的镜像
docker search 查找镜像
docker pull  下载镜像
docker run -it 镜像名 /bin/bash 运行容器
docker start 启动容器
docker stop 停止窗口
docker rm 删除容器
docker cp 拷贝文件
docker exec 进入容器
~~~

### 3.docker安装es

~~~
docker pull elasticsearch:7.7.0
~~~

~~~
docker run --name elasticsearch -d -e ES_JAVA_OPTS="-Xms512m -Xmx512m" -e "discovery.type=single-node" -p 9200:9200 -p 9300:9300 elasticsearch:7.7.0
~~~



