from rest_framework import views, status
from rest_framework.response import Response
from .container import Container
import logging
import traceback

logger = logging.getLogger("django")

class ContainerAPIViews(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            container = Container()
            response = container.query()
            return Response(response)
        except:
            logger.error(traceback.format_exc())
