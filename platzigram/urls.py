"""Platzigram URLs module."""

from django.urls import path
from . import views as local_views
from posts import views as posts_vews

urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),
    path('posts/', posts_vews.list_posts),
]
