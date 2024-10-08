# import random
# import time

# import gradio as gr


# def do_user(user_message, history):  # 把用户的问题消息，放到历史记录中
#     history.append((user_message, None))
#     return '', history


# def do_it(history):  # 定义一个回调函数，
#     # print(history[-1][0])
#     responses = [
#         "谢谢您的留言！",
#         "非常有趣！",
#         "我不确定该如何回答。",
#         "请问还有其他问题吗？",
#         "我会尽快回复您的。",
#         "很高兴能与您交流！",
#     ]
#     # 生成一个答案，随机
#     # resp = random.choice(responses)
#     from langchain_community.llms import Tongyi  

#     # 初始化 Tongyi 模型  
#     tongyi = Tongyi() 
#     mes= history[-1][0]
#     resp =tongyi.stream(mes)

#     # 最后一条历史记录中，只有用户的提问消息，没有AI的的回答
#     history[-1][1] = ''
#     # 流式输出
#     for char in resp:
#         history[-1][1] += char  # 把最后一条聊天记录的  AI的回答 追加了一个字符
#         time.sleep(0.1)
#         yield history

# css = """
# #bgc {background-color: #7FFFD4}
# .feedback textarea {font-size: 24px !important}
# """

# # Blocks： 自定义各种组件联合的一个函数
# with gr.Blocks(title='我的AI聊天机器人', css=css) as instance:  # 自定义
#     gr.Label('我的AI聊天机器人', container=False)
#     chatbot = gr.Chatbot(height=350, placeholder='<strong>AI机器人</strong><br> 你可以问任何问题')
#     msg = gr.Textbox(placeholder='输入你的问题！', elem_classes='feedback', elem_id='bgc')
#     clear = gr.ClearButton(value='清除聊天记录', components=[msg, chatbot])  # 清楚的按钮

#     # 光标在文本输入框中，回车。 触发submit
#     # 通过设置queue=False可以禁用队列，以便立即执行。
#     #  在then里面：调用do_it函数，更新聊天历史，用机器人的回复替换之前创建的None消息，并逐字显示回复内容。
#     msg.submit(do_user, [msg, chatbot], [msg, chatbot], queue=False).then(do_it, chatbot, chatbot)

# # 启动服务
# instance.queue()
# instance.launch(server_name='0.0.0.0', server_port=8008)


from langchain.agents import initialize_agent,Tool
from langchain_community.llms import Tongyi
from langchain.agents import AgentType
llm = Tongyi()

#查询关于订单的问题
def search_order(input:str)->str:
    print("*****订单号为:",input)
    # #查询mysql数据库 requests.get(url,params={"weather":input})
    # orders = Orders.objects.filter(order_no=input).first()
    # olist={"1":"生成","2":"已支付","3":"已发货"}
    # status = olist[orders.status]
    # time = orders.update_time
    status = "已发货"
    time = '2010-10-01'
    return "订单状态："+status+"，发货日期:"+time


#查询关于推荐产品
def recommend_product(input:str)->str:
    #查询mysql数据库
    return "裙子"

#模拟问电商faq
def faq(input:str)->str:
    #查询faiss
    return "7天无理由退货"

tools=[
    Tool(name="search order",func=search_order,
    description = "当用户咨询关于订单的问题用这个工具回答，从用户输入中截取信息，只能订单号后面的单号，不返回订单号这几个字"),
    Tool(name="recommend product",func=recommend_product,
    description = "当用户咨询关于推荐产品问题用这个工具回答"),
    Tool(name="faq",func=faq,
    description = "当用户咨询模拟问电商faq用这个工具回答"),
]
agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
res = agent.invoke("查询订单，订单号为1001")
print(res)

res = agent.invoke("帮我推荐一个上衣")
print(res)