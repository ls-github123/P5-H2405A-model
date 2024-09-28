# 第七单元  RAG项目

## **一、昨日知识点回顾**

```python
1.RGA增强检索的几种方式
2.流式调用案例实现
3.文档分割的方式
4.向量化处理
5.向量数据库的使用
```

------

## **二、考核目标**

```
1.项目需求分析
2.项目流程实现
3.文件上传
4.向量数据库使用
```

------

## **三、本单元知识详讲**

### 7.1 RAG综合项目

#### 7.1.1需求分析

~~~
1.数据采集处理
	（1）爬虫爬取数据
	 (2)数据库mysql(在线问诊、医生回答 500多万条)
	 (3)从百度买800多万条数据（开放api接口，appid,serectkey,获取token，requests.post从api中获取）
	 (4)公司内部pdf,excel,word
	 
2.文档加载、切隔、向量化处理、创建索引，写入向量数据库
3.输入问题-》通过索引加载向量数据库-》检索（召回k=3）
4.构建prompt调用模型处理
~~~

1.数据采集处理
	（1）爬虫爬取数据
	 (2)数据库mysql(在线问诊、医生回答 500多万条)
	 (3)从百度买800多万条数据（开放api接口，appid,serectkey,获取token，requests.post从api中获取）
	 (4)公司内部pdf,excel,word

​			文件本地上传：写一个vue页面，获取文件，点击提交

​             写一个接口：获取文件流，写到static/upload/1目录下		               

爬虫爬取数据

~~~
requests.get(url,data,verfy=false)
requests.post
ip限制(ip代理池)、user_agent、证书加密（verfy=false）
list1=[,,,,,]

~~~

ip代理池

~~~python
import requests
import random

# 代理池
proxies = [
    'http://123.123.123.123:8080',
    'http://456.456.456.456:8080',
    'http://789.789.789.789:8080'
]

def get_random_proxy():
    """从代理池中随机选择一个代理"""
    return random.choice(proxies)

def fetch_url(url):
    """使用随机代理发送请求"""
    # 获取随机代理
    proxy = get_random_proxy()
    # 设置代理
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    try:
        # 发送请求
        response = requests.get(url, proxies=proxies, timeout=5)
        # 检查响应状态码
        if response.status_code == 200:
            return response.text
        else:
            print(f"请求失败，状态码：{response.status_code}")
    except Exception as e:
        print(f"请求时发生错误：{e}")

# 示例 URL
url = 'http://example.com'

# 发送请求
response_text = fetch_url(url)
if response_text:
    print(response_text)
~~~

代码实现

~~~python
class Test(APIView):
    def get(self,request):
        
        from bs4 import BeautifulSoup
        res = requests.get('https://movie.douban.com/',headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        movies = []

        for review in soup.find_all('div', class_='review'):
            movie_link_tag = review.find('div', class_='review-hd').find('a')
            movie_title_tag = review.find('div', class_='review-meta').find_all('a')[-1]
            
            movie_url = movie_link_tag['href']
            movie_name = movie_title_tag.text.strip().replace('《', '').replace('》', '')
            
            movies.append({'电影名称': movie_name, 'url': movie_url})
            
        # 指定文件名
        file_name = './static/upload/movie.json'

        # 使用 with 语句确保文件正确关闭
        with open(os.path.join(file_name), 'w', encoding='utf-8') as file:
            # 使用 json.dump 将 Python 对象转换为 JSON 格式并写入文件
            json.dump(movies, file, ensure_ascii=False, indent=4)

        print(f"数据已成功写入 {file_name} 文件")
        
        # data = getdoc(file_name)
        # print(data)
        # 导入所需的模块和类
        from langchain.embeddings import CacheBackedEmbeddings
        from langchain.storage import LocalFileStore
        from langchain_community.document_loaders import TextLoader
        from langchain_community.vectorstores import FAISS
        from langchain.embeddings.dashscope import DashScopeEmbeddings

        from langchain_text_splitters import CharacterTextSplitter
        
        # 实例化向量嵌入器
        embeddings = DashScopeEmbeddings()
        
        # 初始化缓存存储器
        store = LocalFileStore("./cache/")
        
        # 创建缓存支持的嵌入器
        cached_embedder = CacheBackedEmbeddings.from_bytes_store( embeddings, store, namespace=embeddings.model)
        
        # 加载文档并将其拆分成片段
        doc = TextLoader(file_name,encoding='utf-8').load()
        spliter = CharacterTextSplitter("\n",chunk_size=200, chunk_overlap=0)
        chunks = spliter.split_documents(doc)
        # 创建向量存储
        # db = FAISS.from_documents(chunks, cached_embedder)
        faissdb.add(chunks,'movielist')
        return Response({"code":200})
    
    def post(self,request):
        ask = "电影"
        res = faissdb.search(ask,'movielist',4)
       
        prompt = "请帮我从以下{res}中返回三部电影的名称和请求地址,返回格式转成json格式返回,返回格式转成json格式返回,只返回json数据，不要任务描述信息"
        promptTemplate = PromptTemplate.from_template(prompt)
        # 生成prompt
        prompt = promptTemplate.format(res=res)
        tongyi = Tongyi()
        ret = tongyi.invoke(prompt)
        data = json.loads(ret)
        print(data)
        return Response({"code":200,'data':data})
~~~

django文件本地上传

vue

~~~
 <el-upload
    class="avatar-uploader"
    :before-upload="upload"
  >
   <el-icon  class="avatar-uploader-icon">上传</el-icon>
  </el-upload>
  
const upload=(file)=>{
  const fd = new FormData()
  fd.append("file",file)
  http.post('test/',fd).then(res=>{

  })
}
~~~

django

~~~
file = request.FILES.get('file')
print(file)
filename = file.name

with open(f'./static/upload/{filename}', 'wb') as f:
for chunk in file.chunks():
f.write(chunk)
~~~

读取某个文件夹下所有文件

~~~python
# 指定文件夹路径
        folder_path = './static/upload/'
        from langchain.document_loaders import DirectoryLoader
        # 使用 DirectoryLoader 加载文件夹中的所有文件
        loader = DirectoryLoader(folder_path, glob='**/*.txt')  # 根据需要调整文件类型
        documents = loader.load()

        # 检查加载的文档数量
        print(f'Loaded {len(documents)} documents from {folder_path}')

        # 将文档分割成小块（可选）
        text_splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=0)
        chunks = text_splitter.split_documents(documents)
       
        # 创建向量存储
        # db = FAISS.from_documents(chunks, cached_embedder)
        faissdb.add(chunks,'mtlist')
        res = faissdb.search("电脑",'mtlist',4)

        # 检查分割后的文本数量
        print(res)
