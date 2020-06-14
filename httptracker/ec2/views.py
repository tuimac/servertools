from rest_framework import views, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .ec2 import EC2
import logging
import traceback
import collections

logger = logging.getLogger("django")

class EC2APIViews(views.APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        try:
            ec2 = EC2()
            response = ec2.query()
            logging.info(type(response))
            return Response(response)
        except:
            logger.error(traceback.format_exc())
