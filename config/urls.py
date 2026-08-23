from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinic.urls')),
    path('accounts/', include('accounts.urls')),
    path('appointments/', include('appointments.urls')),
]

# Explicitly serve static files in production
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)