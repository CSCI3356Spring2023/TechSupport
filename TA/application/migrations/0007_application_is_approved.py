# Generated by Django 4.1.7 on 2023-05-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0006_alter_application_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
    ]
