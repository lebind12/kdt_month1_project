from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('EDA/', views.EDA, name='EDA'),
    path('DataCleansing/', views.DataCleansing, name='DataCleansing')
]
