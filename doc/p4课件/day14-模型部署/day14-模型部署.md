# 第十四单元  模型部署

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

### 1.HuggingFace介绍

~~~
# 模型社区

## HuggingFace

官网：https://huggingface.co/

HuggingFace 是一个自然语言处理（NLP）领域的开源社区和平台，它提供了一系列强大的工具、库和预训练模型，帮助开发者快速构建和部署自然语言处理应用。HuggingFace 平台的主要组成部分和特点如下：

1. **Transformers 库**：HuggingFace 的 Transformers 库是其最著名和核心的部分。它提供了广泛的预训练模型（如BERT、GPT、RoBERTa等）的实现，并提供易于使用的API，用于进行文本分类、命名实体识别、文本生成等各种 NLP 任务。Transformers 库支持多种主流深度学习框架，如PyTorch和TensorFlow。
2. **模型架构和优化方法**：HuggingFace 提供了各种用于构建和优化 NLP 模型的架构和方法，包括用于序列分类、序列标注、文本生成等任务的模型架构和损失函数，以及用于模型训练和优化的技术，如学习率调度、权重衰减等。
3. **数据集和指标**：HuggingFace 提供了大量的 NLP 数据集，用于训练和评估模型。这些数据集涵盖了各种不同的任务和语言，包括文本分类、命名实体识别、情感分析等。此外，HuggingFace 还提供了常用的评估指标和评估方法，帮助用户对模型性能进行评估和比较。
4. **模型训练和部署工具**：HuggingFace 提供了用于模型训练和部署的工具和库，使用户能够轻松地进行模型训练、微调和部署。例如，通过使用 HuggingFace 的 Trainer 类，用户可以更便捷地配置和执行模型的训练过程。
5. **模型分享和社区**：HuggingFace 平台鼓励用户分享和交流模型、代码和经验。用户可以在 HuggingFace 的模型仓库中发布和共享自己的模型，并从社区中获取模型、代码和应用案例。
~~~

### 2.魔搭社区ModelScope

~~~
## ModelScope

官网：https://www.modelscope.cn

魔搭社区ModelScope是一个由阿里达摩院推出的开源模型服务平台，其主要功能和目的如下：

1. 模型共享与探索： ModelScope汇集了各领域最先进的机器学习模型，包括但不限于自然语言处理、计算机视觉、语音识别等。用户可以在平台上发现和探索这些模型，了解其特性和性能。
2. 一站式服务： 提供从模型探索、推理、训练到部署和应用的一站式服务。用户不仅可以体验预训练模型的性能，还可以根据自己的需求对模型进行定制和训练，并方便地将训练好的模型部署到实际应用中。
3. 易用性和灵活性： ModelScope旨在为泛AI开发者提供灵活、易用、低成本的模型服务产品。用户无需额外部署复杂的环境，就可以在平台上直接使用各种模型，降低了使用和开发AI模型的门槛。
4. 开源与合作： 作为一款开源平台，ModelScope鼓励社区成员参与模型的开发、改进和分享。通过共同合作，推动AI技术的发展和创新。
5. 智能体开发框架： ModelScope还推出了ModelScope-Agent开发框架，如MSAgent-Qwen-7B，允许用户打造属于自己的智能体。这个框架提供了丰富的环境配置选项，支持单卡运行，并有一定的显存要求。
~~~

### 3.服务器领取

1.打开网址

https://modelscope.cn/models/ZhipuAI/glm-4-9b/files

![image-20240913170622975](img/image-20240913170622975.png)

  2.阿里领取服务器

~~~
# 在线GPU环境

## 阿里云PAI

每天发送500份

搜索中输入 PAI-DSW

export GRADIO_ROOT_PATH=/${JUPYTER_NAME}/proxy/7860/
~~~

3.点击开始使用

~~~
命令行下载
请先通过如下命令安装ModelScope

pip install modelscope
下载完整模型repo
modelscope download --model ZhipuAI/glm-4-9b

~~~

安装虚拟环境

### **Anaconda**

conda是为了解决传统的虚拟环境问题而出现的虚拟环境管理工具，conda在virtualenv基础上，提取了公共代码保存到一个公共目录，独立代码分离开来的模式解决了virtualenv的解释器复制问题，同时conda还可以通过自动管理python解释器的功能，允许我们创建虚拟环境目录时自由的选择不同的python解释器版本。conda一共有2个版本：miniconda与anaconda。

其中，anaconda是conda的完整版本，内置了将近300个关于服务端开发，人工智能，数据分析，爬虫，测试，运维等常用第三方模块。而miniconda则是conda的简单版本，内置了将近30个常用第三方模块。所以学习的时候，建议在本地安装anaconda，在公司开发或项目部署时使用miniconda。

