# Generated by Django 3.2.18 on 2023-04-22 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InstructorAddCourse', '0005_instructoraddcourse_term'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructoraddcourse',
            old_name='course_description',
            new_name='description',
        ),
    ]