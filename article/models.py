from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField

class Category(models.Model):
    title = models.CharField(max_length=70)
    sub_title = models.CharField(max_length=200, blank=True, default='')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article_category')
    text = RichTextUploadingField(blank=True)
    date = models.DateTimeField(auto_now=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

class FAQsCategory(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):     
    title = models.CharField(max_length=100)
    category = models.ForeignKey(FAQsCategory, on_delete=models.CASCADE)
    text = RichTextUploadingField(blank=True)
    date = models.DateTimeField(auto_now=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title   








