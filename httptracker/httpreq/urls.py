from django.urls import path
from . import views

urlpatterns = [
    path('', views.HttpreqAPIViews.as_view())
]
