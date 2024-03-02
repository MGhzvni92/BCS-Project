from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login_page'),
    path('logout', views.log_out, name='log_out'),
]
