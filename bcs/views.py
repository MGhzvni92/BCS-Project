from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model

class ChartView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

def index(request):
    return render(request, 'bcs/index.html')

def login(request):
    return render(request, 'bcs/login.html')

def article_list(request):
    return render(request, 'bcs/article_list.html')

def article_details(request, slug):
    # article = next(article for article in )
    return render(request, 'bcs/article_detail.html')

def project_details(request, slug):
    return render(request, 'bcs/project.html')