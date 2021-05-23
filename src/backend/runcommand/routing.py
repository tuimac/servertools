from django.urls import re_path

from . import runcommand

websocket_urlpatterns = [
    re_path(r'runcommand', consumers.RuncommandConsumer.as_asgi()),
]
