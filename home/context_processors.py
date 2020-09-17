from .models import Logo
from django.conf import settings

def logo(request):
    try:
        logo = Logo.objects.get(id='1')
    except:
        logo = Logo.objects.all()

    free_try = settings.FREE_TRY
    site_name = settings.SITE_NAME
    # web_name = settings.WEB_SITE_NAME

    return {
        'free_try': free_try,
        'logo': logo,
        'site_name': site_name

    }