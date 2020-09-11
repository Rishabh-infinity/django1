from django.shortcuts import render
from .models import Talking

# Create your views here.
def index(request):
    return render(request,"index.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")

def home(request):
    return render(request,"index.html")

def blog(request):
    return render(request,"blog.html")

def elements(request):
    return render(request,"elements.html")

def portfolio(request):
    return render(request,"portfolio.html")

def about(request):
    return render(request,"about.html")

def single_blog(request):
    return render(request,"single-blog.html")

def message_sent(request):
    name = request.POST['name']
    message = request.POST['message']
    email = request.POST['email']
    subject = request.POST['subject']

    talk = Talking(name=name,message=message,email=email,subject=subject)
    talk.save()
    return render(request,"index.html")