anaconda下载地址：https://repo.anaconda.com/archive/

wget https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh

### 安装Anaconda

1. **校验安装文件**（可选）：为了确保下载的文件没有损坏，你可以使用sha256sum来校验文件的完整性。将`Anaconda3-2023.07-1-Linux-x86_64.sh`替换为你实际下载的文件名。

   bash深色版本

   ```
   sha256sum Anaconda3-2024.06-1-Linux-x86_64.sh
   ```

   比对输出的哈希值与Anaconda官网提供的哈希值是否一致。

2. **运行安装程序**：

   - 赋予.sh文件执行权限：

     bash

     ```
     chmod +x Anaconda3-2024.06-1-Linux-x86_64.sh
     ```

   - 运行安装程序：

     

     ```
     ./Anaconda3-2024.06-1-Linux-x86_64.sh
     ```

   - 按照屏幕上的提示进行操作。这包括阅读并接受许可协议，选择安装位置等。

3. **初始化Anaconda**：

   - 在安装过程中，你会被询问是否要初始化Anaconda。如果选择了“yes”，则Anaconda会自动配置你的.bashrc文件，以便每次打开终端时都能使用conda。

   - 如果你错过了这个选项，或者想稍后手动初始化，可以编辑你的.bashrc文件，添加以下行：

     bash深色版本

     ```
     export PATH="/root/anaconda3/anaconda3/bin:$PATH"
     ```

   - 使更改生效：

     bash深色版本

     ```
     source ~/.bashrc
     ```

### 验证安装

cd /root/anaconda3/bin/

1. **检查conda版本**：

   bash深色版本

   ```
   ./conda --version
   ```

   如果安装成功，你应该能看到conda的版本号。

2. **创建一个新的环境**（可选）：

   bash深色版本

   ```
   ./conda create --name myenv
   ```

   这将创建一个名为myenv的新环境。你可以根据需要安装不同的包到这个环境中。

3. **激活环境**：

   bash深色版本

   ```
   ./conda activate myenv
   ```

miniconda下载地址：https://repo.anaconda.com/miniconda/

conda还提供了一个类似pypi的包模块管理库，可以让我们搜索到10年前的包：https://anaconda.org/

| 命令                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| conda -V                                                     | 查看conda版本                                                |
| **conda info**                                               | 查看当前Anaconda的系统配置信息                               |
| **conda env list**                                           | 列出当前系统中所有虚拟环境，环境列表左边`*`号表示当前所在环境，<br>也可以使用`conda info -e`查看，注意：conda安装到本地以后，默认就提供了一个全局版本的虚拟环境，叫`base` |
| **conda create -n <虚拟环境名称> python=<python版本号> <包名1>==<版本号>** | 新建虚拟环境，-n表示设置当前虚拟环境的名称，<br>python表示设置当前虚拟环境的python版本，如果本地没有会自动下载安装<br>表示创建虚拟环境时同时安装一个或多个指定第三方包 |
| conda create -n <新的虚拟环境名称> --clone <旧的虚拟环境名称> | 克隆虚拟环境                                                 |
| **conda activate <虚拟环境名称>**                            | 进入/切换到指定名称的虚拟环境，如果不带任何参数，则默认回到全局虚拟环境`base`中 |
| **conda deactivate**                                         | 退出当前虚拟环境                                             |
| conda install -n <虚拟环境名称> <包名1>==<版本号>            | 在虚拟环境外部，给**指定虚拟环境**安装或更新一个或多个指定包<br>如果是最新的版本的包，conda install无法安装，则可以使用pip install安装 |
| **conda install <包名1>==<版本号>**                          | 在虚拟环境内部，给**当前虚拟环境**安装或更新一个或多个指定包 |
| conda install  <包名1>==<版本号> **-c conda-force**          | 在虚拟环境内部，指定下载服务器源给**当前虚拟环境**安装或更新一个或多个指定包，conda-force有时候会因为网络问题被拦截。 |
| conda remove -n <虚拟环境名称> <包名1>==<版本号>             | 在虚拟环境外部，给**指定虚拟环境**卸载一个或多个指定包       |
| **conda remove <包名1>==<版本号>**                           | 在虚拟环境内部，给**当前虚拟环境**卸载一个或多个指定包       |
| **conda remove -n <虚拟环境名称> --all**                     | 删除指定虚拟环境，并卸载该环境中所有指定包                   |
| **conda env export > environment.yaml**                      | 导出当前虚拟环境的Anaconda包信息到环境配置文件environment.yaml中 |
| **conda env create -f environment.yaml**                     | 根据环境配置文件environment.yaml的包信息来创建新的虚拟环境   |
| conda update --prefix <anaconda安装目录> anaconda            | 更新Anaconda的版本。<br>先回到base环境，再执行conda update，系统会自动提示完整并正确的命令<br>如果上述方法不行，只能卸载现有的conda，然后下载最新版本安装。 |

