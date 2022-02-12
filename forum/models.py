from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, 'Draft'), (1, 'Published'))


class Question(models.Model):
    """ X """
    title = models.CharField(max_length=150, unique=True)
    slug = models.CharField(max_length=150, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='user_questions')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    answered = models.BooleanField(null=False, blank=False, default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """ X """
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title) if self.title else ''


class Comment(models.Model):
    """ X """
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                             related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="user_comments")
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ X """
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.message} by {self.username}'




    
