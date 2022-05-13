from django.test import TestCase
from django.urls import reverse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from itsmeapp.views import Survey
from itsmeapp.views import SurveyResultsAPI
import json
from selenium import webdriver
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
import os

# so pop-up browser doesn't keep popping up
options = webdriver.FirefoxOptions()
# options = webdriver.ChromeOptions()
options.headless = True

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
"""


class TestHTML(StaticLiveServerTestCase):

    def setUp(self):
        # create webdriver object
        self.driver = webdriver.Firefox(executable_path=r'geckodriver.exe', options=options)
        # self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_title(self):
        # get the website
        self.driver.get(self.live_server_url)

        # get title and see if correct
        self.assertEquals(self.driver.title, 'ITSME SURVEY ASSESSMENT')

    def test_header(self):
        # get the website
        self.driver.get(self.live_server_url)

        # get header and see if correct
        header = self.driver.find_element(By.TAG_NAME, 'h1').text
        self.assertEquals(header, 'My Engineer State of Mind:\nA Self-Assessing Tool')

    def test_section1(self):
        # get the website
        self.driver.get(self.live_server_url)

        # get header and see if correct
        header = self.driver.find_element(By.TAG_NAME, 'h2').text
        self.assertEquals(header, 'General background information')

        # gender button has correct text
        gen_but = self.driver.find_element(By.ID, 'gender-button').text
        self.assertEquals(gen_but, 'Gender:')

        # able to type in textbox
        self.driver.find_element(By.ID, 'other-gender-textbox').send_keys('genderless')

        # female label is there and can click the female radio and gender button
        female = self.driver.find_element(By.ID, 'female-lab').text
        self.assertEquals(female, 'Female')
        self.driver.find_element(By.ID, 'female').click()
        self.driver.find_element(By.ID, 'gender-button').click()

        # can click on ethnicity button and make sure a label is there
        self.driver.find_element(By.ID, 'ethnicity-prompt').click()
        asian = self.driver.find_element(By.ID, 'asian-lab').text
        self.assertEquals(asian, 'Asian & Pacific American')
        self.driver.find_element(By.ID, 'ethnicity-prompt').click()

        # before college button has correct text
        before_but = self.driver.find_element(By.ID, 'before').text
        self.assertEquals(before_but, 'Where were you immediately before starting at this institution?')

    def test_section_two(self):
        # get the website
        self.driver.get(self.live_server_url)

        # check header
        header = self.driver.find_element(By.ID, 'section-two').text
        self.assertEquals(header, 'Impressions of engineering')

        # check if certain label is there
        certain = self.driver.find_element(By.ID, 'certain').text
        self.assertEquals(certain, 'Certain')

        # check if moderate-reason label is there
        moderate = self.driver.find_element(By.ID, 'Moderate-Reason').text
        self.assertEquals(moderate, 'Moderate Reason')

        # check if disagree label is there
        disagree = self.driver.find_element(By.ID, 'Disagree').text
        self.assertEquals(disagree, 'Disagree')

        # check if a few questions are there
        finish_deg = self.driver.find_element(By.ID, 'how-certain-you-would-complete-engineering-degree-at-this'
                                                     '-institution-prompt').text
        self.assertEquals(finish_deg, 'At the present time, how certain are you that you will complete an engineering '
                                      'degree at this institution?')

        eng_contribute = self.driver.find_element(By.ID,
                                                  'Engineers-have-contributed-to-fixing-world-problems-prompt').text
        self.assertEquals(eng_contribute, 'Engineers have contributed greatly to fixing problems in the world')

        advantage = self.driver.find_element(By.ID, 'The-advantages-of-studying-engineering-outweigh-the'
                                                    '-disadvantages-prompt').text
        self.assertEquals(advantage, 'The advantages of studying engineering outweigh the disadvantages')

    def test_email(self):
        self.driver.get(self.live_server_url)

        # email button correct label
        mail = self.driver.find_element(By.ID, 'mail-link').text
        self.assertEquals(mail, 'Email Results')

    def test_submit(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'male').click()
        self.driver.find_element(By.ID, 'submit-but').submit()

