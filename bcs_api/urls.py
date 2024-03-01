from django.urls import path
from . import views

app_name = 'bcs_api'

urlpatterns = [
    path('import', views.ImportView.as_view(), name='import_data'),
    path('api-login', views.ApiLogin.as_view(), name='api_login'),
]
