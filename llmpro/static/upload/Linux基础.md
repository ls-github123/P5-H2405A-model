# 第一单元  Liunx

## **一、昨日知识点回顾**

```python
1. git的流程
2. git冲突解决方案
```

------

## **二、考核目标**

```
1.linux基础
2.linux高级命令
3.组和权限掌握
```

------

## **三、本单元知识详讲**

### 1.1 Linux基础



#### 1.1.1 概述

linux就是一个操作系统，与苹果系统，安卓系统，鸿蒙系统，windwos系统类似。

计算机有硬件和软件组成，操作系统就是硬件上面的第一层软件，它是硬件和其它软件沟通的桥梁。计算机技术在二战后快速发展，构成计算机的主要基本单元从电子管发展到分立晶体管，再到后来的大规模集成电路。随着计算机技术发展，计算机性能越来越强劲，硬件越来越复杂，人们发现很难去直接管理计算机了，于是人们开始设计软件用于管理越来越复杂的计算机系统，这些软件称作系统级软件。

![image-20220106010934038](assets\image-20220106010934038.png)

![img](assets\b5af67e95014e05bcc7bc1cdce98d0e6.png)



**Unix**

1965 年，MIT（麻省理工）、Bell（贝尔实验室）和GE（美国通用电气公司）合作准备搞个超级操作系统，取了个霸气的名字：Multics (Multiplexed Information and Computing System），多路复用信息和计算机系统。能让多个人可以同时干很多事，也叫多用户多任务操作系统。

1969 年，Multics 项目进展缓慢，被迫停止，参与项目的两个人 Ken Thompson（肯·汤普森）和 Dennis Ritchie（丹尼斯·里奇） 也闲了下来。他们都是贝尔实验室的人。没活干了，就打游戏。他们俩找了一台破电脑（PDP-7）准备玩以前开发的一个游戏（travel space：遨游太空），为了能在PDP-7 计算机上运行他的游戏，于是在1969 年夏天Ken Thompson（肯·汤普森）趁他夫人回家乡加利福尼亚渡假期间，在一个月内开发出了UNIX 操作系统的原型，UNIX于是就在1970年正式问世了，这就是Unix元年。自 1970 年后，UNIX 系统在贝尔实验室内部的程序员之间逐渐流行起来，当时使用的是BCPL 语言（基本组合编程语言），后经Dennis Ritchie 于1973 年用移植性很强的C语言进行了改写。

UNIX 的出现是由 Ken Thompson（肯·汤普森）和 Dennis Ritchie（丹尼斯·里奇）在贝尔实验室工作期间开发出来的，自然版权属于贝尔实验室所有。一开始贝尔实验室并没有重视这个系统，导致这个系统的源代码在程序员之间不断分发导致美国很多机构、组织和高校都有非常多的人在使用这个UNIX，这就为UNIX的发展带来的高速的发展，但是随着UNIX发展的越来越好，这时候贝尔实验室就开始了商业运作了，他们决定要收回版权。但是从原来的免费获取使用变成后面的高价版权费用，很多人甚至是公司是接受不了的，所以这个商业运作进展缓慢，后面不得已就变成了，贝尔实验室收回版权，但是针对一些有合作的高校和机构，收取廉价或者是几乎免费的版权费用。

于是在20世纪70年代后期，与教育机构和外部商业组织共享了Unix，从而导致了许多不同版本Unix的诞生。其中最突出的是由加州大学伯克利分校的计算机系统研究小组构建的教育版本(BSD)。当然BSD与比尔·乔伊（[Bill Joy](https://baike.baidu.com/item/Bill Joy)）又是另一段传奇故事了。



**GUN**

1983年9月，Richard Stallman(理查德·斯托曼)宣布引入GNU计划(GNU：Gnu Not Unix)。1985年，理查德（Richard）建立了自由软件基金会（FSF），这是一个非营利性组织，旨在促进软件开发的自由。GNU项目创建了许多重要的产品，如GNU Compiler Collection (gcc)、GNU Debugger、GNU Emacs text editor (Emacs)、GNU build automator (make)等，还有今天使用最广泛的: GNU通用公共许可证(GPL)。GNU项目取得了许多伟大的成就，创造了许多与Unix相似的工具。然而，GNU仍然缺少一个重要的组成部分：内核（用于处理与硬件设备(CPU、RAM、设备等)的控制和通信的部分）。

GNU项目的目标是创建一个自由的、类unix的操作系统，在这个系统中，人们人们可以自由地复制，开发，修改和分发软件，并且不受限制。

![img](assets\d058ccbf6c81800ae81cfab97edc96fc808b47f8.jpeg)

**Minix**

Minix诞生于1987年，由Andrew S. Tanenbaum（安德鲁·斯图尔特·塔能鲍姆，谭邦宁）教授编写，用作教学的微内核架构的类Unix系统。当时Unix系统由于AT&T的使用许可问题，Unix不能被大学使用，谭邦宁教授为了让学生能看到操作系统的运行机理，自己重新写了一个操作系统，就叫它Minix。

**Linux**

![image-20220408003903953](assets\image-20220408003903953.png)

Linux内核最初只是由芬兰人Linus Torvalds（林纳斯·托瓦兹）在赫尔辛基大学上学时出于个人爱好而编写的。

Linux是一套免费使用和自由传播的类Unix操作系统，是一个基于POSIX和UNIX的多用户、多任务、支持多线程和多CPU的操作系统。Linux能运行主要的UNIX工具软件、应用程序和网络协议。它支持32位和64位硬件。Linux继承了Unix以网络为核心的设计思想，是一个性能稳定的多用户网络操作系统。

目前市面上较知名的发行版有：**Ubuntu(乌班图)**、RedHat(红帽)、**CentOS（森托斯）**、Debain（德班）、Fedora（费多拉）、 **Alpine（阿尔卑斯）**、OpenSUSE（苏瑟）等。

![](assets\linux-pub-timeline.jpeg)



**系统镜像下载地址**

| 所属大学/企业 | 站点地址                              |
| ------------- | ------------------------------------- |
| 网易          | http://mirrors.163.com/               |
| 搜狐          | http://mirrors.sohu.com/              |
| 阿里          | https://developer.aliyun.com/mirror/  |
| 华为          | https://mirrors.huaweicloud.com/      |
| 腾讯          | https://mirrors.cloud.tencent.com/    |
| 平安          | https://mirrors.pinganyun.com/        |
| 清华          | https://mirrors.tuna.tsinghua.edu.cn/ |
| 北大          | http://mirrors.pku.edu.cn/            |
| 科大          | http://mirrors.ustc.edu.cn            |
| 北交          | https://mirror.bjtu.edu.cn/           |
| 南大          | https://mirrors.nju.edu.cn/           |



#### 1.1.2Linux特点

Linux里面一切皆是文件，目录是文件，网卡等设备都是文件。

Linux里面没有后缀名这一说，但是一般为了方便使用者甄别文件的类型，所以会存在文件添加后缀的情况。



**Linux和Windows区别**

目前国内Linux更多的是应用于服务器上，而桌面操作系统更多使用的是window。主要区别如下。

| 比较     | Window                                                       | Linux                                                        |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 界面     | 界面统一，外壳程序固定所有Windows程序菜单几乎一致，快捷键也几乎相同 | 圆形界面风格依发布版本不同而不同，可能互不兼容。GNU/Linux的终端机是从UNIX传承下来，基本命令和操作方法也几乎一致。 |
| 驱动程序 | 驱动程序丰富，版本更新频繁。默认安装程序里面一般包含有该版本发布时流行的硬件驱动程序，之后所出的新硬件驱动依赖于硬件厂商提供。对于一些老硬件，如果没有了原配的驱动有时候很难支持。另外，有时硬件厂商未提供所需版本的Windows下的驱动，也会比较头痛。 | 由志愿者开发，由Linux核心开发小组发布，很多硬件厂商基于版本考虑并未提供驱动程序，尽管多数无需手动安装，但是涉及安装则相对复杂，使得新用户面对驱动程序问题会一筹莫展。但是在开源开发模式下，许多老硬件尽管在Windows下很难支持的也容易找到驱动。HP、Intel、AMD等硬件厂商逐步不同程序支持开源驱动，问题正在得到缓解。 |
| 使用     | 使用比较简单，容易入门。圆形化界面对没有计算机背景知识的用户使用十分有利。 | 圆形界面使用简单，容易入门。文字界面，需要学习才能掌握。     |
| 学习     | 系统构造复杂、变化频繁、且知识、技能淘汰快，深入学习困难     | 系统构造简单、稳定，且知识、技能传承性好，深入学习相对容易   |
| 软件     | 每一种特定功能可能都需要商业软件的支持，需要购买相应的授权   | 大部分软件都可以自由获取，同样功能的软件选择较少。           |

#### 1.1.3目录结构

windows下面的所有的文件都是保存在盘符下的，而且每一个盘符都有各自的根目录。

Linux下面没有盘符的概念，所有一切的文件都是保存在根目录下

```bash
盘符名称        C:
盘符的根目录    C:\   C:/


根目录          /
```



![assets/diretory.jpg](assets\diretory.jpg)

| 目录        | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| **/**       | 第一层次结构的根(root)、整个文件系统层次结构的根目录。       |
| **/bin/**   | 需要在单用户模式可用的必要命令（二进制可执行文件）；面向所有用户，例如：cat、ls、cp，和/usr/bin类似。 |
| /boot/      | 引导程序文件，例如：kernel、initrd；时常是一个单独的分区。   |
| **/dev/**   | 必要设备, 例如：, /dev/null.                                 |
| **/etc/**   | 系统配置文件的存放目录。                                     |
| **/home/**  | 普通用户的家目录，包含保存的文件、个人设置等，一般为单独的分区。 |
| /lib/       | /bin/ and /sbin/中二进制文件必要的库文件（一般是C语言的库文件）。 |
| /media/     | 可移除媒体(如CD-ROM)的挂载点 (在FHS-2.3中出现)。             |
| /lost+found | 在ext3文件系统中，当系统意外崩溃或机器意外关机，会产生一些文件碎片在这里。当系统在开机启动的过程中fsck工具会检查这里，并修复已经损坏的文件系统。当系统发生问题。可能会有文件被移动到这个目录中，可能需要用手工的方式来修复，或移到文件到原来的位置上。 |
| /mnt/       | 临时挂载的文件系统。比如cdrom,u盘,移动硬盘等，直接插入光驱无法使用，要先挂载后使用 |
| /opt/       | 可选应用软件包的存放目录，用户安装第三方软件，二进制，一般可以选择安装到这里。 |
| /proc/      | 虚拟文件系统，将内核与进程状态归档为文本文件（系统信息都存放这目录下）。例如：uptime、 network。在Linux中，对应Procfs格式挂载。该目录下文件只能看不能改（包括root） |
| **/root/**  | 超级用户root的家目录                                         |
| **/sbin/**  | 必要的系统二进制文件，例如： init、 ip、 mount。sbin目录下的命令，普通用户都执行不了。 |
| **/tmp/**   | 临时文件(参见 /var/tmp)，在系统重启时目录中文件不会被保留。  |
| **/usr/**   | 默认软件都会存于该目录下。用于存储只读用户数据的第二层次；包含绝大多数的(多)用户工具和应用程序。源码程序 |
| **/var/**   | 变量文件——在正常运行的系统中其内容不断变化的文件，如日志，脱机文件和临时电子邮件文件。有时是一个单独的分区。如果不单独分区，有可能会把整个分区充满。如果单独分区，给大给小都不合适。 |



#### 1.1.4远程连接

 **远程连接工具**

界面远程连接工具

向日葵：https://sunlogin.oray.com/download

ToDesk：https://www.todesk.com/index.html



 **终端远程连接工具**

通过SSH连接到远程主机有2种方式：

1. 通过市面上常用的软件来进行连接。

   远程ssh客户端软件：putty（开源免费的，超级轻量级的ssh连接工具），xshell（海螺，收费，但是可以试用）。

   远程ftp客户端软件： xftp，filezilla， FlashFXP

   远程ssh和ftp的客户端合成软件：[FinalShell](http://www.hostbuf.com/t/988.html)、Terminus、[electerm](https://electerm.html5beta.com/)

   touch 文件名

   mkdir 目录名

   rm -rf 要删除内容

2. 通过终端命令来进行ssh连接。首次远程连接会提示记录远程主机的指纹，同意即可。

   基于ssh协议远程登录的命令：ssh、ssh-keygen（免密码登录）

   ```bash
   ssh <用户名>@<ip地址>
   # 例如：远程链接ubuntu
   # ubuntu下查看IP，可以通过命令： ip a
   # ubuntu下查看当前用户：moluo
   ssh moluo@192.168.231.128
   ```

   基于ssh协议进行文件传输的命令：scp

 **SSH**

ssh（ Secure Shell，安全外壳协议），是一种可靠的，专为远程登录会话和其他网络服务提供安全性的协议。最初是UNIX系统上的一个程序，后来又迅速扩展到其他操作平台。简而言之，就是说白了，就是一种网络协议，**用于计算机之间的加密登录**。当然基于ssh协议实现的程序有商业收费的，也有社区免费的。我们可以在windows下安装putty、xshell来帮助我们远程登录，也可以ssh命令来操作。
SSH的默认是22号端口。

```
协议：规定了数据传输双方怎么理解对方发送的数据的一种字符串内容。这份内容就是协议
协议一般用于解决计算机网络中用于传输数据的格式问题的，但是数据传输一定要使用端口的。
端口就是计算机与外界传递数据的进出口，有物理端口和虚拟端口之分。
    物理端口，就是计算机物理的设备端口，例如：usb端口，网线端口，音频端口，麦克风端口
    虚拟端口，就是计算机内部用于接受和发送bytes数据的端口，计算机默认了1-65535个端口
其中，1-1024以内的端口是属于计算机操作的保留端口，一般已经被计算机所预留或占用的。剩余的端口就是提供给开发人员使用。
端口的使用就是基于协议来使用的。一个协议一般就会绑定一个端口作为数据入口。
```



```bash
# 语法：
ssh 用户名@主机地址  # 有时为安全考虑，运维人员会修改ssh端口，则客户端需要指定端口：ssh -p 端口 用户名@主机地址
# 退出ssh远程登录
exit
```

注意，首次使用ssh登录到远程主机，需要手动输入yes记录主机的指纹信息，如下图所示：

![image-20210830122800696](assets\image-20210830122800696.png)



**基于ssh实现免密登录**

所谓的免密登录就是基于rsa非对称加密算法生成一对成对的秘钥对。然后当前主机保管私钥，把公钥上传到远程主机，这样以后登陆时仅需要验证公私钥即可，不再需要密码登陆了。

```bash
# 第一步：生成秘钥对。私钥和公钥成对才能匹配成功，秘钥文件默认保存在~/.ssh/目录下。
# 私钥文件名：id_rsa 
# 公钥文件名：id_rsa.pub
ssh-keygen # 连续三下回车

# 第二步： 将公钥文件信息上传到需要被管理的主机上，远程服务器中的公钥保存目录就在该服务器的家目录下~/.ssh/authorized_keys
ssh-copy-id moluo@192.168.231.128

# windows如果没有这个ssh-copy-id的命令的话，可以安装一个工具来让windows有这个命令。git
```







### 1.2 Linux基础

#### 1.2.1基于ssh实现文件上传下载

scp（secure copy）是一个基于 SSH 协议在网络之间文件进行安全传输的命令。

```bash
# 语法：
# scp [可选参数] 源目录/目标文件  新目录/目标文件
    # 可选参数：
    # -r：递归复制整个目录，强烈建议尽量把目录打包压缩后的上传
    # -v：详细方式输出
    # -q：不显示传输进度条
    # -C：允许压缩
    # -6：使用 IPv6 协议

# 上传本地文件到远程地址
    # scp 本地目录/本地文件  远程用户名@远程ip:远程目录/               # 不修改文件名，直接上传
    # scp 本地目录/本地文件  远程用户名@远程ip:远程目录/远程文件名      # 修改文件名，再上传
    # scp -r 本地目录  远程用户名@远程ip:远程目录
scp -r fsdownload moluo@192.168.231.128:~/Desktop/
win中，先通过cd进入对应得目录下，选择对应得目录，上传，/home/moluo/  绝对路径
可以使用~来代替前面得路径
scp -r test moluo@192.168.17.128:/home/moluo/Desktop/

# 下载远程文件到本地
    # scp 远程用户名@远程ip:远程目录/远程文件名 本地目录/              # 不修改文件名，直接下载
    # scp 远程用户名@远程ip:远程目录/远程文件名 本地目录/本地文件       # 修改文件名，再下载
    # scp -r 远程用户名@远程ip:远程目录 本地目录
scp moluo@192.168.231.128:~/Desktop/fsdownload   ~/Desktop/
```



**vi&vim编辑器**

Gvim 是Windows系统下的版本。下载地址：https://www.vim.org/download.php

Ubuntu默认就内置了vi和vim编辑器，而CentOS则需要单独安装vim：`yum install -y vim`。

![img](D:\人工资料更新\P2新讲义\1-linux基础1-3\assets\vim.png)

![image-20210826090511632](D:\人工资料更新\P2新讲义\1-linux基础1-3\assets\image-20210826090511632.png)

**命令模式**，也叫快捷键模式，在这种模式下，开发者可以通过键盘使用快捷键操作vi/vim编辑器。完成vi编辑器的配置（显示行号、完成一些基本宏操作、复制、粘贴等等操作）。

```bash
x   # 删除光标所在的字符
nd  # n代表数字，表示剪切光标所在位置的后面的n个字符，注意：以空格结束，不要按回车键:5x
dd  # 剪切光标所在行的内容，相当于1dd   
ndd # n代表数字，表示剪切光标所在行的下面n行内容   

yy  # 复制光标所载行的内容
nyy # n代表数字，表示复制光标所在行的下面n行内容
p   # 小写字母，粘贴[在光标下一行粘贴出来]
P   # 大写字母，粘贴[在光标上一行粘贴出来]

u   # 撤销上一步编辑操作

gg  # 光标跳转到第一行
GG  # 光标跳转到最后一行
```

**输入模式**，也叫编辑模式，在这种模式下，开发者可以通过键盘输入文本信息到编辑器中。

​       进入输入模式，可以在命令模式状态下，使用快捷键 i、I、A、a、O、o、S、s、C、c、R 进入。

​        退出输入模式，可以通过ESC键返回命令模式。

```bash
ESC 退出当前模式，进入命令模式
```

**末行模式**，也叫命令行模式/终端模式，在这种模式下，开发者可以通过在编辑器的最后一行输入vi/vim提供的指令完成一系列的编辑器的控制操作，或完成文本的搜索，替换和控制等操作，甚至可以在该模式下，使用Linux提供的shell命令完成来完成其他的命令调用。

​       进入末行模式，可以在命令模式状态下，使用快捷键：冒号进入。

​       退出末行模式，可以通过ESC键返回命令模式。

```bash
# 显示或隐藏文件行号
:set nu
:set nonu

# 跳转到指定行
:行号

# 查找内容
:/内容  # 此时，可以通过键盘中的n（往下）或N（往上）查找匹配项
:?内容

:q  # 退出编辑器，如果没有办法退出，则强制退出
:q! # 强制退出
:w  # 保存内容
:w 文件名 # 把当前内容 另存为 指定文件名

:wq # 先保存内容，接着退出vi编辑器


# 文本替换(支持正则)
:%s/原内容/新内容/   # 把原内容全部替换新内容[部分操作系统下也是替换全部的]
:%s/原内容/新内容/g  # 把原内容全部替换新内容
:%s/原内容//         # 把原内容删除
:%s/原内容//g        # 把匹配到的原内容全部删除[部分操作系统下也是替换全部的]
```



公司里面常用的编辑器：

```bash
前端：sublimetext/webstorm/vscode/atom
后端：
     php: sublimetext/phpstorm/vscode/vim
     python: pycharm/vscode/vim
     java: idea/ecplise/vscode/vim
     go：goland/vscode/vim
     
总结：pycharm/vim/vscode
```



#### 1.2.3用户与权限管理

Linux系统是一个多用户多任务的分时操作系统，任何一个要使用系统资源的用户，都必须首先向系统管理员申请一个账号，然后以这个账号的身份进入系统。Linux默认都会存在着一个超级用户：root。

```bash
其中，Ubuntu是面向个人开发者的Linux，所以Ubuntu原则上不建议使用root权限。
所以在Ubuntu安装过程中，会出现让我们新建账号的情况，所以我们之前创建了一个单独的管理员账号实际上，我们也可以通过这个管理权账号，通过命令`su root` 切换到root账号下面的。
当然，如果首次切换root，会需要输入root的密码，但是一般没有root密码，所以往往需要我们在切换root用户之前，先通过当前管理员修改root的密码。`sudo passwd root`
pwd打印当前工作目录
ls 查看当前目录下所有文件
ll 管理员查看文件记录
rm 文件名，删除文件
```

用户的账号一方面可以帮助系统管理员对使用系统的用户进行跟踪，并控制他们对系统资源的访问；另一方面也可以帮助用户组织文件，并为用户提供安全性保护。

**每个用户账号都拥有一个唯一的用户名和各自的口令(也就是登录密码)**。用户在登录时键入正确的用户名和口令后，就能够进入系统和自己的主目录（也就是家目录，其中root用户的家目录就是/root，而其他管理员的家目录则是/home/用户名）。



实现用户账号的管理，要完成的工作主要有如下几个方面：

-   用户账号的添加、删除与修改。
-   用户口令的管理。
-   用户组的管理。



**用户管理**

linux下的用户，不一定是提供给人使用，还可能提供给软件/程序使用。软件/程序需要操作文件，也是需要用户身份的。

要管理用户，必须使用超级管理员身份！Ubuntu下需要切换到root用户下。

查询系统所有的用户，可以通过`cat /etc/passwd`来查看，里面显示用户的`用户名:x:群组ID:用户ID:组名:家目录:权限`

whoami  查看当前登录用户

-   `useradd`  添加用户
-   `usermod`  修改用户的信息（权限等）
-   `userdel`  删除用户

​	删除得时候，如果出现：user baoguo is currently used by process 13741

​	当前用户正在使用，可以使用 kill -9 13741(这个就是上面提示得数),然后在删除

```bash
# Ubuntu在创建用户以后，新用户是没有家目录的，所以默认的时候，进入了系统根目录！
# 而CentOS则会自动分配权限，新用户拥有自己的家目录。
useradd    xiaohong      # CentOS系统下
useradd -m xiaohong      # Ubuntu系统下，-m 表示生成家目录
# 新用户都需要设置初始密码，否则无法登录
passwd xiaohong  # 接着输入两次密码


# 创建组[创建新用户账户时，如果没分配用户组，则系统会同时创建一个同名的用户组，当前组下只有新账户一个成员]
groupadd pythondev
# 删除组
groupdel pythondev

# 查询系统所有的用户组，可以通过`cat /etc/group`来查看，里面显示用户组的`组名:x:群组ID`
cat /etc/group

# 修改用户信息，让用户加入用户组
# usermod -G 用户组 用户名
groupadd pythondev
usermod -G pythondev xiaohong

# 一个用户可以被添加到多个组中，可以通过`cat /etc/group`来查看
```



**用户组管理**

可以通过`cat  /etc/group`查看当前系统创建了哪些群组

-   `groupadd`
-   `groupmod`
-   `groupdel`

```bash
groupadd 组名
# 查看用户属于哪一个群组下的，有3种方式：
# 查看家目录的文件列表
cd /home
ll
# drwxr-xr-x  3 fuguang fuguang 4096 Aug 30 02:29 fuguang/
# 查看/etc/passwd文件里面的群组ID
cat /etc/group

# 查看用户加入了哪些群组？ groups 用户名
groups xiaoming
# xiaoming : xiaoming fuguang

# 列出一个群组下所有的成员
# grep '组名' /etc/group | awk -F":" '{print $1,$4}'
grep 'pythondev' /etc/group | awk -F":" '{print $1,$4}' # 结果：pythondev xiaohong,moluo
```



**批量管理用户**：

-   成批添加/更新一组账户：`newusers`
-   成批更新用户的口令：`chpasswd`

**组成员管理**：

-   向组中添加用户
    -   `gpasswd -a <用户账号名> <组账号名>`
    -   `usermod -G <组账号名> <用户账号名>`
-   从组中删除用户
    -   `gpasswd -d <用户账号名> <组账号名>`

**密码管理**(禁用、恢复和删除用户密码)：

-   **设置用户密码**：
    -   `passwd [<用户账号名>]`
-   禁用用户账户密码
    -   `passwd -l <用户账号名>`
-   查看用户账户密码状态
    -   `passwd -S <用户账号名>`
-   恢复用户账户密码，与上面的-l禁用相对应
    -   `passwd -u <用户账号名>`
-   清除用户账户密码
    -   `passwd -d <用户账号名>`

**用户切换命令**：

-   `su`
    -   直接切换为超级用户
-   `sudo`
    -   直接使用 sudo 命令前缀执行系统管理命令。执行系统管理命令时无需知道超级用户的口令，使用普通用户自己的口令即可，相当于windows下的“以管理员身份运行”。

![image-20210830103847545](D:\人工资料更新\P2新讲义\1-linux基础1-3\assets\image-20210830103847545.png)



关于文件，Linux下一般针对每个用户和用户不同的身份，对与文件的操作具有以下3种不同的操作权限：

| 权限               | 二进制 | 字母表示 | 八进制 | 对文件的影响   | 对目录的影响                  |
| ------------------ | ------ | -------- | ------ | -------------- | ----------------------------- |
| r（Read, 读取）    | 100    | r        | 4      | 可读取文件内容 | 可列出目录下的所有文件/子目录 |
| w（Write，写入）   | 010    | w        | 2      | 可修改文件内容 | 可在目录中创建删除文件/子目录 |
| x（eXecute，执行） | 001    | x        | 1      | 可作为命令执行 | 可访问目录下的所有文件的内容  |

注意：目录必须拥有 x 权限，否则无法查看目录内部的文件内容了。

Linux下文件的权限记录，针对rwx，采用的是二进制/八进制/字母表示法第三种。

```bash
# Linux下的权限在底层是基于二进制实现的，但是对于外层用户操作时，是可以使用八进制或者字母表示的。
r  w  x    字母表示法
4  2  1    八进制
1  1  1    二进制


# 关于某一个用户对于单个文件的权限，常见有以下几种权限设置：
rwx --> 111  --> 7 表示当前用户对文件拥有可读可写可执行的所有权限
rw- --> 110  --> 6 表示当前用户对文件拥有可读可写的权限
rw- --> 101  --> 5 表示当前用户对文件只拥有可读可执行的权限
r-- --> 100  --> 4 表示当前用户对文件只拥有可读的权限
-wx --> 011  --> 3 表示当前用户对文件只拥有可写可执行的权限
-w- --> 010  --> 2 表示当前用户对文件只拥有可写的权限
--x --> 001  --> 1 表示当前用户对文件只拥有可执行的权限
--- --> 000  --> 0 表示当前用户对文件没有任何操作权限

# Linux下一个文件往往不会仅针对一个用户设置权限，而是针对整个系统下所有用户分配权限，
# 所以一个文件往往会针对当前文件的拥有者、组成员以及其他人同一分配权限的。
# 777  ---> 分别指代3个数字，代表了文件拥有者、文件组成员、其他人的三种身份对于当前文件的操作权限
# rwxrwxrwx  三段rwx，代表了文件拥有者、文件组成员、其他人的三种身份对于当前文件的操作权限，
# 注意：字母表示法中，-表示没有操作权限，二进制和八进制中，0表示没有操作权限
# 举例：
700 => rwx --- --- =>  文件拥有者具有一切(可读可写可执行)权限，组成员和其他人没有任何操作权限【常见于文件】
644 => rw- r-- r-- =>  文件拥有者可读可写，组成员和其他人可读【常见于目录】
755 => rwx r-x r-x =>  文件拥有者具有一切权限，组成员和其他人可读可执行【常见于目录】
777 => rwx rwx rwx =>  任何人都能对当前文件进行任意操作【这种少见，建议慎用！！！】
```

对于ll命令的结果说明（ll 是部分linux提供给用户列出当前目录下所有子文件信息的命令，是 ls -la缩写）

```bash
lrwxrwxrwx   1 root root          9 Feb  1  2021 lib32 -> usr/lib32/
lrwxrwxrwx   1 root root          9 Feb  1  2021 lib64 -> usr/lib64/
lrwxrwxrwx   1 root root         10 Feb  1  2021 libx32 -> usr/libx32/
drwx------   2 root root      16384 Aug 26 04:38 lost+found/
drwxr-xr-x   2 root root       4096 Feb  1  2021 media/
drwxr-xr-x   2 root root       4096 Feb  1  2021 mnt/
drwxr-xr-x   2 root root       4096 Feb  1  2021 opt/
dr-xr-xr-x 279 root root          0 Aug 30 00:23 proc/
drwx------   4 root root       4096 Aug 27 04:41 root/
drwxr-xr-x  27 root root        860 Aug 30 02:29 run/
lrwxrwxrwx   1 root root          8 Feb  1  2021 sbin -> usr/sbin/
drwxr-xr-x   6 root root       4096 Feb  1  2021 snap/
drwxr-xr-x   2 root root       4096 Feb  1  2021 srv/
-rw-------   1 root root 2147483648 Aug 26 05:49 swap.img
dr-xr-xr-x  13 root root          0 Aug 30 00:23 sys/
drwxrwxrwt  12 root root       4096 Aug 30 01:22 tmp/
drwxr-xr-x  14 root root       4096 Feb  1  2021 usr/
drwxr-xr-x  13 root root       4096 Feb  1  2021 var/

ls -l 查看当前所有系统文件
理ll 

# 左边第1个字母，表示文件类型，常见文件类型：目录（d）、文件（-）、链接（l）
# 左边第2~10个字母，表示当前文件拥有者(2~4)、文件组成员(5~7)以及其他人(8~10)对于当前文件的操作权限。

# 命令别名，可以把一些相对比较长，或者参数较多的命令，起一个简单的别名进行调用。
# ll实际上就是ls -la的简写  a-->all
alias ll='ls -la'

# 通过 alias 可以查看当前系统下所有的别名命令。
alias

# 一般工作中，我们为了保证系统安全，往往会设置rm成其他的操作，避免出现误删的情况。
alias rm='echo "rm命令已经被禁用，请改用替换操作：mv"'
# 删除别名
unalias 别名
```



#### 1.2.4文件权限操作

| 命令      | 描述                                         |
| --------- | -------------------------------------------- |
| **chown** | 分配文件给指定用户作为拥有者[需要管理员权限] |
| chgrp     | 分配文件给指定的群组[需要管理员权限]         |
| **chmod** | 分配文件权限给指定用户[需要管理员权限]       |

代码：

```python
# chown # 分配文件给指定用户作为拥有者[需要root权限]
# chown 用户名 文件名
touch demo.txt
chown xiaohong demo.txt          # 把指定文件demo.txt的拥有者分配给xiaohong
chown xiaohong:xiaohong demo.txt # 把指定文件demo.txt的拥有者分配给xiaohong，并分配组给xiaohong用户组

# chgrp 分配文件给指定的群组
# chgrp 组名 文件名
chgrp moluo(组名) js.txt 

# chmod 分配文件权限给指定用户
#   参数选项：
#   -c : 若该文件权限确实已经更改，才显示其更改动作
#   -f : 若该文件权限无法被更改也不要显示错误讯息
#   -v : 显示权限变更的详细资料
#   -R : 对目前目录下的所有文件与子目录进行相同的权限变更(即以递回的方式逐个变更) 最常用

# 基于chmod分配权限一般2种写法：
# 字母表示权限
#     a 表示all，同时给拥有者，组员和其他人分配权限
#     u 表示user，表示给拥有者分配权限
#     g 表示group，表示给组员分配权限
#     o 表示other，表示给其他人分配权限

# 单独给拥有者设置文件的权限为可读可写可执行，组员和其他人的权限没有任何改变
chmod u+rwx demo.txt
# 设置文件权限，拥有者(u)拥有可读可写可执行，组员(g)拥有可读可写，其他人（o）可执行的权限
chmod u+rwx,g+rw,o+r demo.txt   # rwxrw-r--
# 设置文件权限，拥有者(u)移除可执行，组员(g)移除可写，其他人（o）移除可读的权限
chmod u-x,g-w,o-r demo.txt
# 给所有人同时增加或减少权限
chmod a+r demo.txt
chmod a-wrx demo.txt

# 数字表示权限
chmod 777 demo.txt
chmod 755 demo.txt
chmod 644 demo.txt
chmod 700 demo.txt

# 注意：对于系统中的一切权限来说，root都是至高无上的。
```



### 1.3 Linux基础



####  1.3.1常用命令

**系统信息**

| 命令                  | 描述                                                         | ubuntu下的效果/显示             |
| --------------------- | ------------------------------------------------------------ | ------------------------------- |
| arch                  | 显示机器的CPU处理器架构吗，x86_64，x86_32                    | x86_64                          |
| **uname -m**          | 显示机器的CPU处理器架构吗，x86_64，x86_32                    | x86_64                          |
| uname -r              | 显示正在使用的Linux内核版本                                  | 5.8.0-48-generic                |
| dmidecode -q          | 显示硬件系统部件 - (SMBIOS / DMI)                            |                                 |
| hdparm -i /dev/sda    | 罗列指定一个磁盘的架构特性<br>此处的sda表示当前linxu下加载的第一块硬盘，sdb则表示第二块硬盘 |                                 |
| hdparm -tT /dev/sda   | 在指定一个磁盘上执行测试性读取操作                           |                                 |
| **cat /proc/cpuinfo** | 显示CPU info的信息                                           |                                 |
| cat /proc/interrupts  | 显示中断                                                     |                                 |
| **cat /proc/meminfo** | 校验内存使用                                                 |                                 |
| cat /proc/swaps       | 显示哪些swap被使用                                           |                                 |
| **cat /proc/version** | 显示Linux内核的版本和linux发型版本信息                       |                                 |
| cat /proc/net/dev     | 显示网络适配器及统计                                         |                                 |
| cat /proc/mounts      | 显示已加载的文件系统                                         |                                 |
| lspci -tv             | 罗列 PCI 设备                                                |                                 |
| lsusb -tv             | 显示 USB 设备                                                |                                 |
| date                  | 显示系统日期                                                 | Mon 11 Apr 2022 11:37:27 AM CST |
| cal <年份>            | 显示2022年的日历表                                           |                                 |
| date 120810052021.00  | 设置日期和时间 - 月日时分年.秒                               |                                 |
| clock -w              | 执行了data命令修改以后，就要将时间修改结果保存到 BIOS        |                                 |



**系统关机**

关机 (系统的关机、重启以及登出 ) 

| 命令                                | 描述                                            |
| ----------------------------------- | ----------------------------------------------- |
| shutdown -h now                     | 立刻关闭系统                                    |
| init 0                              | 关闭系统                                        |
| telinit 0                           | 关闭系统                                        |
| shutdown -h `<hours>`:`<minutes>` & | 按预定时间关闭系统                              |
| shutdown -c                         | 取消按预定时间关闭系统 [取消上面一句命令的操作] |
| shutdown -r now                     | 立即重启                                        |
| **reboot**                          | 立即重启                                        |
| logout                              | 注销[exit更好用一点]                            |



#### 1.3.2文件和目录

查看文件目录信息

| 命令        | 描述                                           |
| ----------- | ---------------------------------------------- |
| **cd 路径** | 切换当前窗口/应用程序的工作目录                |
| **pwd**     | 打印当前工作目录                               |
| **ls**      | 列出当前工作目录下的所有内容，包括文件，子目录 |
| **tree**    | 以树形结构列出当前工作目录的所有内容           |

tree命令的全称即是“tree”，该命令作用是用于以树状图形式列出目录的内容。 执行tree命令，它会以树状图的方式列出指定目录下的所有文件，包括目录里的文件，显示出指定目录的文件目录结构。

```
sudo apt-get install tree
```



**关于路径(path)的描述**

```python
路径写法分两种：绝对路径和相对路径
绝对路径，从系统的根目录逐层目录进行编写，使用/作为目录分隔符的路径
    windwos: C:/windows/system32/drivers/hosts
    linux:  /etc/hosts
相对路径，从当前窗口/程序作为参考坐标，进行逐层目录进行编写，使用../表示一个上级目录，使用./表示当前目录的路径
./home/1.py   # 表示在当前文件/窗口/程序同级目录有个文件1.py
home/1.py     # 此处同上，一般路径没有以/开头，或者没有判断，则表示当前路径是简写了./
../../home/1.py  # 表示在当前文件/窗口/程序上2级目录下有个home目录下有个文件1.py

# 练习：
|── 3.py
└── 2022/
    ├── 05/
    │   └── 04/
    │       └── 1.py
    └── 06/
        └── 2.py

# 1. 如果在3.py中，要使用路径表示1.py的文件位置?
./2022/05/04/1.py
2022/05/04/1.py  # 省略./也可以
# 2. 如果在3.py中，要使用路径表示2.py的文件位置?
./2022/06/2.py
2022/06/2.py    # 省略./也可以
# 3. 如果在2.py中，要使用路径表示1.py的文件位置?
../05/04/1.py
# 4. 如果在2.py中，要使用路径表示3.py的文件位置?
../../3.py
# 5. 如果在1.py中，要使用路径表示2.py的文件位置?
../../06/2.py
# 6. 如果在1.py中，要使用路径表示3.py的文件位置?
../../../3.py
# 7. 如果3.py的绝对路径是/home/moulo/Desktop/3.py，那么，1.py和2.py的绝对路径?
/home/moulo/Desktop/2022/05/04/1.py
/home/moulo/Desktop/2022/06/2.py

# 路径从终点的文件类型来区分的话，也分两种：目录路径，文件路径
/home/       # 目录路径，因为home可能是一个目录
/home/1.py   # 文件路径，因为1.py可能是1个文件


# 路径从是否使用网络协议来说，也分两种：网络路径，本地路径
网路路径格式：   网络协议://IP或域名/目录路径/文件名
                https://img12.360buyimg.com/pop/1a763aeafe753ebf.jpg

本地路径格式：   file:///C:/python37/课件笔记/day18-Linux基础
                C:/python37/课件笔记/day18-Linux基础
```



命令演示：

```bash
cd /home # 进入 '/home' 目录'
cd .. # 返回上一级目录 
cd ../.. # 返回上两级目录 
cd    # 相当于 cd ~ ，进入个人的主目录 
cd ~  # 进入个人的主目录 
cd -  # 返回上次所在的目录 
pwd   # 显示工作路径 
ls    # 查看目录中的文件 
# ls -F # 查看目录中的文件 
ls -l # 显示文件和目录的详细资料 
ls -la # 显示隐藏文件，以列表格式展示，一般被命名别名为 ll
ls *[0-9]* # 显示包含数字的文件名和目录名 
tree # 显示文件和目录由根目录开始的树形结构
     # ubuntu:   sudo apt install tree
     # centos:   yum install tree
     # maxOS :   brew install tree
     
tree -L 2   # 仅列出2层目录信息
```



**管理文件目录**

目录路径相关的命令

| 命令                          | 描述                                                         |
| ----------------------------- | ------------------------------------------------------------ |
| **mkdir 目录名1  目录名2...** | 根据指定名称，创建1个或多个空目录                            |
| **touch 文件名1  文件名2...** | 根据指定名称，创建1个或多个文件                              |
| **echo 文本内容**             | 往标准输出中写入文本内容（其实就是往终端打印指定文本内容）   |
| **>**                         | 管道符，表示把左边命令输出的结果作为内容清空写入到右边的文件中 |
| >>                            | 管道符，表示把左边命令输出的结果作为内容追加写入到右边的文件中 |
| **rm**                        | 删除文件或目录                                               |
| **mv**                        | 重命名或移动文件或目录                                       |
| **cp**                        | 复制文件或目录                                               |
| **命令语句 && 命令语句 ...**  | 表示上一个命令执行结束以后，直接执行下一个命令语句           |

命令演示：

```bash
mkdir dir1 # 创建一个叫做 'dir1' 的目录' 
mkdir dir1 dir2 ....   # 同时创建两个同级目录或多个同级目录
# 序列
# {dir3,dir4,dir5}      # 指定成员的序列
mkdir {dir3,dir4,dir5}  # 创建了3个目录，分别是dir3,dir4,dir5
# mkdir dir{6..10}      # 指定成员范围的序列
mkdir dir{6..10}         # 创建了dir1,dir2,dir3这个范围的目录
mkdir demo{01..100}      # 指定成员的长度补0，按末尾数字的长度，给所有的数字进行补0，不足2位，左边补1个0
mkdir user{001..3}       # 创建user001,user002,user003这几个目录
# mkdir goods{0..10..2} # 指定步进值的序列，步进值表示间隔数值
mkdir item{00..10..2}   # 创建goods00,goods02,goods..,goods10之间的偶数目录
mkdir -p 2022/{05..8}/{01..10}
mkdir -p ~/dir0/dir1/dir2 # 创建一个目录树[多级目录]

touch 1.html           # 创建一个空内容文件
touch 1.html 2.html    # 创建2个空内容文件，分别是1.html和2.html
touch {00..10..2}.html # touch也支持序列格式写法
touch demo/{00..10..2}.html # 在指定路径下根据序列创建多个文件，前提是路径是存在的

echo  > 2.py              # 创建一个有内容的文件2.py，里面是空白内容 
echo hello world > 3.py   # 创建一个有内容的文件3.py，里面的内容是 hello world
echo welcome to beijing > 3.py # 往3.py文件中追加写入内容

rmdir dir1       # 删除一个叫做 'dir1' 的目录'，rmdir只能删除空目录！，如果目录下有内容，则无法删除！！
# 如果要删除一个有内容的目录，则可以使用rm进行删除
# 当然要注意: 在工作中rm比较危险，绝对禁用的！！！建议使用mv代替！
rm 1.html        # 删除文件，文件名为 1.html
rm -f 2.html     # 无须确认，直接删除一个叫做 '2.html' 的文件' 
rm -rf python01          # 递归删除一个叫做 'python01' 的目录及其内容，慎用！~！！ 
rm -rf python02 python03 # 同时删除两个目录及它们的内容，慎用
rm -rf ./*  删除当前文件中所有内容
rm -rf /* 从根目录挨个删除，切记，全部删除，慎用
# rm -rf {05..07}
mv python04 python04.bakup  # 重命名/移动一个文件/目录，或者对文件进行改名，
                     # 当python04.bakup不存在时，则表示把python04重命名为python04.bakpu
                     # 当python04.bakup已经存在，则表示把python04移动到python04.bakpu目录下
                     # 如果要恢复，则参数翻转即可，mv python04.bakup python04

mv goods-* demo1/    # 重命名/移动所有以dir开头的文件/目录，或者对文件进行改名
                     # 当new_dir不存在时，则报错！

# 多条命名按先后顺序一并执行
touch {01..10}.py && mkdir -p old_dir && mv *.py old_dir && tree old_dir

cp 1.html 1.html.bakup        # 复制一个文件1.html，新文件名为 1.html.bakup，工作中常用
先创建两个对应得文件夹
cp old_dir/* new_dir/         # 复制一个目录下的所有文件到当前工作目录下的new_dir目录中 
cp -a /tmp/dir1 . # 复制一个目录到当前工作目录 
cp -a dir1 dir2 # 复制一个目录 
cp -r dir1 dir2 # 递归复制一个目录及子目录
```



**文件搜索**

| 命令                       | 描述                                                   |
| -------------------------- | ------------------------------------------------------ |
| **find 查找路径 选项参数** | 逐层目录逐个查找文件，建议用于小范围查找，不要全盘查找 |
| locate 文件名              | 按文件数据库信息快速查询文件，要安装命令才可用         |
| **whereis 文件名**         | 查找二进制文件，提供所有能找到的信息                   |
| which 文件名               | 查找二进制文件，提供路径                               |



```bash
find /home -name "*.py"      # 从 '/home'家目录开始进入文件系统搜索名称以'.pt'结尾的文件和目录
find /home -name "*python*"    # 从 '/home' 开始进入文件系统搜索名称包含'python'的文件和目录
find /home -name "demo*"       # 从 '/home' 开始进入文件系统搜索名称以'demo'开头的文件和目录
find / -name "*demo*"          # 不建议使用，从 '/' 开始进入根文件系统搜索名称包含'demo'的文件和目录

    [root@localhost ~]# find / -name "demo*"
    touch /home/moluo/demo001/demo.txt
    /root/dir9/demo.txt
    /root/dir007/dir6/demo.txt
    /root/dir007/demo333.txt
    /root/dir007/demo333_bak.txt
    /root/dir007/dir006/demo.txt

find ~ -user "root"            # ~表示当前用户家目录，搜索属于用户 'root' 的文件和目录 
find /etc/systemd -type f -atime +100  # 从'/etc/systemd'开始，搜索在过去100天内未被使用过的执行文件 
find /home/moluo/Desktop/ -type f -mtime -10  # 从'/home/moluo/Desktop'开始，搜索在10天内被创建或修改过的文件
find /home/moluo/Desktop/ -type d -mtime -10  # 从'/home/moluo/Desktop'开始，搜索在10天内被创建或修改过的目录

# find搜索文件，是逐个目录进行查找， 所以尽量不要从根目录下去进行全盘查找，否则系统会卡顿的！！

# ContOS安装软件、命令:  yum install -y mlocate
# Ubuntu安装软件、命令： sudo apt install -y mlocate
# 使用locate之前，要了解locate内部运行原理：locate执行过程中，直接系统数据库中搜索文件信息的，效率贼高！
# 所以，需要更新以下最近的系统的文件数据库，先运行 'updatedb' 命令，ubuntu下需要以sudo 开头
sudo updatedb
locate *.html  # 寻找以 '.html' 结尾的文件 -  

# 查找二进制文件、例如命令，查找源码包或者命令手册时使用whereis
whereis tree  # 显示一个二进制文件、源码或man的位置 

# 查找二进制文件、例如命令、可执行程序
which tree    # 显示一个二进制文件或可执行文件的完整路径 
```



**查看文件内容**

| 命令        | 描述                                                |
| ----------- | --------------------------------------------------- |
| **wc**      | 统计指定文件/指定目录的总行数/总单词数/总字符数量。 |
| **cat**     | 查看内容[从头到尾]，适用于小文件                    |
| tac         | 查看内容[从尾到头]，适用于小文件                    |
| **more**    | 查看内容，适用于大文件，只能从上往下查看            |
| **less**    | 查看内容，适用于大文件，提供上下查看的操作          |
| **head**    | 查看文件开始部分的内容                              |
| **tail**    | 查看文件结束部分的内容                              |
| **tail -f** | 实时监控文件内容                                    |

```bash
# 准备测试数据
echo "hello
world 
python
baidu" > demo.txt                # 把"hello\nworld" 写入到demo.txt中
cat demo.txt                     # 从第一个字节开始正向查看文件'demo.txt'的内容
                                 # cat只适合用于查看小文件的内容，大文件不适合.
cat -n demo.txt                  # 显示当前文件的内容和行数
tac demo.txt                     # 从最后一行开始反向查看文件'demo.txt'的内容

# 统计文件内容的字数/单词/行数
wc demo.txt                 # 统计demo.txt文件的行数/单词数/字数
wc demo.txt  /etc/passwd    # 统计多个文件的行数/单词数/字数，并汇总。

    [root@localhost dir8]# wc demo.txt /etc/passwd
   行数 单词数 字数  文件路径
	1    3       19 demo.txt
    23   47     1127 /etc/passwd
    24   50     1146 总用量                # 末行表示汇总

# wc还可以统计指定目录下的所有文件的内容
 wc ./*     # 表示统计当前目录下所有内容
行数 单词数 字数  文件路径
 1    3    19     ./1.py
 1    3    18     ./2.py
 4    4    26     ./demo.txt
 6    10   63     总用量


# 写入大段内容到文件中
cat << AAA >> demo2.txt
青青园中葵，朝露待日晞。
阳春布德泽，万物生光辉。
常恐秋节至，焜黄华叶衰。
百川东到海，何时复西归？
少壮不努力，老大徒伤悲。

青青园中葵，朝露待日晞。
阳春布德泽，万物生光辉。
常恐秋节至，焜黄华叶衰。
百川东到海，何时复西归？
少壮不努力，老大徒伤悲。
AAA

# 查看全部内容
more demo2.txt # 翻页，查看大文件"demo.txt"的内容，按空格键可以继续往下翻看数据,Q键退出
less demo2.txt # 类似于 'more' 命令，但是它允许在文件中和正向操作一样的反向操作，上下键控制内容，Q键退出

# 查看部分内容
head -4 demo2.txt # 查看文件的前4行,4不是固定的，表示行数
tail -2 demo2.txt # 查看一个文件的最后2行, 2不是固定的，表示行数 

# 实时查看'/var/log/messages'系统运行信息文件的内容 
tail -f /var/log/messages   # centos
tail -f /var/log/syslog     # ubuntu
```



#### 1.3.3文本处理

| 命令     | 描述           |
| -------- | -------------- |
| **grep** | 文件搜索       |
| **sed**  | 替换查找       |
| **awk**  | 分割处理       |
| paste    | 合并文件内容   |
| sort     | 对内容进行排序 |

```bash
# Linux的文本处理->3剑客：grep, sed, awk 是最强大的三个文本处理命令

# grep  文本搜索，支持正则使用
# 用法1，从文件中搜索关键字
#        grep 关键字 文件
# 用法2，从上一个操作命令的结果内容中，提取关键字信息
#        上一个命令 | grep 关键字

grep '老大' demo2.txt
grep "老大" /home/moluo/Desktop/demo2.txt  # 在文件 '/home/moluo/Desktop/demo2.txt'中查找包含"老大"的内容 
grep ^world /home/moluo/Desktop/demo.txt   # 在文件 '/home/moluo/Desktop/demo.txt'中查找以"world"开头的内容
grep world$ /home/moluo/Desktop/demo.txt   # 在文件 '/home/moluo/Desktop/demo.txt'中查找以"world"结尾的内容

grep [0-9] /home/moluo/Desktop/demo.txt # 在文件 '/home/moluo/Desktop/demo.txt'中查找包含数字的内容 

grep welcome -R /home/moluo/Desktop/*   # 在目录 '/home/moluo/Desktop/'以及子目录中的所有文件内容中 搜索字符串"welcome"

# ps aux 用于查看Linux系统中所有正在启动的进程。相当于windows下的任务管理器中的进程数据
ps aux | grep chrome$         # 先列出当前操作系统中运行的所有进程列表信息以及PID，
                              # 然后从结果中搜索关键字chrome结尾的内容信息

# | 要是一个管道符，把左边命令的输出结果作为内容，提供给右边的命令作为参数使用。


# sed 文本的查看、删除、替换，支持正则使用。
echo "
hello world
welcome to beijing。
hello world
welcome to shanghai。
hello world
welcome to beijing。
" > demo.txt

# 不修改源文件，针对文件内容输出到终端时进行替换
sed "s/hello world/Hi, xiaoming/g" demo.txt    # 先将demo.txt文件内容提取出来，
                                               # 再把内容中的 "hello world" 替换成 "Hi, xiaoming"以后
                                               # 输出到终端，不修改源文件的内容
sed "s/hello world/Hi, xiaoming/g" demo.txt > demo2.txt # 在上面命令的基础上，把替换后的内容写入新文件demo2.txt中

# 替换源文件内容
sed -i "s/hello world/Hi, xiaoming/g" demo.txt # 将demo.txt中的 "hello world" 替换成 "Hi, xiaoming"，
                                               # 并修改源文件内容。
sed '/^$/d' demo2.txt         # 从demo2.txt文件中删除所有空白行，并显示内容，不修改文件内容
sed -i '/^$/d' demo2.txt      # 从demo2.txt文件中删除所有空白行，并修改文件内容

# 准备测试文件
cat << EOF >>demo3.py
from rest_framework.viewsets import ViewSet
# 首页视图类
class HomeViewSet(ViewSet):
    def get_banner(self,request):
        # 获取banner列表数据
        pass		
    def get_nav(self, request):
        # 获取导航数据
        pass
EOF

# 整行删除
sed "/^ *#/d" demo3.py   # 从demo3.py文件中删除以空格+#号开头的行内容或者是以#号开头的行内容
sed "/^ *#/d; /pass/d" demo3.py  # 从demo3.py文件中删除注释行和pass关键字所在行
sed '/ *#/d; /^$/d' demo3.py    # 从demo3.py文件中删除所有注释和空白行，常用于代码压缩

# 删除一行的部分内容
sed -e 's/ *$//' demo3.py       # 删除每一行最后的空白字符 
sed -e "s/#.*//" demo3.py       # 删除文件中每一行以#开头的部分内容
sed -e "s/#.*//; /^ *$/d" demo3.py | wc  # 删除文件demo3.py中所有注释和空白，输出结果作为wc的参数进行统计 
sed -e 's/xiaoming//g' demo3.py  # 从文档demo3.py中只删除"xiaoming"并保留剩余全部

# 根据关键字查看内容
sed -n '/from/p' demo3.py       # 查看demo3.py文件中，包含导包关键字from的行内容 
sed -n "/def/p" demo3.py        # 查看demo3.py文件中，包含定义函数关键字def的行内容

# 指定行查看内容
sed -n '2,4p;4q' demo.txt        # 查看从第2行到第4行内容
sed -n '5p;5q'   demo.txt        # 只查看第5行 


# awk 按换行、按空格处理文本, 按列处理文本内容
# awk会根据文本内容，按空格进行分列，$1,表示第一列,$2表示第二列,以此类推... print表示打印
echo "hello world xiaoming" | awk '{print $1,$3}'  # 输出文本的第1和第3列
# hello xiaoming
echo "hello world xiaoming" | awk '{print $1,$2}'  # 输出文本的第2和第2列
# hello world
echo "hello world xiaoming" | awk '{print $1,$2, $3}' # 输出文本的第1,2,3列
# hello world xiaoming
echo "hello world xiaoming" | awk '{print $1,$3, $2}' # 输出文本的第1,3,2列，可以自己排序。
# hello xiaoming world
echo "hello world xiaoming" | awk '{print $1,$3}' > 1.txt  # 把awk处理的结果写入到文件1.txt中

# 读取文件1.txt的内容，把每一行按空格分列，输出第2列的内容
cat 1.txt | awk '{print $2}'

# NR表示行号
cat demo.txt | awk 'NR%2==1'  # 读取文件demo.txt的内容，输出奇数行内容


# 准备测试内容和文件
echo "hello" > t1.txt
echo " world" > t2.txt
# 合并文件内容
paste t1.txt t2.txt  # 合并2个文件的内容，并打印
paste t1.txt t2.txt > t3.txt  # 合并2个文件的内容，把合并内容记录到t3.txt中

# 对内容进行排序和查看内容是否重复的作用
sort t1.txt t2.txt      # 排序两个文件的内容
echo "hello" >> t2.txt  # 追加内容"hello" 到 t2.txt
sort t1.txt t2.txt | uniq  # 取出两个文件的并集(重复的行只保留一份) 
sort t1.txt t2.txt | uniq -u # 删除交集，留下其他的行 
sort t1.txt t2.txt | uniq -d # 取出两个文件的交集(只留下同时存在于两个文件中的文件)
```



#### 1.3.4打包压缩文件 

```bash
# 基于bzip算法压缩文件内容，不能压缩目录！！！生成的文件后缀.bz2
bzip2 demo.txt        # 压缩一个叫做 'demo.txt' 的文件，得到压缩包，demo.txt.bz2
bunzip2 demo.txt.bz2 # 解压一个叫做 'demo.txt.bz2'的文件

# 基于gzip算法压缩文件，压缩程度把上面的要好，gzip可以针对文件进行打包
# 最常用
gzip demo.txt       # 压缩一个叫做 'demo.txt'的文件，得到压缩包，demo.txt.gz
gunzip demo.txt.gz  # 解压一个叫做 'demo.txt.gz'的文件 
gzip -9 demo.txt    # 最大程度压缩，默认就是最大程度压缩

# 基于rar针对文件或目录打包
# ContOS安装:
#        wget https://www.rarlab.com/rar/rarlinux-x64-6.0.2.tar.gz
#        tar zxvf rarlinux-x64-6.0.2.tar.gz -C /usr/local
# Ubuntu安装：
#        sudo apt install rar
rar a day18.rar day18           # 打包day18目录，并创建一个叫做 'day18.rar' 的包，并没有压缩
rar a day18.rar file1 file2 dir1 # 同时把多个文件或目录一起追加打包到day18.rar的包中 
rar x day18.rar  # 解压rar包

# 基于tar针对文件或目录打包，Linux最常用这个
tar -cvf day18.tar day18                   # 创建一个非压缩的 day18.tar的包 
tar -cvf day18.tar file1 file2 dir1        # 把多个文件或目录追加打包到day18.tar中
tar -tf  day18.tar                         # 显示一个包中的内容
# ar -tf  day18.tar | grep md              # 显示包中的内容并使用grep进行过滤查找

tar -xvf day18.tar # 释放一个包，解包
tar -xvf demo.tar -C 001/ # 将包释放到 001 目录下，前提是001目录是存在的

tar -jcvf day18.tar.bz2 day18   # 创建一个bzip2格式的压缩包，压缩包的文件名，往往会体现打包格式以及压缩算法 
tar -jxvf day18.tar.bz2         # 解压一个bzip2格式的压缩包 
mkdir -p 001 && tar -jxvf day18.tar.bz2 -C 001/   # 创建一个目录001，并把压缩包解压到001目录下

# 重要！最常用的打包压缩命令！
tar -zcvf day18.tar.gz day18   # 创建一个gzip格式的压缩包 
tar -zxvf day18.tar.gz          # 解压一个gzip格式的压缩包

mkdir -p 002 && tar -zxvf day18.tar.gz -C 002/  # 创建一个目录002，并把压缩包解压到002目录下

# zip
zip -r day18.zip day18 # 创建一个zip格式的压缩包 
zip -r day18.zip file1 file2 dir1 # 将几个文件和目录追加压缩到一个zip格式的压缩包 
unzip day18.zip # 解压一个zip格式压缩包 
```

## **四、本单元知识总结**

```python
1.linux基本使用
2.linux用户组权限配制

```

