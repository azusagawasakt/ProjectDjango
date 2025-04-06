from django.urls import path
from . import views

urlpatterns = [
    path('', views.row, name='home'),
]
