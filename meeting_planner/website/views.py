from datetime import datetime
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting

# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html", {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

# About page
def about(request):
    return HttpResponse("This is the About page")
