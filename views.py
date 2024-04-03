from django.shortcuts import render
from django.http import HttpResponse
from .models import teacher

//handles requests for the index page
def index(request):
    //retrieves all teacher objects from the database
    teach = teacher.objects.all()
    //render the html template
    return render(request,"MyApp1/index.html",{'content': teach})

//this one is uneccessary but i keep it anyways
def studenthome(request):
    //returning the http response that shows this page is up and running
    return HttpResponse("Student Home Page")

def studenthome(request):
    //render the html file for student home page
    return render(request, 'MyApp1/studenthome.html')
