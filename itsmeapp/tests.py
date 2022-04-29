from django.test import TestCase
import os


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
            "family-engineer": "True"
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
            "family-engineer": "True"
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
            "family-engineer": "True"
        }
        self.client.post('/api/', data_to_post)
        self.client.get('/download/')  # trigger the downloading function that populates results.csv

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_filename = 'results.csv'
        csv_filepath = base_dir + "/" + csv_filename
        path = open(csv_filepath, 'r')
        self.assertTrue("gpa" in path.read())  # assert that the csv has been populated
