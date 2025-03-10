import json

# 读取以.jsonl结尾的文件
json_data = []
with open('D:/model_data/DISC-Law-SFT/DISC-Law-SFT-Triplet-released.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)
        json_data.append(data)
    # 待填入的模板
    template = []

    # 遍历json数据集
    for idx, data in enumerate(json_data[:]):
        conversation = [
            {
                'from': 'user',
                'value': data['input']
            },
            {
                'from': 'assistant',
                'value': data['output']
            }
        ]
    
        template.append({
            'id': f'identity_{idx}',
            'conversations': conversation
        })
        print(len(template))
        # 输出填充数据后的模板
        # print(json.dumps(template[2], ensure_ascii=False, indent=2))
    # 将template写入到本地文件
    output_file_path = 'D:/model_data/train_data_law.json'
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(template, f, ensure_ascii=False, indent=2)

    print(f'处理好的数据已写入到本地文件: {output_file_path}')