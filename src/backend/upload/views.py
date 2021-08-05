from rest_framework import views, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import logging
import traceback

logger = logging.getLogger("django")

class UploadAPIViews(views.APIView):

    renderer_classes = [JSONRenderer]
    upload_dir = '/upload'

    def post(self, request):
        try:
            file = request.FILES['file']
            path = os.path.join(upload_dir, file.name)
            f = open(path, 'wb')
            for chunk in file.chunks():
                f.write(chunk)
            f.close()
        except:
            logger.error(traceback.format_exc())
