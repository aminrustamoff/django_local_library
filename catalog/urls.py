from django.urls import path
from . import views

# The URL configuration for the catalog app.
urlpatterns = [
    path('', views.index, name='index'),
]

