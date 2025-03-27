# photos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list_page, name='photo_list'),  # Page d'accueil
    path('upload/', views.photo_upload_page, name='photo_upload'),
    path('photo/<int:pk>/', views.photo_detail_page, name='photo_detail'),
    path('photo/<int:pk>/delete/', views.photo_delete_page, name='photo_delete'),
]