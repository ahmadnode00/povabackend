from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
# Admin panel
path('admin/', admin.site.urls),

```
# API routes
path('api/', include('api.urls')),

# Root URL redirects to backend domain
path('', RedirectView.as_view(url='https://backend.apexbitcargo.com/', permanent=False)),
```

]

# Serve media files in debug/dev mode

if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

