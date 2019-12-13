from django.shortcuts import render
from django.http import HttpResponse
from .models import BoyModel
def BoyHome(request):
    objs=BoyModel.objects.all()
    return render(request,'Boy/Home.html',{'Key':objs})
def AddBoy(request):
    request.GET.
    return render(request,'Boy/AddBoy.html')
