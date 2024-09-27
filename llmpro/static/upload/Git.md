# 第一单元  Liunx

## **一、昨日知识点回顾**

```python
无
```

------

## **二、考核目标**

```
1.git基本使用
2.git创建分支
3.git解决冲突
```

------

## **三、本单元知识详讲**

### 1 Git基础介绍

- Git 是目前世界上最先进的分布式版本控制系统（没有之一）

#### 1.1作用

- 源代码管理
  - Git是一个开源的分布式版本控制系统，可以有效、高速地处理从很小到非常大的项目版本管理。 也是Linus Torvalds为了帮助管理Linux内核开发而开发的一个开放源码的版本控制软件。

#### 1.2为什么要进行源代码管理?

- 方便多人协同开发
- 方便版本控制

#### 1.3Git的诞生

- 作者是 Linux 之父：Linus Benedict Torvalds
- 当初开发 Git 仅仅是为了辅助 Linux 内核的开发（管理源代码）

![img](D:\人工资料更新\P3新讲义\day01-git和linux基础\images\李纳斯.png)

> git 开发时间表
>
> - git 的产生是 Linux Torvals 在无奈被逼的情况下创造的，我看了一下时间历程：
>   - 2005 年 4 月3 日开始开发 git
>   - 2005 年 4 月 6 日项目发布
>   - 2005 年 4 月 7 日 Git 开始作为自身的版本控制工具
>   - 2005 年 4 月 18 日发生第一个多分支合并
>   - 2005 年 4 月 29 日 Git 的性能达到 Linux 预期
>   - 2005年 7 月 26 日 Linux 功成身退，将 Git 维护权交给 Git 另一个主要贡献者 Junio C Hamano，直到现在
>
> Git 迅速成为最流行的分布式版本控制系统，尤其是 2008 年，GitHub 网站上线了，它为开源项目免费提供 Git 存储，无数开源项目开始迁移至 GitHub，包括 jQuery，PHP，Ruby 等等
>
> 国内从2013年 Gitee 代码托管平台上线至推出企业版之前的三年多时间中，Gitee 平台已托管了 2000 万+个仓库，是国内知名的代码托管平台。

#### 1.4Git管理源代码特点

- 1.`Git`是分布式管理.服务器和客户端都有版本控制能力,都能进行代码的提交、合并、...

  ![img](D:\人工资料更新\P3新讲义\day01-git和linux基础\images\分布式版本控制.png)

- 2.`Git`会在根目录下创建一个`.git`隐藏文件夹，作为本地代码仓库

  ![img](D:\人工资料更新\P3新讲义\day01-git和linux基础\images\本地仓库.png)

#### 1.5Git操作流程图解

```
Git服务器 --> 本地仓库 --> 客户端 --> 本地仓库 --> Git服务器
```

![img](images\GIT操作图解.png)





### 2 工作区暂存区和仓库区介绍

![img](images\u=2718557050,2037552554&fm=253&app=138&f=JPEG)

#### 2.1 工作区

- 对于`添加`、`修改`、`删除`文件的操作，都发生在工作区中

#### 2.2 暂存区

- 暂存区指将工作区中的操作完成小阶段的存储，是版本库的一部分

#### 2.3 仓库区

- 仓库区表示个人开发的一个小阶段的完成
  - 仓库区中记录的各版本是可以查看并回退的
  - 但是在暂存区的版本一旦提交就再也没有了

操作流程

~~~
1.https://gitee.com/注册账号，用英文用户名和密码
2.选择新建仓库，选择开源
3.保存 git config --global user.name "zhangsan"
  git config --global user.email "zhangsan@163.com"
  
4.进入仓库，复制 git clone git@gitee.com:flyweiweiwei/h2403model.git
5.在本地创建一个文件夹  p3
6. cd  p3执行 git clone git@gitee.com:flyweiweiwei/h2403model.git
7.修改添加代码
8.git add test.py
9. git commit -m '注释'
10. git push 将代码推送到服务器
11. git pull 下载服务器代码
~~~



### 3 Git单人本地仓库操作

- 课程目标：学习常用的Git终端命令
- 提示：本地仓库是个`.git`隐藏文件

