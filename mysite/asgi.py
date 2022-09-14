"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import sys
import django
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
# sys.path.append is need because python doesn't natively allow sibling imports,
# nor does it consider the current dir to be a package while working on it
# this was the easiest solution/most realistic I could find for fixing this really weird python bug
# it will still highlight as red, but there is no issue/error when running file
sys.path.append("..")
from members import routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    }
)

