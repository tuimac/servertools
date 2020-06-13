from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContainerAPIViews.as_view())
]
