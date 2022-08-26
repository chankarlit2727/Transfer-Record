from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('record_data/', views.record_data, name='record_data'),
    path('record_data/delete/<pk>/', views.delete, name='delete'),
]