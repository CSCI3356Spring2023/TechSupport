from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from InstructorAddCourse.models import InstructorAddCourse
from login.models import CustomUser

# Create your models here.
class Application(models.Model):
    is_approved = models.BooleanField(default=False)
    course_name = models.CharField(max_length=200, default=None, blank = False, null=False)
    course_number = models.CharField(max_length=200, default=None)
    description = models.CharField(max_length=800, default=None)
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    eagle_id = models.CharField(max_length=255, default=None)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    
    GRADES = (
        ('--', '--'),
        ('a', 'A'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('c+', 'C+'),
        ('c', 'C'),
        ('c-', 'C-'),
        ('d+', 'D+'),
        ('d', 'D'),
        ('d-', 'D-'),
        ('f', 'F'),
        ('n/a', 'N/A')
    )
    
    GRAD = (
        ('--', '--'),
        ('2023','2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026')
    )
    
    grad = models.CharField(max_length=50, choices=GRAD, default='')

    past_course = models.CharField(choices=[('yes', 'Yes'),('no', 'No')], max_length=50, default='')
        #in form: define radioselect with class "horizontal-list"
        #in css: .horizontal-list li {
                    #display: inline-block;
                    #margin-right: 10px;
        #}
    grade = models.CharField(max_length=50, choices=GRADES, default='')
        #in form: define textinput with class "combobox"
    hours = models.DecimalField(max_digits=2, decimal_places=0, validators=[MinValueValidator(0)], default=0)
        #in form: define NumberInput with attr min: 0
    other_courses = models.CharField(max_length=800, default=None)
        #in form: define textarea with attr 5 rows
    misc_information = models.CharField(max_length=800, default=None)

   




