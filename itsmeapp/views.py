from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import Survey
<<<<<<< HEAD
from django.http import JsonResponse
=======
import os
import mimetypes
import sqlite3
import csv
>>>>>>> develop


def index(request):
    return render(request, 'itsmeapp/index.html', context={})

def populate_results_csv(db_filepath, csv_filepath):
    connect = sqlite3.connect(db_filepath)
    cursor = connect.cursor()

    cursor.execute("SELECT * from ITSMEAPP_SURVEY")

    # Fetch the data returned.
    results = cursor.fetchall()

    # Extract the table headers.
    headers = [i[0] for i in cursor.description]

    # Open CSV file for writing.
    csv_file = csv.writer(open(csv_filepath, 'w', newline=''),
                         delimiter=',', lineterminator='\r\n',
                         quoting=csv.QUOTE_ALL, escapechar='\\')

    # Add the headers and data to the CSV file.
    csv_file.writerow(headers)
    csv_file.writerows(results)

    connect.close()


def download_file(request):
    # Define Django project base directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    csv_filename = 'results.csv'
    # Define the full file path
    csv_filepath = base_dir + "/" + csv_filename
    db_filepath = base_dir + "/db.sqlite3"
    # Open the file for reading content
    populate_results_csv(db_filepath, csv_filepath)
    path = open(csv_filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(csv_filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % csv_filename
    # Return the response value
    path.close()
    return response


class SurveyResultsAPI(APIView):

    # get api for survey results
    self = None

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
            family_engineer=req_data.get('family-engineer'),
            previous_school_impact=req_data.get('family-engineer'),
            finish_degree=req_data.get('finish-degree'),
            finish_degree_here=req_data.get('finish-degree-here'),
            technology_importance=req_data.get('technology-importance'),
            parents_disprove_difft=req_data.get('parents-disprove-difft'),
            engineer_fix_world=req_data.get('engineer-fix-world'),
            engineer_paid=req_data.get('engineer-paid'),
            parents_want=req_data.get('parents-want'),
            job_guarantee=req_data.get('job-guarantee'),
            faculty_encor=req_data.get('faculty-encor'),
            mentor_encor=req_data.get('mentor-encor'),
            intro_opportunity=req_data.get('intro-opportunity'),
            feel_good=req_data.get('feel-good'),
            like_build=req_data.get('like-build'),
            engineer_fun=req_data.get('engineer-fun'),
            use_society=req_data.get('use-society'),
            engineer_interesting=req_data.get('engineer-interesting'),
            figure_out_work=req_data.get('figure-out-work'),
            mentoring_program=req_data.get('mentoring-program')
        )
        survey_data.save()
        return HttpResponse(req_data, status=status.HTTP_200_OK)

    # json format
    def json(self, request):
        response = Survey.objects.all().values()
        response_list = list(response)
        """
        manual way in case the automatic way doesn't work
        req_data = request.data
        json_survey = {'gender': req_data.get('gender'),
                       'ethnicity': req_data.get('ethnicity'),
                       'grade': req_data.get('grade'),
                       'major': req_data.get('major'),
                       'discussion': req_data.get('discussion'),
                       'gpa': req_data.get('gpa'),
                       'program': req_data.get('program'),
                       'professional': req_data.get('professional'),
                       'enrollment': req_data.get('enrollment'),
                       'prior': req_data.get('prior'),
                       'internship': req_data.get('internship'),
                       'research': req_data.get('research'),
                       'parent_engineer': req_data.get('parent-engineer'),
                       'family_engineer': req_data.get('family-engineer'),
                       'previous_school_impact': req_data.get('family-engineer'),
                       'finish_degree': req_data.get('finish-degree'),
                       'finish_degree_here': req_data.get('finish-degree-here'),
                       'technology_importance': req_data.get('technology-importance'),
                       'parents_disprove_difft': req_data.get('parents-disprove-difft'),
                       'engineer_fix_world': req_data.get('engineer-fix-world'),
                       'engineer_paid': req_data.get('engineer-paid'),
                       'parents_want': req_data.get('parents-want'),
                       'job_guarantee': req_data.get('job-guarantee'),
                       'faculty_encor': req_data.get('faculty-encor'),
                       'mentor_encor': req_data.get('mentor-encor'),
                       'intro_opportunity': req_data.get('intro-opportunity'),
                       'feel_good': req_data.get('feel-good'),
                       'like_build': req_data.get('like-build'),
                       'engineer_fun': req_data.get('engineer-fun'),
                       'use_society': req_data.get('use-society'),
                       'engineer_interesting': req_data.get('engineer-interesting'),
                       'figure_out_work': req_data.get('figure-out-work'),
                       'mentoring_program': req_data.get('mentoring-program')
                       }
        return JsonResponse(json_survey)
        """
        return JsonResponse(response_list)
