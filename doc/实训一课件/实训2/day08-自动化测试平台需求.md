### 1.需求分析

~~~
用户模块（rbac）（添加人员、角色、资源）、项目模块（添加项目、添加项目人员）（项目和人员是多对多）、Bug管理、接口自动化测试、批量执行
~~~

### 2.模块分析

####   用户模块

~~~
用户管理
角色管理  配制资源
资源管理
~~~

项目模块

~~~
项目管理   -》添加、人员配制（多对多）
模块管理

~~~

Bug管理

~~~
bug管理-》添加bug（选择项目、选择模块、标题、描述、传入参数、返回结果、报错信息、状态、级别）、更新状态
~~~

接口自动化测试

~~~
接口管理-》添加接口测试（选择项目，选择模块，接口名称，url地址，传入参数，返回结果）-》接口测试列表（开始测试、查看报告）
批量执行-》接口列表中选择多个，批量测试
定时执行-》选择接口测试列表、配制执行时间（选择三种模块：1.cron 2.interval 3.date）
~~~

### 项目中用到的表

#### 资源表

<table>
  <tr><td>字段名</td><td>字段类型</td><td>描述</td></tr>
  <tr><td>资源id</td><td>int</td><td>自增</td></tr>
  <tr><td>资源名称</td><td>varchar</td><td>唯一约束</td></tr>
  <tr><td>pid</td><td>int</td><td>菜单时为0，资源时为菜单id</td></tr>
  <tr><td>资源标识</td><td>int</td><td>十进制存二进制值</td></tr>
  <tr><td>资源类型</td><td>int</td><td>1接口 2为页面</td></tr>
</table>

#### 角色表

<table>
  <tr><td>字段名</td><td>字段类型</td><td>描述</td></tr>
  <tr><td>id</td><td>int</td><td>自增</td></tr>
  <tr><td>角色名称</td><td>varchar</td><td>唯一约束</td></tr>
  <tr><td>权限值</td><td>int</td><td>二进制转十进行存储</td></tr>
</table>

#### 用户表

<table>
  <tr><td>字段名</td><td>字段类型</td><td>描述</td></tr>
  <tr><td>id</td><td>int</td><td>自增</td></tr>
  <tr><td>姓名</td><td>varchar</td><td>唯一约束</td></tr>
  <tr><td>手机号</td><td>char(11)</td><td>唯一约束</td></tr>
   <tr><td>角色id</td><td>int</td><td>外键角色表</td></tr>
</table>

#### 项目表

<table>
  <tr><td>字段名</td><td>字段类型</td><td>描述</td></tr>
  <tr><td>id</td><td>int</td><td>自增</td></tr>
  <tr><td>项目名称</td><td>varchar</td><td>唯一约束</td></tr>
  <tr><td>项目负责人id</td><td>int</td><td></td></tr>
  <tr><td>项目测试url</td><td>varchar</td><td></td></tr>
  <tr><td>项目线上url</td><td>varchar</td><td></td></tr>
  <tr><td>公用变量</td><td>text</td><td>序列化存储</td></tr>
  <tr><td>请求头部</td><td>text</td><td>序列化存储</td></tr>
</table>

#### 项目人员表

<table>
<tr><td>字段名</td><td>字段类型</td><td>描述</td></tr>
  <tr><td>id</td><td>int</td><td>自增</td></tr>
  <tr><td>项目id</td><td>int</td><td></td></tr>
  <tr><td>用户id</td><td>int</td><td></td></tr>
  <tr><td>姓名</td><td>int</td><td></td></tr>
  <tr><td>用户角色id</td><td>int</td><td></td></tr>
</table>

#### 模块表

<table>
<tr><td>字段名</td><td>字段类型</td><td>描述</td></tr>
  <tr><td>id</td><td>int</td><td>自增</td></tr>
  <tr><td>项目id</td><td>int</td><td></td></tr>
  <tr><td>模块名称</td><td>varchar(50)</td><td></td></tr>
  </table>

#### bug表

