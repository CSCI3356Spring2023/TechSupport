# Generated by Django 4.1.7 on 2023-05-10 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0004_customuser_eagle_id_customuser_major_customuser_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(max_length=100),
        ),
    ]