from django.db import models

class Student(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    grade = models.IntegerField()
    gpa = models.DecimalField(max_digits=3,decimal_places=2)
    classes = models.TextField(max_length=1000)