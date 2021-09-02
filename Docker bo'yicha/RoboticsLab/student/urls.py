from django.urls import path
from . import views

urlpatterns = [
    path('group/', views.ClassListView.as_view(), name='group'),
    path('group/<int:pk>/', views.ClassDetailView.as_view(), name='group-detail'),
    path('student/', views.StudentListView.as_view(), name='student'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('payment/', views.PaymentSearchResultsListView.as_view(), name='payment'),
    path('teacher/', views.TeacherListView.as_view(), name='teacher'),
    path('teacher/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
]