# Generated by Django 4.1.7 on 2023-04-20 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("InstructorAddCourse", "0004_instructoraddcourse_curr_num_ta"),
    ]

    operations = [
        migrations.AddField(
            model_name="instructoraddcourse",
            name="term",
            field=models.CharField(default="Spring 2023", max_length=100),
        ),
    ]