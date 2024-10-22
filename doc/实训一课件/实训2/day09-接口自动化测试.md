### 1.接口的构成

请求地址：http://asfs.com/user/reg

请求方式  post

传入参数 {"username":'zs',"password":123}

头部 {"Content-Type":"application/json"}

返回结果

{"code":200,"mes"："成功"}

### 2.接口自动化测试需求

测试人员登录-》添加接口测试-》写入测试表-》点击执行-》根据id读取数据库信息，判断封装调用requets模块进行测试-》将测试结果和预期结果对比，写入测试结果表中

### 3.数据库字典

#### 接口测试表(interface_test)

<table>
  <tr><td>字段名</td><td>字段类型</td><td>中文名</td><td>描述</td></tr>
  <tr><td>title</td><td>varchar(30)</td><td>标题</td><td></td></tr>
  <tr><td>proid</td><td>int</td><td>项目id</td><td></td></tr>
  <tr><td>develop</td><td>varchar</td><td>环境选择</td><td></td></tr>
  <tr><td>moduleid</td><td>int</td><td>模块id</td><td></td></tr>
  <tr><td>userid</td><td>int</td><td>提交人id</td><td></td></tr>
  <tr><td>interface_address</td><td>varchar(50)</td><td>接口地址</td><td></td></tr>
  <tr><td>request_type</td><td>varchar(50)</td><td>请求类型</td><td>get、post、put、delete</td></tr>
  <tr><td>request_params</td><td>text</td><td>请求参数</td><td>序列化</td></tr>
  <tr><td>request_headers</td><td>text</td><td>请求头部</td><td>序列化</td></tr>
  <tr><td>request_result</td><td>text</td><td>预期结果</td><td>序列化</td></tr>
</table>

#### 结果记录表(result_record)

<table>
  <tr><td>字段名</td><td>字段类型</td><td>中文名</td><td>描述</td></tr>
  <tr><td>interfaceid</td><td>int</td><td>测试接口id</td><td></td></tr>
  <tr><td>test_result</td><td>varchar</td><td>测试结果</td><td></td></tr>
  <tr><td>report_result</td><td>varchar</td><td>报告结果说明</td><td></td></tr>
  <tr><td>test_time</td><td>datetime</td><td>测试时间</td><td></td></tr>
</table>



~~~~
record = {"id":1,'title':'注册接口测试','porname':"A项目",'develop':"http://localhost:8000/",'interface_address':'user/reg',request_params:{"username":"abcd","password":"23"},request_result={}}
url = record.develop+record.interface_address
if record.request_type == "get":
   res =request.get(url,params=record.request_params,headers=record.request_result)
   data = json.loads(res.text)
   
   if data['code'] == record.request_result.code:
        
~~~~



