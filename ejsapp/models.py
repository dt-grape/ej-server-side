from django.db import models
from django.contrib.auth.models import User



class Subject(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    group_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Student(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Date(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"Дата: {self.date}"


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    mark = models.CharField(max_length=5)

    def __str__(self):
        return str(self.mark)


