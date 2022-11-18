"""
ASGI config for channelsdemo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "channelsdemo.settings")
django_asgi_app = get_asgi_application()

import chatsync.routing
import chatasync.routing

websocket_urls = []
websocket_urls.extend(chatsync.routing.websocket_urlpatterns)
websocket_urls.extend(chatasync.routing.websocket_urlpatterns)

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urls))
        ),
    }
)
