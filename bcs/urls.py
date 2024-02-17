from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='starting-page'),
    path('chart', views.ChartView.as_view(), name='chart_page'),
    # path('login', views.login, name='login-page'),
    # path('articles', views.articles, name='articles-page'),
    # path('project', views.project, name='project-page'),


    # path('login/<slug:slug>' , name=''),
    path('', views.article_list, name='article-list'),
    path('<slug:slug>', views.article_details, name='articles-details-page'),
    path('project/<slug:slug>', views.project_details, name='project-details-page'),
]