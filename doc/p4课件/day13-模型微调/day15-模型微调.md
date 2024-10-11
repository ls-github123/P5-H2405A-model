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

### 1.基于qwen-1.8B模型微调

\# 下载qwen和模型

git clone https://github.com/QwenLM/Qwen.git

cd Qwen

git clone https://www.modelscope.cn/qwen/Qwen-1_8B-Chat.git



\# 安装依赖

pip install -r requirements.txt

pip install -r requirements_web_demo.txt

python web_demo.py  -c=Qwen-1_8B-Chat





\# 安装torch

\# 安装torch

```
pip install torch torchvision torchaudio
```

方法1

下载地址：http://download.pytorch.org/whl/torch_stable.html

wget http://download.pytorch.org/whl/cu121/torch/torch-2.1.1+cu121-cp310-cp310-linux_x86_64.whl

pip install torch-2.1.1+cu121-cp310-cp310-linux_x86_64.whl

\# 安装deepspeed

pip install "peft<0.8.0" deepspeed



**## 微调**

准备模型：Qwen-1_8B-Chat

准备训练数据:trans_data.json

\```

cd Qwen

\# 移动finetune_lora_single_gpu.sh到外面

cp finetune/finetune_lora_single_gpu.sh ./

chmod +x finetune_lora_single_gpu.sh

\# 修改微调配置

vim finetune_lora_single_gpu.sh



\# 微调，根据需要修改

Model  /mnt/workspace/Qwen/Qwen-1_8B-Chat 

data  /mnt/workspace/Qwen/data/trans_data.json

修改完执行

bash finetune_lora_single_gpu.sh



报错解决

pip install --upgrade transformers

pip install tf-keras

pip install --upgrade transformers accelerate



\# 合并模型，模型合并文件 qwen_lora_merge.py，上传到Qwen文件夹里，然后修改微调模型路径

lora_model_path="/mnt/workspace/Qwen/output_qwen/checkpoint-5"

\# 合并模型

python qwen_lora_merge.py 

\```

**测试**

 交互式Demo

\```

cd Qwen

python cli_demo.py -c Qwen-1_8B-Chat

\```

```

```

\# 启动服务

python web_demo.py --cpu-only -c=Qwen-1_8B-Chat

\# 查看web界面

http://127.0.0.1:8000/



## 1 Gradio的介绍

Gradio是一个用于构建交互式界面的Python库。它可以帮助您快速创建自定义的Web界面，用于展示和测试机器学习模型、自然语言处理模型、计算机视觉模型等。

Gradio使得构建交互式界面变得非常简单，无需编写繁琐的HTML、CSS和JavaScript代码。您可以使用Gradio来创建一个具有输入字段（如文本输入或图像上传）和输出字段（如模型预测结果）的界面，用户可以直接与您的模型进行交互。

Gradio支持多种输入和输出类型，包括文本、图像、音频和视频。您可以通过定义回调函数来处理输入，并将输出返回给用户。Gradio还提供了自动化的界面布局和样式，使得界面设计变得简单而直观。

https://www.gradio.app/docs

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/482/1723190503035/89dbae9a63054e868b314c10f0734d18.png)

## 2 安装

`pip install gradio`

## 3 重要的函数

### Interface()

```python
import gradio as gr

def image_classifier(inp):
    return {'cat': 0.3, 'dog': 0.7}

