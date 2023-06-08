from django.db import models


class Project_b(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    description = models.CharField(max_length=250)

