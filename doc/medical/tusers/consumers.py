from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


import json

class ChatConsumer(WebsocketConsumer):  # 继承WebsocketConsumer
#    room_name = 'chat_all_data'
   def websocket_connect(self, message):
        print("有人进行连接了。。。。")
        # cls = ChatConsumer
        # self.room_group_name = cls.room_name
        # print(self.scope['url_route']['kwargs'])
        self.group_name = self.scope['url_route']['kwargs']['group']
        # self.channel_layer.group_add(self.group_name,self.channel_name)
       
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
       
      
       # 有客户端向后端发送 WebSocket 连接的请求时，自动触发(握手)
        self.accept()
       

   def websocket_receive(self, message):
       # 浏览器基于 WebSocket 向后端发送数据，自动触发接收消息
       #消息持久化 mysql  redis
        print(message['text'])
        data = json.loads(message['text'])
        message = data['message']
        room = str(data['from'])
    #    self.send(message)
        channel_layer = get_channel_layer()
      
        async_to_sync(channel_layer.group_send)(
            room,#房间组名
            {
                'type':'send_to_chrome', #消费者中处理的函数
                'data':message
            }
        )


       
    

   def websocket_disconnect(self, message):
       # 客户端向服务端断开连接时，自动触发
        print("连接断开！！")
        self.group_name = self.scope['url_route']['kwargs']['group']
        
        
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
        raise StopConsumer()
    #自定义的处理房间组内的数据
   def send_to_chrome(self, event):
        try:
            data = event.get('data')
            #接收房间组广播数据，将数据发送给websocket
            self.send(json.dumps(data,ensure_ascii=False))
        except Exception as e:
            pass


