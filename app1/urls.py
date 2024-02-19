from django.urls import path
# from app1 import views
# from app1.views import index
from app1.views import *
#i will try my

urlpatterns = [
    # path('', views.index, name='home')
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
]