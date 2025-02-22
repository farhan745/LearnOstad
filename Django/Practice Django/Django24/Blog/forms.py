from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tag']  # Add 'category' and 'tag' fields to the form
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] 
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your comment here...',
                'rows': 4,
                'style': 'resize:none; border-radius:10px;'
            }),
        }