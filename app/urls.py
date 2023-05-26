app_name='nara'
from django.urls import path
from app.views import *
urlpatterns=[
    path('nara/',nara,name='nara'),
]