from django.urls import path, include
from . import views


urlpatterns = [
    path('api/', views.CourseListView.as_view()),
    path('api/<int:pk>', views.CourseDetailView.as_view()),
    path('api/user/', views.UserCreateAPIView.as_view()),
    path('api/profile/create/', views.ProfileCreateAPIView.as_view()),
    path('api/auth/', include('rest_framework.urls')),
]
