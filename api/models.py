from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    idNo = models.PositiveIntegerField()
    courseName = models.CharField(max_length=50)
    courseId = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.surname