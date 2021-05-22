from rest_framework import views, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .httpreq import Httpreq
import logging
import traceback

logger = logging.getLogger("django")

class HttpreqAPIViews(views.APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        try:
            httpreq = Httpreq(request.headers, request.body.decode('utf-8'))
            response = httpreq.query()
            response["Url"] = "httpreq"
            return Response(response)
        except:
            logger.error(traceback.format_exc())
