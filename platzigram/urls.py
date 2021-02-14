"""Platzigram URLs module."""

from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path('sorted/', views.sort_integers),
    path('hi/<str:name>/<int:age>/', views.say_hi),
]
