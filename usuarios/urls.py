from django.urls import path, include
from . import views
urlpatterns = [
    path('contactar/', views.contactar, name = "contactar"),
    path('perfil/<int:id>', views.perfil, name= "perfil")   
]