# pip install openai

# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="https://446859-proxy-8000.dsw-gateway-cn-shanghai.data.aliyun.com/", api_key="none")

completion = client.chat.completions.create(
  model="qwen:7b",
  messages=[
    {"role": "user", "content": "讲一个50字以内的笑话"}
  ],
  temperature=0.7,
  top_p=0.95,
)

print(completion)