> 以下为演示Git单人本地仓库操作

#### **3.1 安装git**

```
 Linux中安装操作，window中请下载安装包直接安装
 sudo apt-get install git
  密码：Linux密码
```

![img](images/安装Git.png)

#### 3.2**查看git安装结果**

```
  git -v
```

![image-20240221114917540](images\image-20240221114917540.png)

#### 3.3**创建项目**

- 首页创建对应存放文件夹，表示是工作项目

  ```
    通过 cd d/work/test/
    进入到对应目录下
  ```

#### **3.4 创建本地仓库**

1. 进入到`test`，并创建本地仓库`.git`

2. 新创建的本地仓库`.git`是个空仓库

   ```
     git init
   ```

   ![img](images/创建本地仓库.png)

3. 创建本地仓库`.git`后

   ![img](images/空仓库.png)

   <img src="images\image-20240221115215325.png" alt="image-20240221115215325" style="zoom: 50%;" />

> 进入该待显示的文件路径，ctrl + h ，则显示隐藏文件

#### **3.5 配置个人信息**

```
  git config --global user.name "zhangsan"
  git config --global user.email "zhangsan@163.com"
```

![img](images/配置个人信息.png)

- 配置个人信息后

  ![img](images/配置个人信息后.png)

> 默认不配置的话，会使用全局配置里面的用户名和邮箱
> 全局git配置文件路径：~/.gitconfig

#### **3.6 新建py文件**

- 在项目文件`test`里面创建`login.py`文件，用于版本控制演示

  ![img](images/项目文件详情.png)

#### **3.7 查看文件状态**

- 红色表示新建文件或者新修改的文件,都在工作区.

- 绿色表示文件在暂存区

- 新建的`login.py`文件在工作区，需要添加到暂存区并提交到仓库区

  ```
  git status
  ```

  ![img](images/查看文件状态.png)

#### **3.8 将工作区文件添加到暂存区**

```
  # 添加项目中所有文件
  git add .
  或者
  # 添加指定文件
  git add login.py
```

![img](images/添加到暂存区.png)

#### **3.9 将暂存区文件提交到仓库区**

- `commit`会生成一条版本记录

- `-m`后面是版本描述信息

  ```
  git commit -m '版本描述'
  ```

  ![img](images/提交到仓库区.png)

#### **3.10 接下来就可以在**`login.py`**文件中编辑代码**

- 代码编辑完成后即可进行`add`和`commit`操作

- 提示：添加和提交合并命令

  ```
    git commit -am "版本描述"
  ```

- 提交两次代码，会有两个版本记录

  ![img](images/两次版本提交.png)

#### **3.11查看历史版本**

```
  git log
  或者
  git reflog
```

![img](images/查看历史记录log.png)

> git reflog 可以查看所有分支的所有操作记录（包括commit和reset的操作），包括已经被删除的commit记录，git log 则不能察看已经删除了的commit记录

#### **3.12 回退版本**

- **方案一：**

  - `HEAD`表示当前最新版本

  - `HEAD^`表示当前最新版本的前一个版本

  - `HEAD^^`表示当前最新版本的前两个版本，**以此类推...**

  - `HEAD~1`表示当前最新版本的前一个版本

  - `HEAD~10`表示当前最新版本的前10个版本，**以此类推...**

    ```
    git reset --hard HEAD^
    ```

    ![img](images/回退版本HEAD.png)

    ![img](images/回退版本后HEAD.png)

- **方案二：当版本非常多时可选择的方案**

  - 通过每个版本的版本号回退到指定版本

    ```
      git reset --hard 版本号
    ```

    ![img](images/回退版本版本号.png)

    ![img](images/回退版本后版本号.png)

#### **3.13 撤销修改**

- 只能撤销工作区、暂存区的代码,不能撤销仓库区的代码

- 撤销仓库区的代码就相当于回退版本操作

  - 撤销工作区代码

    - 新加代码`num3 = 30`，不`add`到暂存区，保留在工作区

      ```
      git checkout 文件名
      ```

      ![img](images/撤销工作区代码前.png)

      ![img](images/撤销工作区代码后.png)

  - 撤销暂存区代码

    - 新加代码`num3 = 30`，并`add`到暂存区

      ```
      # 第一步：将暂存区代码撤销到工作区
      git reset HEAD  文件名
      # 第二步：撤销工作区代码
      git checkout 文件名
      ```

      ![img](images/撤销暂存区代码.png)







