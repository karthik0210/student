from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_course_success/', views.add_course_success, name='add_course_success'),
]
