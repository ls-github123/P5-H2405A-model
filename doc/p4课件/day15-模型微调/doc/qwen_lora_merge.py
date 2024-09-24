import os
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer

def save_model_and_tokenizer(path_to_adapter, new_model_directory):
    """
    加载模型，合并模型，然后保存模型。
    加载分词器并保存。
    """
    # 检查路径有效性
    if not os.path.exists(path_to_adapter):
        raise FileNotFoundError(f"路径 {path_to_adapter} 不存在。")
    if not os.path.exists(new_model_directory):
        os.makedirs(new_model_directory, exist_ok=True)

    try:
        # 模型加载与合并
        model = AutoPeftModelForCausalLM.from_pretrained(
            path_to_adapter,
            device_map="auto",
            trust_remote_code=True
        ).eval()

        merged_model = model.merge_and_unload()
        
        # 保存合并后的模型
        merged_model.save_pretrained(
            new_model_directory, 
            max_shard_size="2048MB", 
            safe_serialization=True
        )
        
        # 加载并保存分词器
        tokenizer = AutoTokenizer.from_pretrained(
            path_to_adapter,
            trust_remote_code=True
        )
        
        # 假设我们有一个函数来保存分词器，这里只是示意
        save_tokenizer(tokenizer, new_model_directory)
        
    except Exception as e:
        # 异常处理，记录或抛出异常
        print(f"加载或保存过程中遇到错误：{e}")
        raise

def save_tokenizer(tokenizer, directory):
    """
    保存分词器到指定目录。
    """
    # 假设这里有一个路径拼接逻辑，将分词器文件保存到指定目录
    tokenizer.save_pretrained(directory)


if __name__=="__main__":

    # lora_model_path="/out_models/qwen1_8b_chat_lora/checkpoint-1200"
    # new_model_directory = "/out_models/qwen1_8b_chat_lora/Qwen-1_8B-Chat_law_merge"
    
    lora_model_path="/mnt/workspace/Qwen/output_qwen"
    new_model_directory = "/mnt/workspace/Qwen/Qwen-1_8B-Chat_merge"
    # 使用函数来执行任务
    save_model_and_tokenizer(lora_model_path, new_model_directory)
