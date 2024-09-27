# 第十二单元  rag项目

## **一、昨日知识点回顾**

```python
1. 昨日知识点1
2. 昨日知识点2

```

------

## **二、考核目标**

```
1.当日考核目标1
2.当日考核目标2
```

------

## **三、本单元知识详讲**

### 1. 系统架构概述

一个基于 LangChain RAG 的医疗问答机器人主要包括以下几个部分：

- **数据层**：存储医学文献、临床指南、研究论文等结构化和非结构化数据。
- **检索层**：使用检索技术（如向量搜索、关键词匹配等）来查找最相关的文档片段。
- **生成层**：基于检索到的信息生成自然语言的回答。
- **用户接口层**：与用户交互的前端界面，可以是文本聊天窗口、语音交互等。

### 2. 关键技术点

- **知识库构建**：收集权威的医学信息，并对其进行清洗、标注和结构化处理。
- **检索技术**：选择合适的检索引擎（如 Elasticsearch、Milvus 等），确保能够高效地检索到最相关的信息。
- **生成模型**：训练或微调一个生成模型（如 LLMs），使其能够基于检索到的信息生成高质量的回答。
- **安全性与隐私保护**：确保系统符合相关的医疗数据保护标准（如 GDPR、HIPAA 等），并采取措施保护用户隐私。
- **个性化推荐**：根据用户的历史查询记录和其他相关信息，提供个性化的医疗建议和服务。

### 3. 实现步骤

#### 数据准备与知识库构建

1. **数据采集**：从公开的医学数据库、期刊、临床试验结果等渠道收集数据。
2. **数据预处理**：清洗数据，去除噪声和重复内容；进行文本标准化处理。
3. **知识图谱构建**：将数据转换为结构化形式，便于检索和分析。
4. **向量化**：使用嵌入模型（如 BERT、Sentence Transformer 等）将文本转换为向量表示，便于相似度计算。

#### 检索与生成模型训练

1. **检索引擎配置**：选择或搭建适合的检索引擎，配置索引。
2. **模型选择与训练**：选择合适的生成模型，使用医学领域的语料进行预训练或微调。
3. **融合策略开发**：开发算法将检索结果与生成模型结合起来，产生最终的回答。

#### 系统集成与部署

1. **API 开发**：开发 RESTful API 或 GraphQL 接口，供前端应用调用。
2. **前端应用开发**：设计和开发用户界面，实现与机器人的互动。
3. **安全性配置**：设置身份验证、访问控制等安全措施。
4. **部署与监控**：将系统部署到生产环境，并设置监控和日志记录系统。

#### 测试与优化

1. **单元测试**：对每个组件进行单独测试，确保其功能正常。
2. **集成测试**：测试整个系统的协同工作情况。
3. **用户反馈循环**：上线初期收集用户反馈，根据反馈持续改进系统。
4. **性能优化**：针对系统瓶颈进行优化，提高响应速度和处理能力。



### 1.rag

1.新建一个分类  id  name  userid 添加时间

  1.点击+号的时候-》调用接口，用uuid生成id,写入es  id,userid->返回分类id

2.搜索问题（问答）

   1.输入问题-》调用接口，获取问题内容、分类id、userid-》根据分类id查询分类名、如果为空把内容（大模型提取关键词）更新到分类名称

   2.问答表

   字段： Id、userid、分类id、问题、回答、添加时间

  获取问题内容、分类id、userid-》根据问题查询faiss向量数据库-》获取答案k=3-》写一个prompt让大模型整理-》返回

3.历史记录（搜索）

查询分类表-》传递参数userid、搜索名称-》根据userid查询分类表，获取10条-》

点击分类-》传递分类id->通过分类id获取信息20条按时间升序

### 代码实现

1.加载数据，存入向量数据库

~~~
pdf、word
mysql   问诊记录、诊断记录表、医疗文章
{"问题":问诊记表中的描述，“答案”：诊断记录表}  存入向量数据库
~~~

2.定义加载文档的类

