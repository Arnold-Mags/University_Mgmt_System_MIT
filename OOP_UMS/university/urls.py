from django.urls import path
from . import views
from django.contrib import admin

app_name = 'university'

urlpatterns = [
    path('', views.index, name='index'),
]