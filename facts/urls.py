from django.urls import path, include
from . import views

urlpatterns = [
    path("technology/", views.getFact)
]
