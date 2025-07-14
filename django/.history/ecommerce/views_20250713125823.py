from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpsResponse('Hello,welcome to the ecommerce site!')     
