from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    group = models.ForeignKey(Group, related_name='persons', on_delete=models.PROTECT)
