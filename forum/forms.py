from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    X
    """
    class Meta:
        """
        X
        """
        model = Comment
        fields = ('message',)
