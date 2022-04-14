from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import Survey

# Create your views here.
def index(request):
    return render(request, 'itsmeapp/index.html', context={})



class BasicAPI(APIView):
    def get(self, request):
        data = {
            'first_name': 'grant',
            'last_name': 'zhu'
        }
        return Response(data)

    # HERE IS THE POST API
    def post(self, request):
        req_data = request.data

        survey_data = Survey(gender=req_data.get('gender'))
        return Response(req_data, status=status.HTTP_200_OK)
