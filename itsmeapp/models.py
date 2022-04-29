from django.db import models

# Create your models here.


class Survey(models.Model):
    # models for the html front end survey inputs
    gender = models.TextField()
    ethnicity = models.TextField()
    grade = models.TextField()
    major = models.TextField()
    discussion = models.TextField()
    gpa = models.TextField()
    program = models.TextField()
    professional = models.TextField()
    enrollment = models.TextField()
    prior = models.TextField()
    internship = models.BooleanField()
    research = models.BooleanField()
    parent_engineer = models.BooleanField()
    family_engineer = models.BooleanField()

class Results(models.Model):
    # models for the html front end survey results
    score_1 = models.TextField()
    score_2 = models.TextField()
    score_3 = models.TextField()
    score_4 = models.TextField()
    score_5 = models.TextField()
    score_6 = models.TextField()
    score_7 = models.TextField()
    score_8 = models.TextField()
    score_9 = models.TextField()
    score_10 = models.TextField()
    score_11 = models.TextField()
    score_12 = models.TextField()
    score_13 = models.TextField()
    score_14 = models.TextField()
    score_15 = models.TextField()
    eps_total = models.TextField()
    spve = models.TextField()
    me = models.TextField()