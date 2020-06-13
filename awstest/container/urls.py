from django.urls import path
from . import views

urlpatterns = [
    path('container/', views.ContainerAPIViews.as_view())
]
