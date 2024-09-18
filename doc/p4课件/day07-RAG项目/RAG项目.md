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

## **四、本单元知识总结**

```python
1.项目需求分析
2.项目流程实现
3.文件上传
4.向量数据库使用

```

