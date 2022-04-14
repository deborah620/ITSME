from django.db import models

# Create your models here.


class Survey(models.Model):
    # models for the html front end survey results
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
