from django.contrib import admin
from .models import Course, Teacher, Lesson, Profile

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
