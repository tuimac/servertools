from rest_framework import views, status
from rest_framework.response import Response
from ec2 import EC2

class EC2APIViews(views.APIView):
    def get(self, request, *args, **kwargs):
        response = dict()
