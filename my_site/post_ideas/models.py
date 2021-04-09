from django.db import models

# Create your models here.
class Idea_Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    createdby_id = models.IntegerField()