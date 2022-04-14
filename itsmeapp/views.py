from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import Survey


# Create your views here.
def index(request):
    return render(request, 'itsmeapp/index.html', context={})


class SurveyResultsAPI(APIView):
    # get api for survey results
    def get(self, request):
        survey_data = list(Survey.objects.values())
        return Response(survey_data)

    # post api for survey results
    # request object has info about request, ie POST, data, etc
    def post(self, request):
        req_data = request.data

        survey_data = Survey(
            gender=req_data.get('gender'),
            ethnicity=req_data.get('ethnicity'),
            grade=req_data.get('grade'),
            major=req_data.get('major'),
            discussion=req_data.get('discussion'),
            gpa=req_data.get('gpa'),
            program=req_data.get('program'),
            professional=req_data.get('professional'),
            enrollment=req_data.get('enrollment'),
            prior=req_data.get('prior'),
            internship=req_data.get('internship'),
            research=req_data.get('research'),
            parent_engineer=req_data.get('parent-engineer'),
            family_engineer=req_data.get('family-engineer')
        )
        survey_data.save()
        return Response(req_data, status=status.HTTP_200_OK)
