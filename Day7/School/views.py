from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import College,Student
from .forms import CollegeForm,StudentForm
def Home(request):
    college_data=College.objects.all()
    student_data=Student.objects.all()
    return render(request,'School/Home.html',{'CK':college_data,'SK':student_data})
def CollegeView(request):
    college_data=College.objects.all()
    return render(request,'School/College.html',{'CK':college_data})

def StudentView(request):
    student_data=Student.objects.all()
    return render(request,'School/Student.html',{'SK':student_data})

def CollegeStudentView(request,id):
    collegedata=College.objects.get(id=id)
    studentdata=Student.objects.filter(college=collegedata)
    return render(request,"School/CollegeStudentData.html",{'CK':collegedata,'SK':studentdata})

def AddCollege(request):
    form=CollegeForm()
    if request.method=='POST':
        form=CollegeForm(request.POST,request.FILES)
        if form.is_valid():
            College.objects.create(name=form.cleaned_data['name'],
            principal=form.cleaned_data['principal'],
            location=form.cleaned_data['location'],
            collegeimage=form.cleaned_data['collegeimage'])
        return redirect('college')
    return render(request,'School/AddCollege.html',{'form':form})

def AddStudent(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            Student.objects.create(name=form.cleaned_data['name'],
            college=form.cleaned_data['college'],
            branch=form.cleaned_data['branch'],
            semester=form.cleaned_data['semester'],
            studentimage=form.cleaned_data['studentimage'])
        return redirect('student')

    return render(request,'School/AddStudent.html',{'form':form})
