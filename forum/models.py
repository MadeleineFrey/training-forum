from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, 'Draft'), (1, 'Published'))


class Question(models.Model):
    """ X """
    title = models.CharField(max_length=150, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='user_questions')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(
         User, related_name='question_like', blank=True)

    class Meta:
        """
         X
        """
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title) if self.title else ''

    def number_of_likes(self):
        """
        X
        """
        return self.likes.count()


class Comment(models.Model):
    """
     X
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="user_comments")
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ X """
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.message} by {self.username}'
