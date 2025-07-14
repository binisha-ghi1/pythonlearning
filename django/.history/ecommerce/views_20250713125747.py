from django.shortcuts import render

# Create your views here.
def home(request):
    return httpsResponce(request, 'Hello,welcome to the ecommerce site!')     
