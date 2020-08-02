from django.shortcuts import render

def profilesView(request):
    template = 'profiles/profile.html'

    context = {}
    
    return render(request, template, context)



def dashboardView(request):
    pass
