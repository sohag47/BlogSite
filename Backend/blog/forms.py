from django import forms

from .models import Category, Comments, Post


# Category form:
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

# Post form:
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'status']

# Comment form:
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'body')
