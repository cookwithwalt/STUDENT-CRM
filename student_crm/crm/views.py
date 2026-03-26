from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from .forms import CourseForm, EnrollmentForm, StudentForm
from .models import Course, Enrollment, Student


class DashboardView(TemplateView):
    template_name = 'crm/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'student_count': Student.objects.count(),
                'course_count': Course.objects.count(),
                'enrollment_count': Enrollment.objects.count(),
                'recent_enrollments': Enrollment.objects.select_related('student', 'course')[:5],
            }
        )
        return context


class StudentListView(ListView):
    model = Student
    template_name = 'crm/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(email__icontains=query))
        return queryset


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'crm/form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, 'Student created successfully.')
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'crm/form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, 'Student updated successfully.')
        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'crm/confirm_delete.html'
    success_url = reverse_lazy('student_list')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'Student deleted successfully.')
        return super().post(request, *args, **kwargs)


class CourseListView(ListView):
    model = Course
    template_name = 'crm/course_list.html'
    context_object_name = 'courses'


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'crm/form.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        messages.success(self.request, 'Course created successfully.')
        return super().form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'crm/form.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        messages.success(self.request, 'Course updated successfully.')
        return super().form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'crm/confirm_delete.html'
    success_url = reverse_lazy('course_list')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'Course deleted successfully.')
        return super().post(request, *args, **kwargs)


class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'crm/enrollment_list.html'
    context_object_name = 'enrollments'

    def get_queryset(self):
        return Enrollment.objects.select_related('student', 'course')


class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'crm/form.html'
    success_url = reverse_lazy('enrollment_list')

    def form_valid(self, form):
        messages.success(self.request, 'Enrollment created successfully.')
        return super().form_valid(form)


class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'crm/confirm_delete.html'
    success_url = reverse_lazy('enrollment_list')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'Enrollment deleted successfully.')
        return super().post(request, *args, **kwargs)


def home_redirect(_request):
    return redirect('dashboard')