~~~



~~~
1.从百度文库下载pdf、word文档，教育  requests.get  豆瓣
2.以数据进行处理，用正则或者xpath提取电影名称和地址，存入Json文件
3.加载文档，分隔，向量化处理，写入FAISS数据库
4.写一个vue页面，输入电影标题，点击搜索
5.查询向量数据库，获取信息，调用大模型处理返回结果
~~~

![](/Users/hanxiaobai/Library/Application Support/typora-user-images/image-20240613155956292.png)

以下是构建这样一个 RAG 项目的步骤：

1. **环境准备**:
   - 安装 LangChain 和其他依赖库，如 ChromaDB 或 FAISS 作为向量数据库，以及相应的文档加载器和转换器。
2. **数据准备**:
   - 收集和整理你的知识库。这可以是文档、网页或其他文本数据。
   - 将这些数据转换成适合 LangChain 处理的格式。
3. **创建向量数据库**:
   - 使用 LangChain 的文档加载器加载数据。
   - 将文档分割成块，并将这些块嵌入到向量数据库中。这将允许你的模型检索相关文档片段。
4. **设置 LangChain 链**:
   - 创建一个 LangChain 链，包括一个 LLM（例如通义千问）和一个向量数据库检索器。
   - 配置检索器以确定从数据库中检索多少个文档。
5. **提问和回答**:
   - 向模型提出问题。
   - 模型将从向量数据库中检索相关文档，并利用这些信息生成答案。
6. **评估和优化**:
   - 评估生成的答案是否准确和有用。
   - 如果必要，调整检索器的参数，或者增加更多的训练数据。

步骤概览

1. 设置Django后端
   - 创建一个Django项目和应用。
   - 安装必要的库（如`faiss-cpu`，`django-rest-framework`等）。
   - 定义模型（如果需要）。
   - 创建API视图来处理文件上传和向量查询。
2. 设置Vue前端
   - 创建一个Vue项目。
   - 编写上传文件的组件。
   - 编写查询组件，用于输入查询内容并发送请求。
   - 展示查询结果。
3. 前后端通信
   - 使用Django REST framework创建RESTful API。
   - Vue使用axios或fetch API与Django后端通信。

### 7.2页面构建

#### 7.2.1 流程分析

1.新建vue项目，引入element ui 

2.新建一个vue页面

3.写一个文件上传按钮

4.点击提交上传文件

#### 7.2.2 项目代码

~~~js
<template>
  <el-form label-width="80px">
    <el-form-item label="上传文件">
  <el-upload
    class="avatar-uploader"
    action="http://localhost:8000/fileUpload/"
    :show-file-list="false"
    :on-success="handleAvatarSuccess"
    :before-upload="beforeAvatarUpload"
  >
    图片<img v-if="imageUrl" :src="imageUrl" class="avatar" />
    <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
  </el-upload>
