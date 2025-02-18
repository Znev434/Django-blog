from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Wybieramy pola, które będą w formularzu

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']  # Pokażemy tylko te pola w formularzu