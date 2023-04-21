from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
   ROLE_CHOICES = (
       ('S', 'Student'),
       ('T', 'Teacher'),
       ('A', 'Admin'),
   )
   role = models.CharField(max_length=1, choices=ROLE_CHOICES)


   applications = models.PositiveIntegerField(default=0)


   major = models.CharField(max_length=100, blank=True)
   eagle_id = models.CharField(max_length=8, blank=True)
   year = models.CharField(max_length=20, blank=True)


   def can_apply(self):
       if self.role == 'S' and self.applications >= 5:
           return False
       else:
           return True


   def increment_applications(self):
       if self.role == 'S':
           self.applications += 1
           self.save()


