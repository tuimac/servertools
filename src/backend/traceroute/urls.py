from django.urls import path
from . import views

urlpatterns = [
    path('', views.TracerouteAPIViews.as_view())
]
