from django.contrib import admin
from .models import Class, Student, Payment, Teacher
# Register your models here.
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Payment)
admin.site.register(Teacher)