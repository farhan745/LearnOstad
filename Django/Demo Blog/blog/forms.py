from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','author', 'category', 'tag']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control comment-box',
                'placeholder': 'Leave a comment...',
                'style': (
                    'width: 100%; '
                    'height: 180px; '
                    'border-radius: 12px; '
                    'border: 1px solid #ddd; '
                    'box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); '
                    'padding: 20px; '
                    'font-size: 16px; '
                    'line-height: 1.6; '
                    'resize: vertical; '
                    'background-color: #ffffff; '
                    'color: #333; '
                ),
            }),
        }