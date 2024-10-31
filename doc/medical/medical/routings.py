from django.urls import re_path

from tusers import consumers

websocket_urlpatterns = [
    # 示例 url ： xxxxx/room/x1/
    re_path(r"room/(?P<group>\w+)/$", consumers.ChatConsumer.as_asgi())
]

