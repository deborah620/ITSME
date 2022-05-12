# ITSME
CMSC 447 Spring 2022 

This code was developed in python

To run this website, open the terminal of your choosing and type these commands
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Currently, this opens a website browser and displays the beginnings of a survery assessment. It also contains a database and a post endpoint to store users responses and a get endpoint to get all previous responses. 

to run the test suite one must have firefox downloaded (can use this link to do so: https://www.mozilla.org/en-US/firefox/new/), the firefox web driver is included in this repository. 
to run the tests type: python manage.py test
