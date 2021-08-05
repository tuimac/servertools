from django.urls import path
from . import views

urlpatterns = [
    path('', views.UploadAPIViews.as_view())
]
