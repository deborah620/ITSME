from django.db import models

# Create your models here.


class Survey(models.Model):
    # models for the html front end survey results
    # objects = models.Manager()
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
    previous_school_impact = models.TextField()
    finish_degree = models.TextField()
    finish_degree_here = models.TextField()
    technology_importance = models.TextField()
    parents_disprove_difft = models.TextField()
    engineer_fix_world = models.TextField()
    engineer_paid = models.TextField()
    parents_want = models.TextField()
    job_guarantee = models.TextField()
    faculty_encor = models.TextField()
    mentor_encor = models.TextField()
    intro_opportunity = models.TextField()
    feel_good = models.TextField()
    like_build = models.TextField()
    engineer_fun = models.TextField()
    use_society = models.TextField()
    engineer_interesting = models.TextField()
    figure_out_work = models.TextField()
    mentoring_program = models.TextField()

