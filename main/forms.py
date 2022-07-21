from django.forms import ModelForm
from main.models import Post, Comment 
from django.contrib.auth.models import User

class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment 
        fields = ['text']
