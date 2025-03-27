from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('photos.api_urls')),  # Toutes les URLs API
    path('', include('photos.urls')),  # Toutes les vues HTML
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)