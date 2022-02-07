from django.db import models
from django.contrib.auth.models import User
#from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Question(models.Model):
    ''' X '''
    title = models.CharField(max_length=150, unique=True)
    slug = models.CharField(max_length=150, unique=True)
    question = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="user_question")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    answerd = models.BooleanField(null=False, blank=False, default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ''' X '''
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title) if self.title else ''

