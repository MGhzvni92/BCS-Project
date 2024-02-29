from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


v1_urlpatterns = [    
    path('', include('bcs_api.urls')),    
]

urlpatterns = [
    path('', include('home_module.urls')),
    path('', include('account_module.urls')),
    path('chart/', include('chart.urls')),
    path('bcs/', include('bcs.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1_urlpatterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
