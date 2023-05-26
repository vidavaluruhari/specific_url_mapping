app2_name='ironman'
from django.urls import path
from app2.views import *
urlpatterns=[
    path('ironman/',ironman,name='ironman'),
 
]