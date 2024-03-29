from rest_framework import views, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import logging
import traceback
import os

logger = logging.getLogger("django")

class UploadAPIViews(views.APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request):
        try:
            file = request.FILES['file']
            upload_dir = '/upload'
            path = os.path.join(upload_dir, file.name)
            f = open(path, 'wb')
            for chunk in file.chunks():
                f.write(chunk)
            f.close()
            response = dict()
            response['result'] = 'success'
            return Response(response)
        except:
            logger.error(traceback.format_exc())
            response = dict()
            response['result'] = 'failure'
            return Response(response)
