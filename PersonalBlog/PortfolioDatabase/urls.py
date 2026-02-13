
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('hobbies/', views.hobbies),
    path('portfolio/', views.portfolio),
    path('contact/', views.contact),

]