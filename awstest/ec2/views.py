from rest_framework import views, status
from rest_framework.response import Response
from .ec2 import EC2
import logging
import traceback

logger = logging.getLogger("django")

class EC2APIViews(views.APIView):
    try:
        def get(self, request, *args, **kwargs):
            response = ec2.query()
            return Response(response)
    except:
        logger.error("".join(traceback.format_list()))
