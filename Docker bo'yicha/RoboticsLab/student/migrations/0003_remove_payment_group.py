# Generated by Django 3.2.4 on 2021-08-05 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210805_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='group',
        ),
    ]