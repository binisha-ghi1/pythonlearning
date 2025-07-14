from django.urls import pathfrom ecomerce import views

urlpatterns = [
    path('home/', views.home),
]
