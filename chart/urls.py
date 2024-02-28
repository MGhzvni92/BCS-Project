from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_chart, name='show_chart'),
]
