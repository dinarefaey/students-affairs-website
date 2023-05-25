from django.contrib import admin
from django.urls import path
from main.views import home,instructions,CreateStudent, assign_department, change_student_status, delete_student, search_students, update_student,view_all_students
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("instructions",instructions,name='instructions'),
    path("create",CreateStudent.as_view(),name='create-student'),
    path("update/<id>",update_student,name='update-student'),
    path("students",view_all_students,name='view-students'),
    path("delete/<id>",delete_student,name='delete-student'),
    path("update/status/<id>",change_student_status,name='change-status'),
    path("update/department/<id>",assign_department,name='assign-department'),
    path("search",search_students,name="search-students")
]
