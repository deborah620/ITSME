from django.db import models

# Create your models here.


class Survey(models.Model):
    text = models.TextField()
