from django.urls import path
from ecomerce import views

urlpatterns = [
    path('home/', views.home),
]
