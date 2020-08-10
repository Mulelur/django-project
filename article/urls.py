from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('<str:article_slug>/', views.article_list, name='article_list'),
    path('<str:category_slug>/<str:article_slug>/', views.article_detail, name='article_detail'),
]