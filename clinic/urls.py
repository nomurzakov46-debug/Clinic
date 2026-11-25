from django.urls import path
from .import views

urlpatterns = [
    path('directions/',views.direction_list,name='direction_list'),
    path('directions/<slug:slug>/',views.direction_detail,name='direction_detail'),
    path('doctors/',views.doctor_list,name='doctor_list'),
    path('doctors/<int:pk>/',views.doctor_detail,name='doctor_detail'),
    path('appointment/',views.appointment_create,name='appointment_create'),
    path('callback/',views.callback_create,name='callback_create'),
    
    
]