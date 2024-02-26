from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login_page'),

    # path('reset-password', views.RegisterView.as_view(), name='reset_password')

]