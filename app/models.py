from django.db import models

# Create your models here.
class Student(models.Model):
    student=models.CharField( max_length=50)
    number=models.IntegerField()
    city=models.CharField(max_length=50)
