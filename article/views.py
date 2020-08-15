from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.db.models import Q


def article_list(request, category_slug):
    template = 'article/article.html'
    categories = get_object_or_404(Category, slug=category_slug)
    category = Category.objects.all()[:5]
    article = Article.objects.filter(category=categories)
    context = {
        'article': article,
        'categories': categories,
        'category': category
    }
    return render(request, template, context)


def article_detail(request, category_slug, article_slug):
    template = 'article/article_detail.html'
    categories = Category.objects.get(slug=category_slug)
    article = get_object_or_404(Article, slug=article_slug)
    categorys = Category.objects.all()[:5]
    next_article = Article.objects.exclude(slug=article_slug)[0]

    context = {
        'article': article,
        'category': categorys,
        'categories':categories,
        'next_article': next_article
    }
    return render(request, template, context)

def search(request):
    query = request.GET.get('q')
    if query:
        results = Article.objects.filter(Q(title__icontains=query) | Q(text__icontains=query) | Q(slug__icontains=query))
    else:
        results = Article.objects.all()

    Qs = request.GET.get('page')
    paginator = Paginator(results, 10) # Show 10 contacts per page.
    page_obj = paginator.get_page(Qs)
    return render(request, 'article/article_search.html', {'page_obj': page_obj, 'query': query})

# def search(request):
#     query = request.GET.get('q')
#     if query:
#         results = Article.objects.filter(Q(title__icontains=query) | Q(text__icontains=query) | Q(slug__icontains=query))
#         paginator = Paginator(results, 1) 
#         page_obj = paginator.get_page('page')
#         return render(request, 'article/article_search.html', {'page_obj': page_obj, 'query': query, 'results': results})
#     else:
#         results = Article.objects.all()
#         paginator = Paginator(results, 1) 
#         query = request.GET.get('page')

#     page_obj = paginator.get_page(query)
#     return render(request, 'article/article_search.html', {'page_obj': page_obj})