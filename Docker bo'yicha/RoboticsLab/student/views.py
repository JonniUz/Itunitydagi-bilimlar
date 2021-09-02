from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django_filters.views import FilterView

from . import filters
from .models import Class, Student, Payment, Teacher


class ClassListView(generic.ListView):
    model = Class
    template_name = 'student/group.html'


class StudentListView(generic.ListView):
    model = Student
    template_name = 'student/student.html'


class PaymentSearchResultsListView(FilterView):
    model = Payment
    template_name = 'student/payment.html'
    filterset_class = filters.PaymentFilter


class TeacherListView(generic.ListView):
    model = Teacher
    template_name = 'student/teacher.html'


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'student/teacher-detail.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/student-detail.html'


class ClassDetailView(DetailView):
    model = Class
    template_name = 'student/group-detail.html'
