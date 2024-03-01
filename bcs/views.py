from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model


def index(request):
    return render(request, 'bcs/index.html')

def login(request):
    return render(request, 'bcs/login.html')

