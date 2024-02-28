from django.contrib import admin
from django.urls import path, include


v1_urlpatterns = [    
    path('', include('bcs_api.urls')),    
]

urlpatterns = [
    path('', include('home_module.urls')),
    path('', include('account_module.urls')),
    path('bcs/', include('bcs.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1_urlpatterns)),
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
