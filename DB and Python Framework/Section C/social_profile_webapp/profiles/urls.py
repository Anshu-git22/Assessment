from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('create/', views.create_profile, name='create_profile'),
    path('edit/<int:pk>/', views.edit_profile, name='edit_profile'),
    path('delete/<int:pk>/', views.delete_profile, name='delete_profile'),
    path('export/', views.export_profiles, name='export_profiles'),
]