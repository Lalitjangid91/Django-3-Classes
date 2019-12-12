from django.http import HttpResponse
def Home(request):
    return HttpResponse("<h1>WelCome to Home Page</h1>")
