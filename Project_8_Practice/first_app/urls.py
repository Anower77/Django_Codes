from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('form/', views.form, name="formpage"),
    path('students/', views.student_list_view, name='student_list')
    
]
