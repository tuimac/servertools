from django.urls import re_path

from . import runcommand

websocket_urlpatterns = [
    re_path(r'runcommand', runcommand.RuncommandConsumer.as_asgi()),
]
