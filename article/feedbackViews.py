from django.shortcuts import redirect, get_object_or_404

from .forms import FeedBackBadModelForm, FeedBackFairModelForm, FeedBackGoodModelForm
from .models import Article
from django.contrib import messages

def good_feedback_view(request, category_slug, article_slug):
    article = get_object_or_404(Article, slug=category_slug)
    obj = article
    obj.good = article.good + 1
    obj.save()
    messages.success(request, "Feedback sent")
    return redirect('article:article_detail', category_slug=category_slug, article_slug=article_slug)

def fair_feedback_view(request, category_slug, article_slug):
    article = get_object_or_404(Article, slug=category_slug)
    obj = article
    obj.fair = article.fair + 1
    obj.save()
    messages.success(request, "Feedback sent")
    return redirect('article:article_detail', category_slug=category_slug, article_slug=article_slug)

def bad_feedback_view(request, category_slug, article_slug):
    article = get_object_or_404(Article, slug=category_slug)
    obj = article
    obj.bad = article.bad + 1
    obj.save()
    messages.success(request, "Feedback sent")
    return redirect('article:article_detail', category_slug=category_slug, article_slug=article_slug)