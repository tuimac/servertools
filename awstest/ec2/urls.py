from django.urls import path
from . import views

urlpatterns = [
    path('ec2/', views.EC2APIViews.as_view())
]
