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
    
    applications = models.PositiveIntegerField(default=0)

    def can_apply(self):
        if self.role == 'S' and self.applications >= 5:
            return False
        else:
            return True
    
    def increment_applications(self):
        if self.role == 'S':
            self.applications += 1
            self.save()
