from django.shortcuts import render

# Create your views here.
def home(request):
    return httpsResponse(request, 'Hello,welcome to the ecommerce site!')     
