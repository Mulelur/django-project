from django.shortcuts import render

def projects(request):

    template = 'projects/project.html'

    context = {}
    return render(request, template, context)
