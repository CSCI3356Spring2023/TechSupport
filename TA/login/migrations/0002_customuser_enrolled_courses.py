# Generated by Django 4.1.7 on 2023-04-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="enrolled_courses",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
