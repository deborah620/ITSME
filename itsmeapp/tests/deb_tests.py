from django.test import TestCase
from django.urls import reverse
from itsmeapp.views import Survey
from itsmeapp.views import SurveyResultsAPI
import json

"""
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


# testing the survey model
class TestSubmit(TestCase):

    def test(self):
        form = Survey.objects.create(gender="male", ethnicity='ethnicity', grade=False,
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
