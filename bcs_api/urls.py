from django.urls import path
from . import views

app_name = 'bcs_api'
urlpatterns = [
    path('import', views.ImportView.as_view(), name='import_data'),
]
