from django.urls import path

from . import views
from .views import BasicAPI

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', BasicAPI.as_view())
]