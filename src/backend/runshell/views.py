from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .runshell import Runshell
import logging
import traceback

logger = logging.getLogger("django")

class RunshellAPIViews(views.APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        try:
            Runshell.run(request)
            return
        except:
            logger.error(traceback.format_exc())
