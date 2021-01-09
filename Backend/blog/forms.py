from django import forms

from .models import Category, Post


# Post form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'status']

