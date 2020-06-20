from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .traceroute import Traceroute
import logging
import traceback

logger = logging.getLogger("django")

class TracerouteAPIViews(views.APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        try:
            traceroute = Traceroute(request.META.get("REMOTE_ADDR"))
            response = traceroute.traceroute()
            response["Url"] = "traceroute"
            return Response(response)
        except:
            logger.error(traceback.format_exc())
