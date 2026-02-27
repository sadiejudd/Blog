
from django.urls import path
from . import views

app_name = "portfoliodatabase"

urlpatterns = [
    path('home/',views.home, name = "home"),
    path('hobbies/', views.hobbies, name = "hobbies"),
    path('portfolio/', views.portfolio, name = "portfolio"),
    path('contact/', views.contact, name = "contact"),
    path('hobbies/<int:id>/', views.hobby_details, name = 'HobbyDetails'),
    path('portfolio/<int:id>/', views.port_details, name ='PortDetails'),

] 