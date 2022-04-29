from django.test import TestCase
from django.urls import reverse
from itsmeapp.views import Survey
# from itsmeapp.views import SurveyResultsAPI
import json
from django.test import TestCase
import os


"""
couldn't get this to work properly
# testing JSON format
class TestJsonFormat(TestCase):
    def setUp(self):
        # Setup run before every test method.
        Survey.gender = "male"
        Survey.gpa = "4.0"

    def test_json(self):
        self.assertTrue(SurveyResultsAPI.json(SurveyResultsAPI.self, {'gender': 'male'}.get('gender')), msg="gender "
                                                                                                            "saved "
                                                                                                            "properly")
        self.assertEqual(
            json.loads(SurveyResultsAPI.json(request='male').response_list.content)['male'],
            []
        )


class JSONViewTestCase(TestCase):
    def test_json_view(self):
        response = self.client.post(
            reverse(
                'response_list',
                args=('test', 123)
            ),
            json.dumps({
                'user': 'me@example.com',
            }),
            'json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        json_string = response.content
        response_data = json.loads(json_string)
"""


# testing the survey model, gender and ethnicity only
class TestSubmit(TestCase):

    def test(self):
        form = Survey.objects.create(gender="male", ethnicity='white', grade=False,
                                     major=False,
                                     discussion=False,
                                     gpa=False,
                                     program=False,
                                     professional=False,
                                     enrollment=False,
                                     prior=False,
                                     internship=False,
                                     research=False,
                                     parent_engineer=False,
                                     family_engineer=False,
                                     previous_school_impact=False,
                                     finish_degree=False,
                                     finish_degree_here=False,
                                     technology_importance=False,
                                     parents_disprove_difft=False,
                                     engineer_fix_world=False,
                                     engineer_paid=False,
                                     parents_want=False,
                                     job_guarantee=False,
                                     faculty_encor=False,
                                     mentor_encor=False,
                                     intro_opportunity=False,
                                     feel_good=False,
                                     like_build=False,
                                     engineer_fun=False,
                                     use_society=False,
                                     engineer_interesting=False,
                                     figure_out_work=False,
                                     mentoring_program=False,
                                     )

        self.assertEqual(form.gender, "male", msg="gender is male")
        self.assertEqual(form.ethnicity, "white", msg="ethnicity is white")


# Create your tests here.
class Tests(TestCase):

    def test_post_survey_results(self):
        data_to_post = {
            "gender": "male",
            "ethnicity": "white",
            "grade": "senior",
            "major": "cmpe",
            "discussion": "1",
            "gpa": "3.5 - 3.75",
            "program": "False",
            "professional": "N/A",
            "enrollment": "full-time",
            "prior": "high school",
            "internship": "True",
            "research": "True",
            "parent-engineer": "True",
            "family-engineer": "True",
            "previous_school_impact": "False",
            "finish-degree": "test",
            "finish-degree-here": "False",
            "technology-importance": "False",
            "parents-disprove-difft": "False",
            "engineer-fix-world": "False",
            "engineer-paid": "False",
            "parents-want": "False",
            "job-guarantee": "False",
            "faculty-encor": "False",
            "mentor-encor": "False",
            "intro-opportunity": "False",
            "feel-good": "False",
            "like-build": "False",
            "engineer-fun": "False",
            "use-society": "False",
            "engineer-interesting": "False",
            "figure-out-work": "False",
            "mentoring-program": "False",
        }
        response = self.client.post('/api/', data_to_post)
        self.assertEqual(response.status_code, 200)

    def test_persist_to_database(self):
        data_to_post = {
            "gender": "male",
            "ethnicity": "white",
            "grade": "senior",
            "major": "cmpe",
            "discussion": "1",
            "gpa": "3.5 - 3.75",
            "program": "False",
            "professional": "N/A",
            "enrollment": "full-time",
            "prior": "high school",
            "internship": "True",
            "research": "True",
            "parent-engineer": "True",
            "family-engineer": "True",
            "previous_school_impact": "False",
            "finish-degree": "test",
            "finish-degree-here": "False",
            "technology-importance": "False",
            "parents-disprove-difft": "False",
            "engineer-fix-world": "False",
            "engineer-paid": "False",
            "parents-want": "False",
            "job-guarantee": "False",
            "faculty-encor": "False",
            "mentor-encor": "False",
            "intro-opportunity": "False",
            "feel-good": "False",
            "like-build": "False",
            "engineer-fun": "False",
            "use-society": "False",
            "engineer-interesting": "False",
            "figure-out-work": "False",
            "mentoring-program": "False",
        }

        self.client.post('/api/', data_to_post)
        database_after_one_post = self.client.get('/api/')
        self.assertEqual(len(database_after_one_post.data), 1)  # assert that there is one survey results row stored in the database
        self.client.post('/api/', data_to_post)
        self.client.post('/api/', data_to_post)
        database_after_three_posts = self.client.get('/api/')
        self.assertEqual(len(database_after_three_posts.data), 3)  # now 3 since we just added 2 more rows

    def test_download_csv(self):
        data_to_post = {
            "gender": "male",
            "ethnicity": "white",
            "grade": "senior",
            "major": "cmpe",
            "discussion": "1",
            "gpa": "3.5 - 3.75",
            "program": "False",
            "professional": "N/A",
            "enrollment": "full-time",
            "prior": "high school",
            "internship": "True",
            "research": "True",
            "parent-engineer": "True",
            "family-engineer": "True",
            "previous_school_impact": "False",
            "finish-degree": "test",
            "finish-degree-here": "False",
            "technology-importance": "False",
            "parents-disprove-difft": "False",
            "engineer-fix-world": "False",
            "engineer-paid": "False",
            "parents-want": "False",
            "job-guarantee": "False",
            "faculty-encor": "False",
            "mentor-encor": "False",
            "intro-opportunity": "False",
            "feel-good": "False",
            "like-build": "False",
            "engineer-fun": "False",
            "use-society": "False",
            "engineer-interesting": "False",
            "figure-out-work": "False",
            "mentoring-program": "False",
        }
        self.client.post('/api/', data_to_post)
        self.client.get('/download/')  # trigger the downloading function that populates results.csv

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_filename = 'results.csv'
        csv_filepath = base_dir + "/" + csv_filename
        path = open(csv_filepath, 'r')
        self.assertTrue("gpa" in path.read())  # assert that the csv has been populated
