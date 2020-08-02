from django.shortcuts import render
from .models import Plan

def homeView(request):
    return render(request, 'home/index.html')

def pricingView(request):

    plan = Plan.objects.all()

    context = {
        'plan': plan
    }
    return render(request, 'home/pricing.html', context)    

def aboutView(request):
    return render(request, 'home/about.html')    


def serviceView(request):
    return render(request, 'home/service.html')        
