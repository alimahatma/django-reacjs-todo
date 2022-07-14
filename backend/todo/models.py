from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

# class Tugas(models.Model):
#     title = models.CharField(max_length=100)
#     time = models.TimeField()

    def __str__(self):
        return self.title