</el-form-item>
   <el-form-item label="输入框">
      <el-input v-model="inputText"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="handleSubmit">提交</el-button>
    </el-form-item>
</el-form>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'

import type { UploadProps } from 'element-plus'

const imageUrl = ref('')
const inputText = ref('')

const handleAvatarSuccess: UploadProps['onSuccess'] = (
  response,
  uploadFile
) => {
  imageUrl.value = URL.createObjectURL(uploadFile.raw!)
}

const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
  if (rawFile.type !== 'image/jpeg') {
    ElMessage.error('Avatar picture must be JPG format!')
    return false
  } else if (rawFile.size / 1024 / 1024 > 2) {
    ElMessage.error('Avatar picture size can not exceed 2MB!')
    return false
  }
  return true
}

const handleSubmit = ()=>{
  alert('dd')
}
</script>

<style scoped>
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>

<style>
.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}
</style>

~~~

### 7.3文件上传

#### 7.3.1 文件上传配制

1.在项目根目录下创建media文件夹

2.在settings文件中配制

import os

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 指向你的媒体文件存储目录  

MEDIA_URL = '/media/'  # 用于URL配置的媒体文件访问前缀

3.文件上传代码

~~~python
import os
from llmproject import settings
class FileUpload(APIView):
    def post(self,request):
        file = request.FILES['file']
         
        # 生成文件路径  
        file_path = os.path.join(settings.MEDIA_ROOT, file.name)  
        with open(file_path, 'wb+') as destination:  
            for chunk in file.chunks():  
                destination.write(chunk) 
                
        return Response({"code":200})   
~~~

#### 7.3.2 保存文件存入向量数据库

~~~python
db = None

def add_faiss(filepath):
    global db
    # 实例化向量嵌入器
    embeddings = DashScopeEmbeddings()
    # 初始化缓存存储器
    store = LocalFileStore("./cache/")
    # 创建缓存支持的嵌入器
    cached_embedder = CacheBackedEmbeddings.from_bytes_store( embeddings, store, namespace=embeddings.model)
    
    # 加载文档并将其拆分成片段
    doc = TextLoader(filepath,encoding='utf-8').load()
    spliter = CharacterTextSplitter("\n",chunk_size=200, chunk_overlap=0)
    chunks = spliter.split_documents(doc)
    # 创建向量存储
    db = FAISS.from_documents(chunks, cached_embedder)
~~~

### 7.4查询

#### 7.4.1查询流程实现

1.写一个vue页面，加一个输入框

2.写一个接口，获取信息，查询向量数据库

3.解析结果调用大模型

4.封装结果返回数据

#### 7.4.2 查询结果实现

~~~python
from langchain.prompts import PromptTemplate
from langchain_community.llms import Tongyi  

class Ttest(APIView):
    def get(self,request):
        #add_faiss('/Users/hanxiaobai/Downloads/dxb/llmproject/media/NBA新闻.txt')
       
        query_text = request.GET.get('title')
        if query_text: 
            res = db.similarity_search(query_text)
            #调用通义千问查询
            pp = "在返回的{res}中信息很多,请帮我提取治疗方案"
            # 实例化模板类
            promptTemplate = PromptTemplate.from_template(pp)
            # 生成prompt
            prompt = promptTemplate.format(res=res)
            tongyi = Tongyi()
            ret = tongyi.invoke(prompt)
            return Response({"code":200,'list':ret})

~~~

综合案例

~~~
做一个基于医疗行业的知识问题，用户在页面输入描述，返回可能是什么病，注意事项及用药标准
1.requests爬取医生论谈、百度文库下载pdf文档，心脏病、高血压、风湿病
2.加载文档，信息存入向量数据库
3.用文档信息构造事例选择器  messages =[{"心脏病":"心慌 心跳快"}]
4.写一个页面查询
5.写一个接口，获取用户输入-》根据事例选择器定位病种-》查询向量数据库-》调用大模型处理返回结果


1.requests爬取医生论谈、百度文库下载pdf文档，心脏病、高血压、风湿病
2.加载文档，信息存入向量数据库，建立索引index1
3.写prompt用文档内容让模型自动生成10个问题，把问题存入向量数据库，建立索引index2
4.写一个vue页面，用户搜索
5.根据问题去index2中查询k=3个标准问题，查询index1答案
6.调用模型处理返回


~~~



## **四、本单元知识总结**

```python
1.项目需求分析
2.项目流程实现
3.文件上传
4.向量数据库使用

```

