from django.urls import path
from . import views

app_name = 'chart'

urlpatterns = [
    path('', views.show_chart, name='show_chart'),
]
