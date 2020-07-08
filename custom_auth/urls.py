from django.contrib import admin
from django.urls import path, include

from .views import index, login, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('', index),
    path('logout/', logout, name='logout'),
]