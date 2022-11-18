# chatasync/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chatasync/(?P<room_name>\w+)/$", consumers.ChatAsyncConsumer.as_asgi()),
]
