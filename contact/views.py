from django.shortcuts import render

def contactView(request):
    return render(request, 'home/contact.html')