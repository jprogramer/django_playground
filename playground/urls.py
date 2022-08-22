from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('add_object/<str:vul>/', views.add_object),
    path('analyse/', views.analyse),
]