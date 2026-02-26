
from django.urls import path
from . import views

app_name = "portfoliodatabase"

urlpatterns = [
    path('home/',views.home, name = "home"),
    path('hobbies/', views.hobbies),
    path('portfolio/', views.portfolio),
    path('contact/', views.contact),
    path('hobbies/<int:id>/', views.hobby_details, name = 'HobbyDetails'),

] 