~~~python
class FileLoad():
    def __init__(self) -> None:
        pass
    
    #使用loader来加载markdown文本
    def markdown_load(self,url):
       
        from langchain_community.document_loaders import TextLoader
        loader = TextLoader(url)
        print(loader.load())
        return loader.load()
    
    #使用loader来加载cvs文件
    def csv_load(self,url):
        from langchain_community.document_loaders.csv_loader import CSVLoader

        loader = CSVLoader(file_path=url,source_column="Location")
        data = loader.load()
        print(data)
        return data
    
    #使用loader来加载cvs文件
    def pdf_load(self,url):
        print("343434333!!!!")
        #使用loader来加载pdf文件
        from langchain_community.document_loaders import PyPDFLoader
        loader = PyPDFLoader(url)
        pages = loader.load_and_split()
        return pages
    
    def getdata(self,url,filename):
        #对文件名进行解析，判断后缀是什么调用哪个方法处理
        arr = filename.split('.')
        if arr[1] == 'md':
            return self.markdown_load(url)
        elif arr[1] == 'csv':
            return self.csv_load(url)
        elif arr[1] == 'pdf':
            return self.pdf_load(url)
        #返回结果
fileload = FileLoad()
# data = fileload.getdata('/Users/hanxiaobai/Downloads/dxb/h2403apro/medical/static/upload/成人高血压食养指南 2023.pdf','成人高血压食养指南 2023.pdf')
# print(data)
~~~

3.向量数据库封装

~~~python
# 导入所需的模块和类
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings.dashscope import DashScopeEmbeddings

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings.dashscope import DashScopeEmbeddings


class DB:
    def __init__(self):
        # 实例化向量嵌入器
        self.embeddings = DashScopeEmbeddings()
        
        # 初始化缓存存储器
        self.store = LocalFileStore("./cache/")
        
        # 创建缓存支持的嵌入器
        self.cached_embedder = CacheBackedEmbeddings.from_bytes_store( self.embeddings, self.store, namespace=self.embeddings.model)
        
        print(self.cached_embedder)
       
    def add(self,chunks,key):
            # 创建向量存储
            db = FAISS.from_documents(chunks, self.cached_embedder)
            db.save_local(key)
    def search(self,ask,key,count):
        db = FAISS.load_local(key,self.cached_embedder,allow_dangerous_deserialization=True)
        res = db.similarity_search(ask, k=count)
        return res
    
db = DB()
~~~

### 4.定义一个视图

~~~python
 def get(self,request):
        doc = fileload.getdata('/Users/hanxiaobai/Downloads/dxb/h2403apro/medical/static/upload/成人高血压食养指南 2023.pdf','成人高血压食养指南 2023.pdf')
        # print(data)
        spliter = CharacterTextSplitter("\n",chunk_size=300, chunk_overlap=20)
        chunks = spliter.split_documents(doc)
        db.add(chunks,'doctorss.faiss')
        #查询mysql数据库，获取信息，存入向量数据库
~~~

业务端

### vue页面

~~~python
<template>
  <div class="common-layout">
    <el-container>
      <!-- 左侧边栏 -->
      <el-aside width="200px" class="sidebar">
        <el-button @click="newConversation">新建会话</el-button>
        <el-input v-model="input" placeholder="搜索会话" style="margin-top: 16px; width: 100%;" />
        <ul class="conversation-list" style="margin-top: 16px;">
          <li v-for="(item, index) in conversations" :key="index">{{ item }}33333</li>
        </ul>
      </el-aside>
      <!-- 主要内容区域 -->
      <el-main class="main-content">
        <ul class="message-list">
          <li v-for="(msg, index) in messages" :key="index">
            {{ msg['qustion'] }} </br>
            {{ msg['answer'] }}
          </li>
        </ul>
        <el-form>
          <el-input
            v-model="textarea"
            type="textarea"
            :autosize="{ minRows: 2, maxRows: 4}"
            placeholder="请输入消息"
            style="margin-bottom: 8px;"
          ></el-input>
          <el-button type="primary" @click="submitMessage">发送</el-button>
        </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import http from '../../http'

// 示例数据
const conversations = ['会话1', '会话2'];
const messages = ref([]);

const textarea = ref('');
const input = ref('');
const cateid=ref('')
const catename=ref('')

const newConversation=()=>{
  // 新建会话逻辑
  http.post('cateManager/',{"userid":1}).then(res=>{
        if(res.data.code == 200){
            alert("添加成功")
            cateid.value = res.data.cateid
        }
    })
}

