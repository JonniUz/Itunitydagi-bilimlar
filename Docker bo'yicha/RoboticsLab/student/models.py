from django.utils import timezone

from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    birthday = models.DateField(default=timezone.now)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Class(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    birthday = models.DateField(default=timezone.now)
    group = models.ForeignKey(Class, on_delete=models.PROTECT, related_name='students')
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name

class Payment(models.Model):
    MONTH = [
        ('January', 'January'), ('February', 'February'),
        ('March', 'March'), ('April', 'April'),
        ('May', 'May'), ('June', 'June'),
        ('July', 'July'), ('August', 'August'),
        ('September', 'September'), ('October', 'October'),
        ('November', 'November'), ('December', 'December'),
    ]
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    month = models.CharField(choices=MONTH, max_length=255)
    date_paid = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.student.first_name


