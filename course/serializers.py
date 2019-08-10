from rest_framework import serializers
from .models import Teacher, Course, Lesson, Profile
from django.contrib.auth.models import User


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Teacher
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ('title', 'description', 'lessons', 'start_date')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):

    courses = CourseSerializer(read_only=True, many=True)
    student = serializers.ReadOnlyField(source='student.username')

    class Meta:
        model = Profile
        fields = ('courses', 'student')
