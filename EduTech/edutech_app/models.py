from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    pass


class Subject(models.Model):
    name = models.TextField(max_length=50)
    objects = models.Manager()


class Teacher(models.Model):
    name = models.TextField(max_length=50)
    avatar = models.ImageField()
    description = models.TextField(max_length=800)
    subject = models.ManyToManyField(Subject)
    objects = models.Manager()


class ClassNumber(models.Model):
    number = models.IntegerField()
    objects = models.Manager()


class Course(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=800)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    classNumber = models.ForeignKey(to=ClassNumber, on_delete=models.CASCADE)
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)
    header1 = models.TextField(max_length=50)
    description1 = models.TextField(max_length=800)
    header2 = models.TextField(max_length=50)
    description2 = models.TextField(max_length=800)
    header3 = models.TextField(max_length=50)
    description3 = models.TextField(max_length=800)
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('course', kwargs={'course_id': self.pk})


class CurrentCourse(models.Model):
    c_course_id = models.IntegerField()
    c_name = models.TextField(max_length=60)
    c_classNumber = models.IntegerField()
    objects = models.Manager()
