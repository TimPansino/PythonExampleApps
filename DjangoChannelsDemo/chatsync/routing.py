# chatsync/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chatsync/(?P<room_name>\w+)/$", consumers.ChatSyncConsumer.as_asgi()),
]
