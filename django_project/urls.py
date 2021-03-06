from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    # path('account/', include('accounts.urls')),
    path('profile/', include('profiles.urls')),
    path('article/', include('article.urls')),
    path('help/', include('help.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('buy/', include('buy.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('payment/', include('payment.urls')),
    path('contact/', include('contact.urls')),
    path('accounts/', include('allauth.urls')),
    path('projects/', include('projects.urls')),
    path('payfast/', include('payfast.urls')),
]

if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)