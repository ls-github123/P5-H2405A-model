~~~
需求：用户名5-10位数字加字母
有效：5-10 数字加字母
无效： 小于5位，大于10位

1001 短视频平台   用户模块   abcd123     200
1002 短视频平台   用户模块   1234abcd    200
1003 短视频平台   用户模块   2a3as34d3   200
1004 短视频平台   用户模块   1234        10010

   
作业：
1.用django写一个注册接口  用户名：5-8位数字加字母  密码：7-10任意字符
requests测试

判定表法

投币50  投币100
充值50  充值100


投币50
投币100
充值50
充值100

投币50
充值50

投币50
充值100

投币100
充值50

投币100
充值100

第一列  a或b   第二列 必须为数字
a  数字
a  非数字

b  数字
b  非数字


不是a或b  数字
不是a或b  非数字







~~~





### 10.1.1 需求分析★★★★★

| 需求编号 | 模块         | 功能     | 需求分析                                                     |
| -------- | ------------ | -------- | ------------------------------------------------------------ |
| 1        | 注册模块     | 注册     | 账号长度必须为6-15位,必须包含大写字母、小写字母、数字。<br>密码长度必须为8-20位,必须包含字母、数字。<br>两次输入密码必须一致。<br>禁止复制粘贴。<br>下拉框必须要有默认选中项。 |
| 2        | 登录模块     | 登录     | 正确的账号密码(测试),登录成功。<br>手机号登录。<br>三方登录。 |
| 3        | 上传资质模块 | 上传资质 | 用户必须为登录状态(token的校验)。<br>上传资质(图片)最大为2x1024KB。 |
| 4        | 上传物料模块 | 上传物料 | 用户必须为登录状态(token的校验)。<br>单次上传资质(图片、视频、音频等)最大为8x1024KB。 |




## 10.1.5 用例编写★★★★★

### 等价类划分

#### 注册

有效等价类：
&emsp;&emsp;账号长度必须在6-15位范围内,必须包含大写字母、小写字母、数字。
&emsp;&emsp;密码长度必须在8-20位范围内,必须包含字母、数字、特殊字符。
&emsp;&emsp;两次输入密码必须一致。
无效等价类：
&emsp;&emsp;账号长度在6-15位范围外,其中包含特殊字符。
&emsp;&emsp;密码长度在8-20位范围外,其中包含特殊字符。
&emsp;&emsp;两次输入密码不一致。


#### 登录(账密)

有效等价类：
&emsp;&emsp;账号长度必须在6-15位范围内,必须包含大写字母、小写字母、数字。
&emsp;&emsp;密码长度必须在8-20位范围内,必须包含字母、数字、特殊字符。
无效等价类：
&emsp;&emsp;账号长度在6-15位范围外,其中包含特殊字符。
&emsp;&emsp;密码长度在6-15位范围外,其中包含特殊字符。



## 10.2 自动化测试

#### 10.2.0 Unittest介绍

### 1.2 什么是UnitTest框架？

```
概念：UnitTest框架是专门用来进行执行代码测试的框架；
```

### 1.3 为什么使用UnitTest框架？

```
1. 能够组织多个用例去执行
2. 提供丰富的断言方法
3. 提供丰富的日志与测试结果

提示：
    1). 断言知识点-在4.2章节会进行学习和讲解；
```

------

### 提示

```
在学习UnitTest框架之前，我们先了解下UnitTest框架内几个核心要素
```

## 2. UnitTest核心要素

```
1. TestCase
2. TestSuite
3. TextTestRunner
4. Fixture
```

### 2.1 TestCase

```
说明：(翻译：测试用例)一个TestCase就是一条测试用例；
使用：
    1. 导包：import unittest             --> 导入unitest框架
    2. 继承：unittest.TestCase             --> 新建测试类继承unittest.TestCase

提示：
    1). 测试用例：在自动化测试中，一条用例就是一个完整的测试流程；                
    2). 测试方法名称命名必须以test开头；
       (原因：unittest.TestCase类批量运行的方法是搜索执行test开头的方法)
```

### 2.2 TestSuite

```
说明：(翻译：测试套件)多条测试用例集合在一起，就是一个TestSuite；
使用：
    1. 实例化：     suite=unittest.TestSuite()                    
                 (suite：为TestSuite实例化的名称)
    2. 添加用例：suite.addTest("ClassName(MethodName)")    
                 (ClassName：为类名；MethodName：为方法名)

    3. 添加扩展：suite.addTest(unittest.makeSuite(ClassName))
                 (搜索指定ClassName内test开头的方法并添加到测试套件中)

提示：
    1). 一条测试用例(.py)内，多个方法也可以使用测试套件
    2). TestSuite需要配合TextTestRunner才能被执行
```

### 2.3 TextTestRunner

```
说明：(翻译：测试执行)是用来执行测试用例套件
使用：
    1. 实例化： runner=unittest.TextTestRunner()
                (runner：TextTestRunner实例化名称)
    2. 执行：    runner.run(suite)
                (suite：为测试套件名称)
```

### 2.4 Fixture

```
说明：是一个概述，对一个测试用例环境的搭建和销毁就是一个Fixture；
使用：
    1. 初始化(搭建)：def setUp(self)        --> 首先执行
       (setUp:此方法继承于unittest.TestCase)        
    2. 结束(销毁):    def tearDown(self)        --> 最后执行
       (tearDown:此方法继承于unittest.TestCase)
提示：
    1. 必须继承unittest.TestCase类，setUp、tearDown才是一个Fixture；
    2. setUp：一般做初始化工作，比如：实例化浏览器、浏览器最大化、隐式等待设置
    3. tearDown：一般做结束工作，比如：退出登录、关闭浏览器
    4. 如果一个测试类有多个test开头方法，则每个方法执行之前都会运行setUp、结束时运行tearDown
```

