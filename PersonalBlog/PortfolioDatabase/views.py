from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Hobby
from .models import Portfolio
from django.template import loader


# Create your views here.
def home(request):
  template = loader.get_template('PortfolioDatabase/index.html')
  return HttpResponse(template.render({}, request))
   

def hobbies(request):
    hobbies = Hobby.objects.all()
    template = loader.get_template('PortfolioDatabase/hobby.html')
    context = {
        'hobbies': hobbies
    }
    return HttpResponse(template.render(context, request))
    

    


def portfolio(request):
    portfolio = Portfolio.objects.all()
    output = ""
    for port in portfolio:
        output += f"{port.port_name}: {port.port_desc}<br></br>"
    return HttpResponse(output)

def contact(request):
    return HttpResponse("Student Email: sadiejudd@mail.weber.edu")

def hobby_details(request, id):
    hobby = get_object_or_404(Hobby, id = id)
    template = loader.get_template('PortfolioDatabase/hobby_details.html')
    context = {
        "hobby": hobby
    }
    return HttpResponse(template.render(context, request))
    
