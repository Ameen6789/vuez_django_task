# Generated by Django 5.1.2 on 2024-11-04 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='created_date',
        ),
    ]