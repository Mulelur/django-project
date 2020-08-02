from django.shortcuts import render, get_object_or_404
from .models import Article, Category


def article_list(request):
    template = 'article/article_list.html'
    article = Article.objects.filter(category=category)
    categories = Category.objects.all()
    article_c = Article.objects.all()
    context = {
        'article': article,
        'categories': categories,
        'article-c': article_c
    }
    return render(request, template, context)


def article_detail(request, category_slug, article_slug):
    template = 'article/article.html'
    category = Category.objects.filter(slug=category_slug)
    article = get_object_or_404(Article, slug=article_slug)

    context = {
        'article': article,
        'category': category,
    }
    return render(request, template, context)
