from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('EDA1/', views.EDA1, name='EDA1'),
    path('EDA2/', views.EDA2, name='EDA2'),
    path('EDA3/', views.EDA3, name='EDA3'),
    path('EDA4/', views.EDA4, name='EDA4'),
    path('EDA5/', views.EDA5, name='EDA5'),
    path('EDA6/', views.EDA6, name='EDA6'),
    path('EDA7/', views.EDA7, name='EDA7'),
    path('EDA8/', views.EDA8, name='EDA8'),
    path('DataCleansing/', views.DataCleansing, name='DataCleansing')
]
