from django.shortcuts import render
from django.http import HttpResponse
from .models import GirlModel
def GirlHome(request):
    objs=GirlModel.objects.all()
    return render(request,'Girl/Home.html',{'Key':objs})
