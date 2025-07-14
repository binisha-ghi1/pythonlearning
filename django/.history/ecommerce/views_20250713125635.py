from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Hello,welcome to the ecommerce site!')  # Adjust the template name as needed    
