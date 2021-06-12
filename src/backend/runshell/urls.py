from django.urls import path
from . import views

urlpatterns = [
    path('', views.RunshellAPIViews.as_view())
]
