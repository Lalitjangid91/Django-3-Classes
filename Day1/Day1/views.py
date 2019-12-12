from django.http import HttpResponse
from django.shortcuts import render
def f(request):
    return render(request,'home.html',{'Key':['Lalit','Sahil','Bharti','Jahid']})