const submitMessage=()=> {
  // 提交消息逻辑
  http.post('newsManager/',{"userid":1,'cateid':cateid.value,'message':textarea.value}).then(res=>{
        if(res.data.code == 200){
            alert("添加成功")
            // var message = {"qustion":textarea.value,'answer':res.data.mes}
            messages.value.push({"qustion":textarea.value,'answer':res.data.mes})
            if(res.data.cname){
                catename.value= res.data.cname
            }
        }
    })
}
</script>

<style scoped>
.common-layout {
  height: 100%;
  background-color: #ebeef2;
}

.sidebar {
  background-color: #efe7e7;
  padding: 16px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.main-content {
  padding: 16px;
  background-color: #dcd7d7;
  height: calc(100vh - 32px);
  overflow-y: auto;
}

.conversation-list,
.message-list {
  list-style-type: none;
  padding-left: 0;
}

.conversation-list li,
.message-list li {
  padding: 8px;
  border-bottom: 1px solid red;
  color:rgb(20, 7, 7);
}

.conversation-list li:last-child,
.message-list li:last-child {
  border-bottom: none;
}
</style>
~~~

django代码

~~~python
from tools.fileload import fileload
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.llms import Tongyi
from tools.db import db
class TestOrder(APIView):
    def get(self,request):
        doc = fileload.getdata('/Users/hanxiaobai/Downloads/dxb/h2403apro/medical/static/upload/成人高血压食养指南 2023.pdf','成人高血压食养指南 2023.pdf')
        # print(data)
        spliter = CharacterTextSplitter("\n",chunk_size=300, chunk_overlap=20)
        chunks = spliter.split_documents(doc)
        db.add(chunks,'doctorss.faiss')
        #查询mysql数据库，获取信息，存入向量数据库
        
        
        # ask = "蔬菜类等量交换表"
        # res = db.search(ask,'doctorss.faiss',3)
        
        # pp = "在返回的{res}中信息很多,请帮我返回符合问题{ask}的答案,如果返回的是表格请帮我转成json格式"
        # # 实例化模板类
        # promptTemplate = PromptTemplate.from_template(pp)
        # # 生成prompt
        # prompt = promptTemplate.format(res=res,ask=ask)
        # tongyi = Tongyi()
        # ret = tongyi.invoke(prompt)
        # print(ret)
        return Response({"code":200})
    
import datetime,uuid
class CateManager(APIView):
    def post(self,request):
        userid = 1
        res = es.index('dock1',body={"userid":userid,'addtime':datetime.datetime.now(),'name':''})
        return Response({"code":200,'cateid':res['_id']})

# 1导入prompt的类
from langchain.prompts import PromptTemplate

class NewsManager(APIView):
    def post(self,request):
        #接收参数message
        userid = request.data['userid']
        cateid = request.data['cateid']
        message = request.data['message']
        #prompt提取核心内容
        pp = "请帮我生成摘要根据{mes}"
        # 实例化模板类
        promptTemplate = PromptTemplate.from_template(pp)
        # 生成prompt
        prompt = promptTemplate.format(mes=message)
        # 实例化通义大模型
        tongyi = Tongyi()
        ret = tongyi.invoke(prompt)
        #查询分类id
        #查询共有多少条记录的条件O01y1ZEB3zxGBe8bRy7J"
        dsl={
            "query":{
                "match":{"_id":cateid}
            }

        }
        res = es.search(index="dock1", body=dsl)
      
        cates = res['hits']['hits'][0]
        cate = cates['_source']
        cname = ''
        if cate['name']=='':
            cname = ret
            #更新分类
            update_body = {
                "doc": {
                    "name": ret
                }
            }
            es.update(index='dock1',id=cateid,body=update_body)
        
        #调用faiss查询
        resask = db.search(message,'doctorss.faiss',3)
        
        pp = "在返回的{res}中信息很多,请帮我返回符合问题{ask}的答案,如果返回的是表格请帮我转成json格式"
        # 实例化模板类
        promptTemplate = PromptTemplate.from_template(pp)
        # 生成prompt
        prompt = promptTemplate.format(res=resask,ask=message)
      
        ret = tongyi.invoke(prompt)
       
        #写prompt调用大模型处理
        #写入es中返回
        return Response({"code":200,'mes':ret,'cname':cname})
~~~





## **四、本单元知识总结**

```python
1.当日知识点总结1
2.当日知识点总结2

```

