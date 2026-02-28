# converter/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.main_page, name ='main_page' ),
    path('length/', views.length_converter, name='length_converter'),
    path('weight/' , views.weight_converter ,name='weight_converter'),
    path('temperature/', views.temprature_converet , name='temperature_converter')
]