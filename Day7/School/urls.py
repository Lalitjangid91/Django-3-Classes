from django.urls import path
from . import views
urlpatterns=[
    path('',views.Home,name='home'),
    path('college/',views.CollegeView,name='college'),
    path('addcollege/',views.AddCollege,name='addcollege'),
    path('addstudent/',views.AddStudent,name='addstudent'),
    path('student/',views.StudentView,name='student'),
    path('colleges/<int:id>',views.CollegeStudentView,name='collegestudent'),

]
