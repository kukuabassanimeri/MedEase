from django.contrib import admin
from django.urls import path
from . import views

app_name = 'med_ease'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('queue/', views.queue, name='queue'),
    path('contact/', views.contact, name='contact'),
    
]