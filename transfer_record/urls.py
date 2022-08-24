from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<pk>', views.delete, name='delete'),
]