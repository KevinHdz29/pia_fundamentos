from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('cortes/', views.cortes, name='cortes'),
    path('personal/', views.personal, name='personal'),
    path('contacto/', views.contacto, name='contacto'),
]