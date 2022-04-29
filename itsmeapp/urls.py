from django.urls import path

from . import views
from .views import SurveyResultsAPI
from .views import download_file

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', SurveyResultsAPI.as_view()),
    path('download/', download_file)
]