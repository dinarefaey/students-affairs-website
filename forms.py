from dataclasses import fields
from django import forms
from .models import Student,DEPARTMENT_CHOICES

class UpdateStudentForm(forms.ModelForm):
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES,disabled=True)
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {"date_of_birth":forms.DateInput(attrs={"type":"date"})}


class AssignDepartmentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["id","name","department"]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {"date_of_birth":forms.DateInput(attrs={"type":"date"})}
