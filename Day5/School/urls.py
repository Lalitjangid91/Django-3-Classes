from django.urls import path
from . import views
urlpatterns=[
    path('',views.Home,name='home'),
    path('college/',views.CollegeView,name='college'),
    path('school/',views.StudentView,name='student')
]
