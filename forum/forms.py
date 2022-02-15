from .models import Comment, Question
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


class QuestionForm(forms.ModelForm):
    """
    X
    """
    class Meta:
        """
        X
        """

        model = Question
        fields = [
            'title',
            'slug',
            'body',
            'answered',
            'status'
        ]


