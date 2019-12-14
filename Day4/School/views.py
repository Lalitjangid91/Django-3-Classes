from django.shortcuts import render
from .models import College,Student
def Home(request):
    college_data=College.objects.all()
    student_data=Student.objects.all()
    return render(request,'School/Home.html',{'CK':college_data,'SK':student_data})
