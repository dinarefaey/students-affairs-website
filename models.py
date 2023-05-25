from django.db import models
from django.urls import reverse

GENDER_CHOICES = (
    ("M","Male"),
    ("F","Female")
)
LEVEL_CHOICES = (
    ("1","Level One"),
    ("2","Level Two"),
    ("3","Level Three"),
    ("4","Level Four"),
)
STATUS_CHOICES = (
    ("active","Active"),
    ("inactive","Inactive")
)
DEPARTMENT_CHOICES = (
    ("CS","Computer Science"),
    ("IS","Information Systems"),
    ("IT","Information Technology"),
    ("AI","Artificial Intelligence"),
    ("DS","Operation Research and Decision Support")
)
class Student(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=120,unique=True)
    mobile = models.CharField(max_length=12)
    date_of_birth = models.DateField()
    gpa = models.FloatField()
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)
    level = models.CharField(choices=LEVEL_CHOICES,max_length=1)
    status = models.CharField(choices=STATUS_CHOICES,max_length=10)
    department = models.CharField(choices=DEPARTMENT_CHOICES,max_length=2)

    def get_absolute_url(self):
        return reverse("view-students")

    def __str__(self):
        return f"ID:{self.id},Name:{self.name}"