<table>
<tr><td>字段名</td><td>字段类型</td><td>描述</td></tr>
  <tr><td>id</td><td>int</td><td>自增</td></tr>
  <tr><td>项目id</td><td>int</td><td></td></tr>
  <tr><td>模块id</td><td>int</td><td></td></tr>
  <tr><td>标题</td><td>varchar(50)</td><td></td></tr>
  <tr><td>内容描述</td><td>text</td><td>使用富文件编辑器</td></tr>
  <tr><td>状态</td><td>int</td><td>(1 new:新建 2 open:打开 3 fixed:修复缺陷 4 closed:关闭缺陷 5 postpone:推迟缺陷 6 rejected:拒绝缺陷 7.reopen)</td></tr>
  <tr><td>参数</td><td>varchar(255)</td><td></td></tr>
  <tr><td>预期结果</td><td>varchar(255)</td><td></td></tr>
  <tr><td>实际结果</td><td>varchar(255)</td><td></td></tr>
  <tr><td>级别</td><td>int</td><td>（1严重  2一般）</td></tr>
  <tr><td>优先级</td><td>int</td><td>（1紧急  2一般）</td></tr>
  <tr><td>当前操作人</td><td>int</td><td></td></tr>
  <tr><td>操作时间</td><td>datetime</td><td></td></tr>
  <tr><td>下一操作人</td><td>id</td><td></td></tr>
  <tr><td>下一操作角色</td><td>角色id</td><td></td></tr>
  </table>

#### bug操作记录表

<table>
<tr><td>字段名</td><td>字段类型</td><td>描述</td></tr>
  <tr><td>id</td><td>int</td><td>自增</td></tr>
  <tr><td>bugId</td><td>int</td><td></td></tr>
  <tr><td>操作人</td><td>int</td><td></td></tr>
  <tr><td>时间</td><td>datetime</td><td></td></tr>
  <tr><td>描述</td><td>text</td><td></td></tr>
</table>

#### 接口表

<table>
<tr><td>字段名</td><td>字段类型</td><td>描述</td></tr>
  <tr><td>id</td><td>int</td><td>自增</td></tr>
  <tr><td>项目id</td><td>int</td><td></td></tr>
  <tr><td>模块id</td><td>int</td><td></td></tr>
  <tr><td>接口名称</td><td>varchar(100)</td><td></td></tr>
  <tr><td>接口地址</td><td>varchar(255)</td><td></td></tr>
  <tr><td>请求方式</td><td>varchar(10)</td><td>[get、post、put、delete]</td></tr>
  <tr><td>环境选择</td><td>int</td><td></td></tr>
  <tr><td>请求参数</td><td>text</td><td></td></tr>
  <tr><td>预期结果</td><td>text</td><td></td></tr>
</table>

#### 接口测试结果记录表

<table>
<tr><td>字段名</td><td>字段类型</td><td>描述</td></tr>
  <tr><td>id</td><td>int</td><td>自增</td></tr>
  <tr><td>接口id</td><td>int</td><td></td></tr>
  <tr><td>返回结果</td><td>varchar(255)</td><td></td></tr>
  <tr><td>测试结果描述</td><td>varchar(255)</td><td></td></tr>
  <tr><td>测试状态</td><td>int</td><td>1成功  2失败</td></tr>
  <tr><td>时间</td><td>datetime</td><td></td></tr>
</table>

#### 定时任务配制表

<table>
<tr><td>字段名</td><td>字段类型</td><td>描述</td></tr>
  <tr><td>id</td><td>int</td><td>自增</td></tr>
  <tr><td>接口id</td><td>int</td><td></td></tr>
  <tr><td>test_type</td><td>int</td><td>1cron 2interval 3date</td></tr>
  <tr><td>参数</td><td>varchar(255)</td><td></td></tr>
</table>

### 2.用户模块

~~~
添加角色
添加资源
角色配制资源
添加用户-》选择角色

登录-》用机号登录-》登录成功（从数据库中查询此用户对应的接口权限和页面权限），
页面权限返回给客户端，客户端存储在LocalStorage中。mian.js加一个beforeEach白名单过滤，
获取LocalStorage页面权限，判断当前Url是否在，不在返回没权限操作

router.beforeEach((to, from, next) => {
        if (to.path == '/login') {
            next();
        } else {
            var token = localStorage.getItem('token')
            if (token) {
                //获取页面权限列表
                var pagelist = JSON.parse(localStorage.getItem('pagelist'))
                    //判断当前请求的Url是否在这个列表中
                if (pagelist.indexOf(to.path) == -1) {
                    alert("您无权访问")
                    return false;
                }
                next()
            } else {
                alert('请先登录');
                next('/login')
            }

        }
    })
    
    接口权限：
    登录成功获取此用户的接口权限，将权限列表转成字符串存入redis中，自定义中间件中判断token是否有效，是否过期。获取redis中的接口权限列表，转成列表判断
    interfacelist = r.get("interfacelist")
    interfacelist = json.loads(interfacelist)
    if request.url not in interfacelist:
        return "无权操作"

~~~









