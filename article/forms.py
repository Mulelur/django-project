from django.forms import ModelForm
from .models import Article

class FeedBackGoodModelForm(ModelForm):
    class Meta:
        model = Article
        fields = 'good',

class FeedBackFairModelForm(ModelForm):
    class Meta:
        model = Article
        fields = 'fair',

class FeedBackBadModelForm(ModelForm):
    class Meta:
        model = Article
        fields = 'bad',