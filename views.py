from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView
from django.contrib import messages
from django.http import HttpResponseBadRequest,HttpResponse,Http404
from main.forms import AssignDepartmentForm, StudentForm, UpdateStudentForm
from main.models import Student


def home(request):
    return render(request,"main/home.html")


def instructions(request):
    return render(request,"main/instructions.html")

def update_student(request,id):
    student = get_object_or_404(Student,id=id)
    form = UpdateStudentForm(instance=student)
    if request.method == "POST":
        form = UpdateStudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,"Student Information Updated")
            return redirect("view-students")
    return render(request,"main/update.html",{"form":form,"student":student})

def assign_department(request,id):
    student = get_object_or_404(Student,id=id)
    form = AssignDepartmentForm(instance=student)
    if student.level!="3":
        form.fields["department"].disabled = True
        messages.error(request,"Only level 3 students can change department")
    if student.level=="3" and request.method=="POST":
        form = AssignDepartmentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,"Student Department Updated")
    return render(request,"main/assign_department.html",{"form":form,"student":student})


def change_student_status(request,id):
    if request.method!="POST":
        return Http404()
    student = get_object_or_404(Student,id=id)
    status = request.GET.get("status")
    if status not in ["active","inactive"]:
        return HttpResponseBadRequest("Please provide valid status")
    student.status = status
    student.save()
    return HttpResponse({"msg":"Status updated","status":status})

def search_students(request):
    name = request.GET.get("name")
    students = []
    if name:
        students = Student.objects.filter(name__icontains=name,status="active")
        print(students)
        if(students.count()==0):
            messages.info(request,"No active students found")
    return render(request,"main/search.html",{"students":students})

def view_all_students(request):
    students = Student.objects.all()
    return render(request,"main/view.html",{"students":students})

def delete_student(request,id):
    if request.method!="POST":
        return Http404()
    student = get_object_or_404(Student,id=id)
    student.delete()
    return HttpResponse("Student deleted")

class CreateStudent(CreateView):
    model = Student
    template_name = "main/add.html"
    form_class = StudentForm

