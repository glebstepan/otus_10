from django.test import TestCase
import pytz

from datetime import datetime

from .serializers import CourseSerializer, TeacherSerializer, LessonSerializer, ProfileSerializer

from .models import Course, Teacher, Lesson, Profile
# Create your tests here.

class CourseTestCase(TestCase):

    def test_CourseSerializer(self):
        start_date = '2019-08-10'

        instance = Course.objects.create(title='titleTest', description='descriptionTest', start_date=start_date)

        serialized = CourseSerializer(instance)
        max_length = Course._meta.get_field('title').max_length
        self.assertEqual(serialized.data['title'], 'titleTest')
        self.assertEquals(max_length, 50)
        self.assertEqual(serialized.data['description'], 'descriptionTest')
        self.assertEqual(serialized.data['start_date'], start_date)


class TeacherTestCase(TestCase):

    def test_TeacherSerializer(self):
        course = Course.objects.create(title='titleTest', description='descriptionTest', start_date='2019-08-10')
        instance = Teacher.objects.create(name='nameTest', course=course)

        serialized = TeacherSerializer(instance)
        max_length = Teacher._meta.get_field('name').max_length

        self.assertEqual(serialized.data['name'], 'nameTest')
        self.assertEquals(max_length, 50)
        self.assertEqual(serialized.data['course'], 1)


class LessonTestCase(TestCase):

    def test_LessonSerializer(self):
        instance = Lesson.objects.create(name='nameTest')

        serialized = LessonSerializer(instance)
        max_length = Lesson._meta.get_field('name').max_length

        self.assertEqual(serialized.data['name'], 'nameTest')
        self.assertEquals(max_length, 50)

