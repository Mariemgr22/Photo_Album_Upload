from django.urls import path
from . import views

urlpatterns = [
    path('photos/', views.photo_list, name='photo_list_api'),
    path('photos/upload/', views.photo_upload, name='photo_upload_api'),
    path('photos/<int:pk>/', views.photo_detail, name='photo_detail_api'),
    path('photos/<int:pk>/update/', views.photo_update, name='photo_update_api'),
    path('photos/<int:pk>/delete/', views.photo_delete, name='photo_delete_api'),
]