from django.urls import path, include
from . import rest_views

urlpatterns = [
    path('api/', rest_views.CourseListView.as_view()),
    path('api/<int:pk>', rest_views.CourseDetailView.as_view()),
    path('api/user/', rest_views.UserCreateAPIView.as_view()),
    path('api/profile/create/', rest_views.ProfileCreateAPIView.as_view()),
    path('api/auth/', include('rest_framework.urls')),
]
