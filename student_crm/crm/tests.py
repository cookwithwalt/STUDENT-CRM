from django.test import TestCase
from django.urls import reverse

from .models import Course, Enrollment, Student


class CRMModelTests(TestCase):
    def test_enrollment_string_representation(self):
        student = Student.objects.create(
            name='John Doe', email='john@example.com', phone='1234567890', address='Main street'
        )
        course = Course.objects.create(name='Physics', duration='10 Weeks', description='Intro course')
        enrollment = Enrollment.objects.create(student=student, course=course)
        self.assertIn('John Doe', str(enrollment))


class DashboardTests(TestCase):
    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
