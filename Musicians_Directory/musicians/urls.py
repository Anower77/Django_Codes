# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name="homepage"),
#     # path('')
    
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('add-musician/', views.add_musician, name="add_musician"),
    path('edit-musician/<int:pk>/', views.edit_musician, name="edit_musician"),
    path('delete-musician/<int:pk>/', views.delete_musician, name="delete_musician"),
]