### 4 Git远程仓库Github

#### 4.1 创建远程仓库

> 以下操作为演示在Gitee网站上创建远程仓库

- 1.登陆注册Gitee
- 2.创建仓库入口
- ![image-20240221115630458](images\image-20240221115630458.png)
- 3.编辑仓库信息
- ![image-20240221115840698](images\image-20240221115840698.png)
- 4.仓库创建完成
- ![image-20240221115918727](images\image-20240221115918727.png)
- 5.查看仓库地址
  - ![image-20240221120000741](images\image-20240221120000741.png)



#### 4.2 配置SSH

选择SSH操作,添加公钥

![image-20240221120105317](images\image-20240221120105317.png)

- 如果某台电脑需要与`Github`上的仓库交互，那么就要把这台电脑的SSH公钥添加到这个`Gitee账户上

- 1.配置SSH公钥入口

  ![image-20240221120206584](images\image-20240221120206584.png)

- 2.生成SSH公钥

  ```
  Windows 用户建议使用 Windows PowerShell 或者 Git Bash，在 命令提示符 下无 cat 和 ls 命令。
  1、通过命令 ssh-keygen 生成 SSH Key：
  ssh-keygen -t ed25519 -C "Gitee SSH Key"
  
  -t key 类型
  -C 注释 
  ```

  输出，如：

  ```bash
  Generating public/private ed25519 key pair.
  Enter file in which to save the key (/home/git/.ssh/id_ed25519):
  Enter passphrase (empty for no passphrase):
  Enter same passphrase again:
  Your identification has been saved in /home/git/.ssh/id_ed25519
  Your public key has been saved in /home/git/.ssh/id_ed25519.pub
  The key fingerprint is:
  SHA256:ohDd0OK5WG2dx4gST/j35HjvlJlGHvihyY+Msl6IC8I Gitee SSH Key
  The key's randomart image is:
  +--[ED25519 256]--+
  |    .o           |
  |   .+oo          |
  |  ...O.o +       |
  |   .= * = +.     |
  |  .o +..S*. +    |
  |. ...o o..+* *   |
  |.E. o . ..+.O    |
  | . . ... o =.    |
  |    ..oo. o.o    |
  +----[SHA256]-----+
  ```

  - 中间通过三次**回车键**确定

  2、查看生成的 SSH 公钥和私钥：

  ​		ls ~/.ssh/

  ![image-20240221120406286](images\image-20240221120406286.png)

  

- 配置SSH公钥

​		复制生成后的 ssh key，通过仓库主页 **「管理」->「部署公钥管理」->「添加部署公钥」** ，将生成的公钥添		加到仓库中。

![添加部署公钥](images\deploy_keys_create-da41d7ed1687833a3d8652f9e753d7d7.png)

- ![image-20240221120524537](images\image-20240221120524537.png)

#### 4.3 克隆项目

- 准备经理的文件 `Desktop/manager/`
- 准备张三的文件 `Desktop/zhangsan/`

经理的工作

- 立项：克隆远程仓库+配置身份信息+创建项目+推送项目到远程仓库

- 1.克隆远程仓库的命令

  ```
    cd Desktop/manager/
    git clone https://github.com/test01/info.git
  ```

- 2.克隆远程仓库到本地

  <img src='images/github经理克隆远程仓库02.png'>

- 3.克隆成功后查看经理的文件

  <img src="images/github经理克隆远程仓库成功后.png">

- 4.配置经理身份信息

  ```
    cd Desktop/jingli/info/
    git config user.name '经理'
    git config user.email 'jingli@jiyun.com'
  ```

  <img src="images/github经理配置个人信息后.png">

- 5.创建项目

  <img src="images/github经理创建项目.png">

- 6.推送项目到远程仓库

  ```
    # 工作区添加到暂存区
    git add .
    # 暂存区提交到仓库区
    git commit -m '立项'
    # 推送到远程仓库
    git push
  ```



- 在 push 的时候需要设置账号与密码，该密码则是 gitee 的账号与密码

张三的工作

- 获取项目：克隆项目到本地、配置身份信息

- 1.克隆项目到本地

  ```
    cd Desktop/zhangsan/
    git clone https://github.com/zhangsan/info.git
  ```

  <img src="images/github张三克隆远程仓库02.png">

- 2.克隆成功后查看张三的文件

  <img src="images/github张三克隆远程仓库后.png">

- 3.配置张三身份信息

  ```
    cd Desktop/zhangsan/info/
    git config user.name '张三'
    git config user.email 'zhangsan@jiyun.com'
  ```

> 张三身份信息配置成功后即可跟经理协同开发同一个项目



#### 4.4 多人协同开发

- 1.代码编辑界面介绍：此处使用`gedit`做演示

  - 代码编辑界面左边为模拟经理的操作

  - 代码编辑界面右边为模拟张三的操作

    <img src="images/github代码编辑界面介绍.png">

- 2.模拟张三先编辑`login.py`文件代码

  - 进入张三本地仓库：`cd Desktop/zhangsan/info`

  - 编辑代码：`num1 = 10`

  - 本地仓库记录版本：`git commit -m '第一个变量'`

  - 推送到远程仓库：`git push`

    <img src="images/github张三编辑num1.png">

    <img src="images/github张三编辑num1git操作.png">

    <img src="images/github张三编辑num1推送后.png">

- 3.模拟经理后编辑`login.py`文件代码

  - 进入经理本地仓库：`cd Desktop/manager/info/`

  - 经理同步服务器代码：`git pull`

  - 编辑代码：`num2 = 20`

  - 本地仓库记录版本：`git commit -m '第二个变量'`

  - 推送到远程仓库：`git push`

    <img src="images/github经理同步num1.png">

    <img src="images/github经理编辑num2.png">

    <img src="images/github经理编辑num2git操作.png">

    <img src="images/github经理编辑num2推送后.png">

- 4.模拟张三同步服务器代码

  - 本次可以把`num2`同步到张三的本地仓库

    <img src="images/github张三同步num2.png">

- 5.按照以上`2-3-4`步骤循环操作，即可实现基本的协同开发

- 6.总结：

  - 要使用git命令操作仓库，需要进入到仓库内部
  - 要同步服务器代码就执行：`git pull`
  - 本地仓库记录版本就执行：`git commit -am '版本描述'`
  - 推送代码到服务器就执行：`git push`
  - 编辑代码前要先`pull`，编辑完再`commit`，最后推送是`push`



#### 4.5 代码冲突

- **提示**：多人协同开发时，避免不了会出现代码冲突的情况
- **原因**：多人同时修改了同一个文件
- **危害**：会影响正常的开发进度
- **注意**：一旦出现代码冲突，必须先解决再做后续开发

代码冲突演练

- 1.张三先编辑`login.py`文件代码

  - 进入张三本地仓库：`cd Desktop/zhangsan/info`

  - 拉取服务器最新代码：`git pull`

  - 编辑代码：`num3 = 30`

  - 本地仓库记录版本：`git commit -am '第三个变量'`

  - 推送到服务器仓库：`git push`

  - 张三本地仓库和远程仓库代码如下：

    <img src="images/github查看张三本地仓库num3.png">

    ![img](/images/github查看远程仓库num3.png)

- 2.经理后编辑`login.py`文件代码

  - 进入经理本地仓库：`cd Desktop/manager/info/`

  - 编辑代码：`num3 = 300`

  - 本地仓库记录版本：`git commit -am '第三个变量'`

  - 推送到服务器仓库：`git push`

  - **以上操作会出现代码冲突**

    - 提示需要先pull

      <img src="images/github冲突提示需要先pull.png">

    - 提示冲突文件

      <img src="images/github冲突提示冲突文件.png">

    - 冲突代码表现

      <img src="images/github冲突代码表现.png">

- 3.解决冲突

  - 原则：谁冲突谁解决，并且一定要协商解决

  - 方案：保留所有代码 或者 保留某一人代码

  - 解决完冲突代码后，依然需要`add`、`commit`、`push`

    <img src="images/github冲突解决方案.png">

    <img src="images/github冲突解决推送.png">

  - 提示：如果张三执行`pull`没有影响，就算真正解决了冲突代码

补充：

- **容易冲突的操作方式**
  - 多个人同时操作了同一个文件
  - 一个人一直写不提交
  - 修改之前不更新最新代码
  - 提交之前不更新最新代码
  - 擅自修改同事代码
- **减少冲突的操作方式**
  - 养成良好的操作习惯,先`pull`在修改,修改完立即`commit`和`push`
  - 一定要确保自己正在修改的文件是最新版本的
  - 各自开发各自的模块
  - 如果要修改公共文件,一定要先确认有没有人正在修改
  - 下班前一定要提交代码,上班第一件事拉取最新代码
  - 一定不要擅自修改同事的代码



#### 4.6 标签

- 当某一个大版本完成之后,需要打一个标签

- 作用：

  - 记录大版本

  - 备份大版本代码

    <img src="images/github标签图解.png">

模拟经理打标签

- 1.进入到经理的本地仓库info

  ```
   cd Desktop/manager/info/
  ```

- 2.经理在本地打标签

  ```
   git tag -a 标签名 -m '标签描述'
   例：
   git tag -a v1.0 -m 'version 1.0'
  ```

  <img src="images/github经理在本地打标签.png">

- 3.经理推送标签到远程仓库

  ```
   git push origin 标签名
   例：
   git push origin v1.0
  ```

  <img src="images/github经理推送标签.png">

- 4.查看打标签结果

  <img src="images/github查看打标签结果.png">

- 补充：删除本地和远程标签

  ```
    # 删除本地标签
    git tag -d 标签名
    # 删除远程仓库标签
    git push origin --delete tag 标签名
  ```

#### 4.7 分支

<img src="images/github分支.png">

- 作用：
  - 区分生产环境代码以及开发环境代码
  - 研究新的功能或者攻关难题
  - 解决线上bug
- 特点：
  - 项目开发中公用分支包括master、dev
  - 分支master是默认分支，用于发布，当需要发布时将dev分支合并到master分支
  - 分支dev是用于开发的分支，开发完阶段性的代码后，需要合并到master分支

模拟经理分支操作

- 对比：操作分支前的代码

  <img src="images/github经理操作分支前代码.png">

- 1.进入到经理的本地仓库info

  ```
   cd Desktop/manager/info/
  ```

- 2.查看当前分支

  ```
    git branch
  ```

  - 没有创建其他分支时，只有`master`分支

    <img src="images/github经理第一次查看master分支.png">

- 3.经理创建并切换到dev分支

  ```
   git checkout -b dev
  ```

  <img src="images/github经理创建并切换到dev分支.png">

- 4.设置本地分支跟踪远程指定分支（将分支推送到远程）

  ```
    git push -u origin dev
  ```

- 5.经理在dev分支编辑代码

  <img src="images/github经理dev编辑代码num4.png">

- 6.管理dev分支源代码：`add`、`commit`、`push`

  <img src="images/github经理dev编辑代码num4后git操作.png">

  <img src="images/github经理dev编辑代码num4后推送.png">

- 7.dev分支合并到master分支

  - 提示：只有当dev分支合并到master分支成功，张三才能获取到`num4`

  - 7.1 先切换到master分支

    ```
      git checkout master
    ```

    <img src="images/github经理合并分支切换到master分支.png">

  - 7.2 dev分支合并到master分支

    ```
      git merge dev
    ```

    <img src="images/github经理合并分支dev到master.png">

  - 7.3 经理推送合并分支操作到远程仓库

    - 合并分支默认在本地完成，合并后直接推送即可

      ```
      git push
      ```

      <img src="images/github经理合并分支dev到master推送.png">

- 8.张三同步经理合并后的`num4`

  - 只有当张三同步代码成功，分支合并才算成功

    ```
      cd Desktop/zhangsan/info/
      git pull
    ```

    <img src="images/github张三同步分支合并后git操作.png">

    <img src="images/github张三同步分支合并后代码.png">

## **五、本单元知识总结**

```python
1.git基本常用命令
2.git创建分支及解决冲突

```

