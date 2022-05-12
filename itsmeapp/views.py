from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import Survey
from django.http import JsonResponse
import os
import mimetypes
import sqlite3
import csv


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
    # self = None

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
            engineer_interesting=req_data.get('engineer-inter'),
            figure_out_work=req_data.get('figure-out-work'),
            mentoring_program=req_data.get('mentoring-program'),
            Relate=req_data.get('Relate'),
            lot_common=req_data.get('lot-common'),
            others_share=req_data.get('others-share'),
            relate_extra=req_data.get('relate-extra'),
            succeed=req_data.get('succeed'),
            well_paying=req_data.get('well-paying'),
            expect=req_data.get('expect'),
            lifestyle=req_data.get('lifestyle'),
            part_group=req_data.get('part-group'),
            job=req_data.get('job'),
            like_job=req_data.get('like-job'),
            bad_test=req_data.get('bad-test'),
            friends=req_data.get('friends'),
            cope=req_data.get('cope'),
            only_one=req_data.get('only-one'),
            approach=req_data.get('approach'),
            new_env=req_data.get('new-env'),
            self_confidence=req_data.get('self-confidence'),
            leadership=req_data.get('leadership'),
            public=req_data.get('public'),
            math=req_data.get('math'),
            science=req_data.get('science'),
            communication=req_data.get('communication'),
            apply=req_data.get('apply'),
            business=req_data.get('business'),
            teams=req_data.get('teams'),
            reward=req_data.get('reward'),
            study=req_data.get('study'),
            advantage=req_data.get('advantage'),
            no_care=req_data.get('no-care'),
            benefit=req_data.get('benefit'),
            other=req_data.get('other'),
            no_change=req_data.get('no-change'),
            effort=req_data.get('effort'),
            boring=req_data.get('boring')
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