demo = gr.Interface(fn=image_classifier, inputs="image", outputs="label")
demo.launch()
```

* fn(Union[Callable, List[Callable]])：包装的函数，可以是一个或者多个，用列表存放多个函数。
* inputs(Union[str, InputComponent, List[Union[str, InputComponent]]])：输入类型/格式，一个参数可以是字符串str；可以是输入组件InputComponent；多个参数可以是列表，列表可以包含字符串str，输入组件InputComponent。输入组件的个数应该和fn函数的参数个数一致。
* outputs(Union[str, OutputComponent, List[Union[str, - OutputComponent]]])：输出类型/格式，与inputs类似，区别就算这是输出组件。输出组件的个数应该和fn函数返回个数一致。
* live(bool)：默认为False，设置为True，为动态页面，只要输入发生变化，结果马上发生改变。
* layout(str)：输入输出面板的布局。"horizontal"安排他们为两列等高；"unaligned"安排他们为两列不等高；"vertical"安排他们为垂直排放。
* allow_flagging(str)：有三个选项"never"、“auto”、“manual”。设置为"never"或"auto"时，用户无法看到Flag按钮；设置为"manual"，用户可见Flag按钮。如果设置为"auto"，每次的输入输出都会被标记保存。如果设置为"manual"，当用户按下Flag按钮，标记当前输入输出的结果并保存。
* flagging_dir(str)：Flag保存的文件夹名称

### launch函数

```python
import gradio as gr
def reverse(text):
    return text[::-1]
demo = gr.Interface(reverse, "text", "text")
demo.launch(share=True, auth=("username", "password"))
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/482/1723190503035/cabfc9eb138b41b38fab1365c856a304.png)

## 4  案例

### 4.1 计算器应用

```python
"""
这段代码使用Gradio库创建了一个简单的计算器应用。应用中定义了一个名为calculator的函数，它接受三个参数：num1（第一个数字）、operation（操作符）和num2（第二个数字）。根据操作符的不同，函数会执行相应的计算操作，包括加法、减法、乘法和除法。如果除法操作中的第二个数字为零，会抛出一个gr.Error异常。
"""
import gradio as gr
#from foo import BAR
#
def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise gr.Error("Cannot divide by zero!")
        return num1 / num2

demo = gr.Interface(
    calculator,
    [
        "number", 
        gr.Radio(["add", "subtract", "multiply", "divide"]),
        "number"
    ],
    "number",
    examples=[
        [45, "add", 3],
        [3.14, "divide", 2],
        [144, "multiply", 2.5],
        [0, "subtract", 1.2],
    ],
    title="Toy Calculator",
    description="Here's a sample toy calculator. Allows you to calculate things like $2+2=4$",
)

demo.launch()
```

### 4.2 进度条案例

```python
import time

import gradio as gr


def do_it(input_word: str, progress=gr.Progress()):   # 定义一个回调函数，并初始化一个进度条
    res = ''
    progress(0, desc='开始...')

    # 进度条滚动，
    for letter in progress.tqdm(input_word, desc='运行中...'):
        time.sleep(0.25)
        res = res + letter
    return res


instance = gr.Interface(  # 构建一个UI界面
    fn=do_it,
    inputs=[
       gr.Text(label='请输入任何文本')
    ],
    outputs=gr.Text(label='输出的结果：')
)

# 启动服务
instance.launch(server_name='0.0.0.0', server_port=8008)


```

### 4.3 流式输出案例

```python
import random
import time

import gradio as gr


def do_it(message, history):   # 定义一个回调函数，
    responses = [
        "谢谢您的留言！",
        "非常有趣！",
        "我不确定该如何回答。",
        "请问还有其他问题吗？",
        "我会尽快回复您的。",
        "很高兴能与您交流！",
    ]
    # 生成一个答案，随机
    resp = random.choice(responses)
    # 流式输出
    res = ''
    for char in resp:
        res += char
        time.sleep(0.1)
        yield res


instance = gr.ChatInterface(  # 构建一个UI界面
    fn=do_it,
    # inputs=[
    #    gr.Text(label='请输入一个提问')
    # ],
    # outputs=gr.Text(label='输出的结果：'),
    title='模拟流式输出！'
)

# 启动服务
instance.launch(server_name='0.0.0.0', server_port=8008)

```

### 4.4 AI大模型客户端案例

