from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


def get_default_term():
	return "Spring 2023"

# Create your models here.
class InstructorAddCourse(models.Model):
	course_instructor = models.ForeignKey(User, on_delete=models.CASCADE)
	course_name = models.CharField(max_length=255)
	course_number = models.CharField(max_length=255)
	course_instructor = models.CharField(max_length=255)
	description = models.CharField(max_length=800)
	total_time_commitment = models.DecimalField(max_digits=2, decimal_places=0, validators=[MinValueValidator(0)], default=0)
	has_discussion = models.CharField(choices=[('yes', 'Yes'),('no', 'No')], max_length=50, default='')
	num_ta_needed = models.DecimalField(max_digits=2, decimal_places=0, validators=[MinValueValidator(0)], default=0)
	curr_num_ta = models.IntegerField(default=0)
	graded_meeting = models.CharField(choices=[('yes', 'Yes'),('no', 'No')], max_length=50, default='')
	office_hours = models.DecimalField(max_digits=2, decimal_places=0, validators=[MinValueValidator(0)], default=0)
	other_info = models.CharField(max_length=800, default=None)
	term = models.CharField(default=get_default_term(), max_length=100)
