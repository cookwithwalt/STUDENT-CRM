from django.urls import path

from .views import (
    CourseCreateView,
    CourseDeleteView,
    CourseListView,
    CourseUpdateView,
    DashboardView,
    EnrollmentCreateView,
    EnrollmentDeleteView,
    EnrollmentListView,
    StudentCreateView,
    StudentDeleteView,
    StudentListView,
    StudentUpdateView,
    home_redirect,
)

urlpatterns = [
    path('', home_redirect, name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/add/', StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/add/', CourseCreateView.as_view(), name='course_add'),
    path('courses/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment_list'),
    path('enrollments/add/', EnrollmentCreateView.as_view(), name='enrollment_add'),
    path('enrollments/<int:pk>/delete/', EnrollmentDeleteView.as_view(), name='enrollment_delete'),
]
