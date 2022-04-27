from django.urls import path

from . import views
from .views import SurveyResultsAPI

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', SurveyResultsAPI.as_view(), name='survey_result_api')
]
