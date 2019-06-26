from django.conf.urls import url
from college_erp import views

urlpatterns = [
    url('login', views.loginList.as_view()),
    url('signup', views.signupList.as_view()),
    url('student', views.studentList.as_view()),
    url('department', views.departmentList.as_view()),
    url('subject', views.subjectList.as_view()),
    url('college', views.collegeList.as_view()),
    url('faculty', views.facultyList.as_view()),  
]