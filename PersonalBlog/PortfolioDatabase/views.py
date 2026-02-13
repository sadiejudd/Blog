from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<strong>Welcome!</strong>")

def hobbies(request):
    return

def portfolio(request):
    return

def contact(request):
    return HttpResponse("Student Email: sadiejudd@mail.weber.edu")