------

## 3. 案例-3

```
需求：使用UnitTest框架对iweb_shop项目测试
    1. 登陆进行测试
```

### 3.1 操作步骤分析：

```
1. 导包 import unittest
2. 新建测试类并继承unittest.TestCast
3. 新建一个Fixture(setUp、tearDown)
4. 新建登录方法
5. if __name__ == '__main__':
6. unittest.main()执行
```



## 10.2.1 Unittest使用★★★★★

###代码示例

```
# 调用测试类
class TestCount(unittest.TestCase):

    # 初始化方法
    def setUp(self):

        print("开始测试")

    # 编写测试用例
    def test_add(self):

        # 实例化对象
        self.Count = Count(6,3)

        # 断言
        self.assertEqual(self.Count.add(),9)
    
    # 析构方法
    def tearDown(self):

        print("结束测试")
    

 if __name__=="__main__":

     # 构造测试集
     suite = unittest.TestSuite()
     suite.addTest(TestCount("test_add"))


     # 进行测试
     runner = unittest.TextTestRunner()
     runner.run(suite)
```

## 10.2.2 单元测试★★★★★

```
import unittest

from HTMLTestRunner import HTMLTestRunner

import requests

class TestRegisterLogin(unittest.TestCase):

    def setUp(self):
        pass

    # 编写注册测试用例(账号、密码合法)
    def register(self):

        res = requests.post("http://localhost:8000/userinfo/",data={"username":"Admin1","password":"zhang123","type":1})

        res=res.json()["meg"]

        # 断言
        self.assertEqual(res,"注册成功")

    # 编写注册测试用例(账号不合法)
    def register_username(self):

        res = requests.post("http://localhost:8000/userinfo/",data={"username":"admin1","password":"zhang123","type":1})

        res=res.json()["meg"]

        # 断言
        self.assertEqual(res,"账号不合法")

    # 编写注册测试用例(密码不合法)
    def register_password(self):

        res = requests.post("http://localhost:8000/userinfo/",data={"username":"Admin1","password":"11","type":1})

        res=res.json()["meg"]

        # 断言
        self.assertEqual(res,"密码不合法")

    # 编写登录测试用例(账号、密码合法)
    def login(self):

        res = requests.get("http://localhost:8000/userinfo/",params={"username":"Admin1","password":"zhang123","type":1})
        
        res=res.json()["meg"]
        
        # 断言
        self.assertEqual(res,"登录成功")

    # 编写登录测试用例(账号不合法/错误)
    def login_username(self):

        res = requests.get("http://localhost:8000/userinfo/",params={"username":"admim1","password":"z123456","type":1})
        
        res=res.json()["meg"]
        
        # 断言
        self.assertEqual(res,"登录失败,用户名或密码错误")

    # 编写登录测试用例(密码不合法/错误)
    def login_password(self):

        res = requests.get("http://localhost:8000/userinfo/",params={"username":"admim1","password":"z123456","type":1})
        
        res=res.json()["meg"]
        
        # 断言
        self.assertEqual(res,"登录失败,用户名或密码错误")

    def tearDown(self) -> None:
        pass

if __name__ =='__main__':
   
    # 构造测试集
    suite = unittest.TestSuite()

    suite.addTests([TestRegisterLogin('register'),

                    TestRegisterLogin('register_username'),

                    TestRegisterLogin('register_password'),

                    TestRegisterLogin('login'),

                    TestRegisterLogin('login_username'),

                    TestRegisterLogin('login_password')

                    ])

    
    #使用testrunner生成测试报告
    runner = HTMLTestRunner(log=True,output="report",title="test report",report_name="report",open_in_browser=True
    ,description="测试")
    
    runner.run(suite)
```

## 10.2.3 异步方式★★★★★

请求url:/userinfo/
请求方式:POST
公共参数:

| 参数名称 | 参数类型 | 是否必填 |
| -------- | -------- | -------- |
| 无       | 无       | 无       |

参数:

| 参数名称 | 参数类型 | 是否必填 |
| -------- | -------- | -------- |
| username | String   | 是       |
| password | String   | 是       |
| type     | Int      | 是       |

返回值:

```
{
    "code":200,
    "meg":"注册成功"
}
```

## 文字描述

 同步的自动化测试在高并发、多任务的情况下可能会消耗一部分时间,而使用异步的方式自动化测试能更好的提高效率。

 ## 接口代码实例

 ```
import unittest

from unittest.async_case import IsolatedAsyncioTestCase

from HTMLTestRunner import HTMLTestRunner

import requests

 # 声明异步方法
async def get():

    res = requests.post("http://localhost:8000/userinfo/",data={"username":"Admin12","password":"zhang123","type":1})

    res=res.json()0

    return res["meg"]




异步测试用例
class Test(IsolatedAsyncioTestCase):

    async def setUp(self):

        pass

    async def test_len(self):

        res = await get()

        self.assertEqual(res,"注册成功")

    async def tearDown(self) -> None:
        
        pass
    
if __name__=='__main__':

    # 构造测试集
    suite = unittest.TestSuite()

    suite.addTest(Test("register"))

    #使用testrunner生成测试报告
    runner = HTMLTestRunner(log=True,output="report",title="test report",report_name="report",open_in_browser=True
    ,description="注册接口测试")

    runner.run(suite)
    
    
    
    
 ```

 ## 10.2.4 测试报告★★★★★

 ![](/Users/hanxiaobai/Downloads/python/实训一/讲义新/day11/广告竞价平台课件/images/report.png)

