from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

# Redirect root to your frontend
def redirect_to_frontend(request):
    return redirect("https://povalogistics-com.vercel.app/")  # replace with your Vercel URL

urlpatterns = [
    # Root path redirects to frontend
    path('', redirect_to_frontend),

    # Admin panel
    path('admin/', admin.site.urls),

    # API routes
    path('api/', include('api.urls')),
]

# Serve media files in debug/dev mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
