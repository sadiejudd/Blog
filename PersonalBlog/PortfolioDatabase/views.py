from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby

# Create your views here.
def home(request):
    return HttpResponse("""<strong>Welcome!</strong> 
    My name is Sadie Judd. I am a Computer Science student at Weber State University.
    I spend a lot of time studying and working, but I also like spending time with friends and family,
    playing with my dog, and spening time outdoors.""")
   

def hobbies(request):
    hobbies = Hobby.objects.all()
    output = ""
    for hobby in hobbies:
        output+= f"{hobby.hobby_name}: {hobby.hobby_desc}\n"
    return HttpResponse(output)

    


def portfolio(request):
    return

def contact(request):
    return HttpResponse("Student Email: sadiejudd@mail.weber.edu")

