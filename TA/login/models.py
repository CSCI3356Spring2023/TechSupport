from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('S', 'Student'),
        ('T', 'Teacher'),
        ('A', 'Admin'),
    )
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    
    enrolled_courses = models.PositiveIntegerField(default=0)

    def increment_enrolled_courses(self):
        if self.role == 'S':
            self.enrolled_courses += 1
            self.save()
