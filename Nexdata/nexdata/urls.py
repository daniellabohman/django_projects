from django.urls import path
from nexdata import views

urlpatterns = [
    path('', views.main, name='main'),
    path('contact/', views.contact, name='contact'), 
    path('about/', views.about, name='about'),        
    path('portfolio/', views.portfolio, name='portfolio'),  
]
