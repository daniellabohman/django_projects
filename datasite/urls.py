from django.urls import path
from . import views
from .views import contact_view, success_view  

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success')
]
