# assistant/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='assistant-home'),
]
