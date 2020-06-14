from django.urls import path
from . import views

urlpatterns = [
    path('', views.EC2APIViews.as_view())
]
