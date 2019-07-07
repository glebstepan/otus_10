from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='static/img/course/', blank=True, null=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Lesson(models.Model):
    course = models.ForeignKey('Course', related_name='lessons', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.course}): {self.start_time}"

    class Meta:
        ordering = ('start_time',)


class Profile(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey('Course', related_name='courses', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.student} > {self.course}"
