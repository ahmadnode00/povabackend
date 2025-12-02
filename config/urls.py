from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # During development, redirect root to the frontend dev server
    # Change or remove this if you build the frontend and serve static files from Django
    path('', RedirectView.as_view(url='http://localhost:3001/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include API routes
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
