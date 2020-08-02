from django.shortcuts import render
from article.views import Category, Article

def support(request):
    template = 'help/help.html'

    category = Category.objects.all()
    article  = Article.objects.all()
    context = {'categories': category, 'article': article}
    return render(request, template, context)

def faqs(request):
    template = 'help/faqs.html'

    category = Category.objects.all()
    context = {'categories': category}
    return render(request, template, context)