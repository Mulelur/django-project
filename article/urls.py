from django.urls import path
from . import views
from .feedbackViews import good_feedback_view, fair_feedback_view, bad_feedback_view
from .views import search

app_name = 'article'

urlpatterns = [
    path('<str:category_slug>/', views.article_list, name='article_list'),
    path('<str:category_slug>/<str:article_slug>/', views.article_detail, name='article_detail'),
    path('good/<category_slug>/<article_slug>/feedback/', good_feedback_view, name='good_feedback'),
    path('fair/<category_slug>/<article_slug>/feedback/', fair_feedback_view, name='fair_feedback'),
    path('bad/<category_slug>/<article_slug>/feedback/', bad_feedback_view, name='bad_feedback'),
    path('support/article/search/results/', search, name='search')
]