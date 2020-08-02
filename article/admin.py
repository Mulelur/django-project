from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)

