from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('contact-us', views.contact_page, name='contact-page')
    # path('site-header', views.site_header_component, name='site_header_partial')
    # path('articles', views.articles, name='articles-page'),
    # path('project', views.project, name='project-page')
]