```bash
# 新建虚拟环境
# -n <虚拟环境名称> 或者 --name <虚拟环境名称>
#     表示设置当前虚拟环境的名称
# python=<python版本号>
#     表示设置当前虚拟环境的python版本，如果本地没有会自动下载安装

# <包名>==<版本号>
#     表示创建虚拟环境时同时安装一个或多个指定第三方包
#     可指定版本号，如果不指定版本，则安装当前python环境能支持的最新版本的包
#     注意:
#         指定包的版本时，有可能会因为没有这个版本或当前python环境不支持当前版本而导致虚拟环境创建失败。
#         所以，建议指定包版本时，尽量使用*号表示小版本，例如：django==1.*

conda create -n <虚拟环境名称> python=<python版本号> <包名1>==<版本号> <包名2> ... <包名n>

# 例如：
conda create -n py27 python=2.7
conda create -n py36 python=3.6  pymongo   # 表示安装pymongo模块的最新版本
conda create -n pro1 python=3.8  flask celery   # 表示安装2个包
conda create -n pro2 python=3.6  django==2.2.0 pymysql    # 表示安装django指定版本，pymysql的最新版本

# 克隆虚拟环境
conda create -n <新的虚拟环境名称> --clone <旧的虚拟环境名称>

# 进入/切换到指定名称的虚拟环境，如果不带任何参数，则默认回到全局环境base中。
conda activate <虚拟环境名称>

# 退出当前虚拟环境
conda deactivate

# 在虚拟环境外部，给指定虚拟环境安装/或者更新一个或多个指定包
conda install -n <虚拟环境名称> <包名1>==<版本号> <包名2> ... <包名n>
# 也可以在进入虚拟环境以后，通过conda install <包名> 来完成安装工作
conda install <包名1>==<版本号> <包名2> ... <包名n>

#  在虚拟环境外部，给指定虚拟环境卸载一个或多个指定包
conda remove -n <虚拟环境名称> <包名1>==<版本号> <包名2> ... <包名n>
# 也可以在进入虚拟环境以后，通过conda remove <包名> 来完成卸载工作
conda remove <包名1>==<版本号> <包名2> ... <包名n>

# 删除指定虚拟环境
conda remove -n <虚拟环境名称> --all

# 导出当前虚拟环境的Anaconda包信息到环境配置文件environment.yaml中
conda env export > environment.yaml 

# 根据环境配置文件environment.yaml的包信息来创建新的虚拟环境
conda env create -f environment.yaml

# 更新Anaconda的版本，这里可以先执行conda update，系统会自动提示完整并正确的命令
conda update --prefix <anaconda安装目录> anaconda
```

> 注意：
>
> 有了Anaconda以后，要养成一个习惯：新建一个项目，就给这个项目单独分配一个虚拟环境。



### 创建并运行虚拟环境

创建虚拟环境并在虚拟环境中下载安装django包

```bash
# 创建djdemo虚拟环境，务必要指定python解析器的版本
conda create -n py310 python=3.10
# 进入虚拟环境
conda activate py310
# 安装django基本模块
pip install django==4.2.5 -i https://pypi.tuna.tsinghua.edu.cn/simple

# 生成一个具有基本目录结构的django项目，在python安装了django包以后，默认就提供了一个全局命令django-admin，可以让我们基于django-admin快速创建django项目
django-admin startproject djdemo   # djdemo 就是项目目录名，建议采用与项目相关的名称，最好英文！！！
```

### 4.千问模型本地部署

#### 1.代码下载

项目地址：https://github.com/QwenLM/Qwen/

下载到本地: git clone https://github.com/QwenLM/Qwen.git

#### 2.环境安装

conda create -n qwen1 python == 3.10.1

conda activate qwen1

cd Qwen

pip install -r requirements.txt

#### 3.模型下载

git clone https://www.modelscope.cn/qwen/Qwen-7B-Chat.git

git clone https://www.modelscope.cn/qwen/Qwen-1_8B-Chat.git

#### 4.本地模型推理

安装 pytorch

安装依赖包

pip install -r requirements_web_demo.txt

vim web_demo.py修改模型的路径

GPU推理

   python web_demo.py --server-name 0.0.0.0 -c  Qwen-7B-Chat

python openai_api.py  -c=Qwen-7B-Chat

启动模型

~~~
- 交互式Demo
```
cd Qwen
python cli_demo.py  -c Qwen-1_8B-Chat
```

- chat界面

```
# 启动服务
python web_demo.py --cpu-only -c=Qwen-1_8B-Chat
# 查看web界面
http://127.0.0.1:8000/
```

