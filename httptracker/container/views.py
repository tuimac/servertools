from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from .container import Container
import logging
import traceback
import collections

logger = logging.getLogger("django")

class ContainerAPIViews(views.APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        try:
            container = Container()
            response = container.query()
            return Response(response)
        except:
            logger.error(traceback.format_exc())
