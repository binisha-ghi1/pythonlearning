from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the E-commerce Home Page")    