- API
```
# 先安装依赖
pip install fastapi sse_starlette uvicorn pydantic
# 启动API服务
python openai_api.py  -c=Qwen-7B-Chat
```
~~~

访问本地模型

~~~python
import openai
openai.api_base = "http://localhost:8000/v1"
openai.api_key = "none"

# 使用流式回复的请求
for chunk in openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=True
    # 流式输出的自定义stopwords功能尚未支持，正在开发中
):
    if hasattr(chunk.choices[0].delta, "content"):
        print(chunk.choices[0].delta.content, end="", flush=True)

# 不使用流式回复的请求
response = openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "帮我写一篇关于春天的作文"}
    ],
    stream=False,
    stop=[] # 在此处添加自定义的stop words 例如ReAct prompting时需要增加： stop=["Observation:"]。
)
print(response.choices[0].message.content)
~~~

使用langchain

~~~
from langchain_community.llms.openai import OpenAI
from langchain_community.chat_models.openai import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


# 创建一个ChatOpenAI集成对象，用于与OpenAI模型交互
# 注意：API只支持流式输出
llm = ChatOpenAI(base_url="http://localhost:8000/v1", api_key="none",streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]  )
 
llm.invoke("讲一个50字以内的笑话")
~~~



### 2.使用ollama3部署本地大模型

Ollama 是一个开源项目，它允许用户在本地机器上运行大型语言模型。这个项目简化了在个人电脑或服务器上部署和运行像LLaMA这样的大型语言模型的过程。如果你想要使用 Ollama 部署本地的大模型

\- 由于学生电脑系统不统一，有的是windows，有的是mac,还有的是Ubautu

\- 这几个系统中，Ubautu遇到的问题比较少，windows可能遇到的问题最多

下载对应系统的版本

\- https://ollama.com/download

Windows

\- 下载完毕后，双击执行安装

\- 安装完成后在cmd中执行以下命令，安装具体某个大模型

\- 如果本地不存在模型，则会先行下载

linux

linux安装

~~~
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3
~~~

llama3支持的大模型

 https://github.com/ollama/ollama

<img src="img/lla_20240801143507.png" style="margin-left: 0px" width="600px">

~~~
ollama list
~~~



NAME                    ID              SIZE    MODIFIED

llama2-chinese:13b      990f930d55c5    7.4 GB  6 weeks ago

gemma:latest            a72c7f4d0a15    5.0 GB  6 weeks ago

qwen2:latest            e0d4e1163c58    4.4 GB  6 weeks ago

llama3:latest           365c0bd3c000    4.7 GB  6 weeks ago

测试服务是否启动

\- http://localhost:11434/api/tags

测试代码

~~~


```
curl http://localhost:11434/api/generate -d '{
    "model": "llama3",
    "prompt":"Why is the sky blue?"
    }'
```
~~~

python代码访问

~~~
import requests  
  
url = 'http://127.0.0.1:11434/v1/chat/completions'    
  
# 发送JSON数据  
json_data = {
    'model': 'llama3:latest',
    'messages': [
        {
            'role': 'system',
            'content': 'You are a helpful assistant.'
        },
        {
            'role': 'user',
            'content': '你是谁？'
        }
    ]
}
  
# 发送POST请求，并指定json参数  
response = requests.post(url, json=json_data)  
  
print(response.status_code)  
print(response.text)  #str
~~~

### 4.GLM-4-9B介绍

~~~
GLM-4-9B 是智谱 AI 推出的最新一代预训练模型 GLM-4 系列中的开源版本。 在语义、数学、推理、代码和知识等多方面的数据集测评中， GLM-4-9B 及其人类偏好对齐的版本 GLM-4-9B-Chat 均表现出超越 Llama-3-8B 的卓越性能。除了能进行多轮对话，GLM-4-9B-Chat 还具备网页浏览、代码执行、自定义工具调用（Function Call）和长文本推理（支持最大 128K 上下文）等高级功能。本代模型增加了多语言支持，支持包括日语，韩语，德语在内的 26 种语言。我们还推出了支持 1M 上下文长度（约 200 万中文字符）的 GLM-4-9B-Chat-1M 模型和基于 GLM-4-9B 的多模态模型 GLM-4V-9B。GLM-4V-9B 具备 1120 * 1120 高分辨率下的中英双语多轮对话能力，在中英文综合能力、感知推理、文字识别、图表理解等多方面多模态评测中，GLM-4V-9B 表现出超越 GPT-4-turbo-2024-04-09、Gemini 1.0 Pro、Qwen-VL-Max 和 Claude 3 Opus 的卓越性能。
GLM-4-9B 的基座版本，支持8K上下文长度
~~~



## **四、本单元知识总结**

```python
1.当日知识点总结1
2.当日知识点总结2

```