```python
import random
import time

import gradio as gr


def do_user(user_message, history):  # 把用户的问题消息，放到历史记录中
    history.append((user_message, None))
    return '', history


def do_it(history):  # 定义一个回调函数，
    print(history)
    responses = [
        "谢谢您的留言！",
        "非常有趣！",
        "我不确定该如何回答。",
        "请问还有其他问题吗？",
        "我会尽快回复您的。",
        "很高兴能与您交流！",
    ]
    # 生成一个答案，随机
    resp = random.choice(responses)

    # 最后一条历史记录中，只有用户的提问消息，没有AI的的回答
    history[-1][1] = ''
    # 流式输出
    for char in resp:
        history[-1][1] += char  # 把最后一条聊天记录的  AI的回答 追加了一个字符
        time.sleep(0.1)
        yield history

css = """
#bgc {background-color: #7FFFD4}
.feedback textarea {font-size: 24px !important}
"""

# Blocks： 自定义各种组件联合的一个函数
with gr.Blocks(title='我的AI聊天机器人', css=css) as instance:  # 自定义
    gr.Label('我的AI聊天机器人', container=False)
    chatbot = gr.Chatbot(height=350, placeholder='<strong>AI机器人</strong><br> 你可以问任何问题')
    msg = gr.Textbox(placeholder='输入你的问题！', elem_classes='feedback', elem_id='bgc')
    clear = gr.ClearButton(value='清除聊天记录', components=[msg, chatbot])  # 清楚的按钮

    # 光标在文本输入框中，回车。 触发submit
    # 通过设置queue=False可以禁用队列，以便立即执行。
    #  在then里面：调用do_it函数，更新聊天历史，用机器人的回复替换之前创建的None消息，并逐字显示回复内容。
    msg.submit(do_user, [msg, chatbot], [msg, chatbot], queue=False).then(do_it, chatbot, chatbot)

# 启动服务
instance.queue()
instance.launch(server_name='0.0.0.0', server_port=8008)

```

案例

~~~
import random
import time

import gradio as gr


def do_user(user_message, history):  # 把用户的问题消息，放到历史记录中
    history.append((user_message, None))
    return '', history


def do_it(history):  # 定义一个回调函数，
    # print(history[-1][0])
    responses = [
        "谢谢您的留言！",
        "非常有趣！",
        "我不确定该如何回答。",
        "请问还有其他问题吗？",
        "我会尽快回复您的。",
        "很高兴能与您交流！",
    ]
    # 生成一个答案，随机
    # resp = random.choice(responses)
    from langchain_community.llms import Tongyi  

    # 初始化 Tongyi 模型  
    tongyi = Tongyi() 
    mes= history[-1][0]
    resp =tongyi.stream(mes)

    # 最后一条历史记录中，只有用户的提问消息，没有AI的的回答
    history[-1][1] = ''
    # 流式输出
    for char in resp:
        history[-1][1] += char  # 把最后一条聊天记录的  AI的回答 追加了一个字符
        time.sleep(0.1)
        yield history

css = """
#bgc {background-color: #7FFFD4}
.feedback textarea {font-size: 24px !important}
"""

# Blocks： 自定义各种组件联合的一个函数
with gr.Blocks(title='我的AI聊天机器人', css=css) as instance:  # 自定义
    gr.Label('我的AI聊天机器人', container=False)
    chatbot = gr.Chatbot(height=350, placeholder='<strong>AI机器人</strong><br> 你可以问任何问题')
    msg = gr.Textbox(placeholder='输入你的问题！', elem_classes='feedback', elem_id='bgc')
    clear = gr.ClearButton(value='清除聊天记录', components=[msg, chatbot])  # 清楚的按钮

    # 光标在文本输入框中，回车。 触发submit
    # 通过设置queue=False可以禁用队列，以便立即执行。
    #  在then里面：调用do_it函数，更新聊天历史，用机器人的回复替换之前创建的None消息，并逐字显示回复内容。
    msg.submit(do_user, [msg, chatbot], [msg, chatbot], queue=False).then(do_it, chatbot, chatbot)

# 启动服务
instance.queue()
instance.launch(server_name='0.0.0.0', server_port=8008)


~~~

