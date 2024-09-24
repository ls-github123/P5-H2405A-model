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

### 1.基于qwen-7B模型微调

\# 安装torch

pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117

\# 安装deepspeed

pip install "peft<0.8.0" deepspeed



**## 微调**

准备模型：Qwen-7B-Chat

准备训练数据:trans_data.json

\```

cd Qwen



\# 移动finetune_lora_single_gpu.sh到外面

cp finetune/finetune_lora_single_gpu.sh ./

chmod +x finetune_lora_single_gpu.sh

\# 修改微调配置

vim finetune_lora_single_gpu.sh



\# 微调，根据需要修改

./finetune_lora_single_gpu.sh -m /mnt/workspace/Qwen/Qwen-7B-Chat -d /mnt/workspace/data/trans_data.json



\# 合并模型，模型合并文件 qwen_lora_merge.py，上传到Qwen文件夹里，然后修改微调模型路径

lora_model_path="/mnt/workspace/Qwen/output_qwen/checkpoint-30"



\# 合并模型

python qwen_lora_merge.py 

\```

