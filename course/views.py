from django.http import HttpResponse
from .models import Teacher, Course, Lesson, Profile
from django.views.generic.list import ListView

class CourseListView(ListView):

    model = Course