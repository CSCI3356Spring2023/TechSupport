# Generated by Django 3.2.18 on 2023-04-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_application_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='course_number',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='application',
            name='description',
            field=models.CharField(default=None, max_length=800),
        ),
    ]
