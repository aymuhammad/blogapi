import imp
from statistics import mode
from django.db import models
from django.utils import timezone
from django.conf import settings

# from .forms import CommentForm

class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Post(models.Model):

    #adding categories for the post
    Category=(
        ('Web-Dev', 'Web-Dev'),
        ('Machine Leanring', 'Machine Learning'),
        ('Artificial Intelegent', 'Artificial Intelegent'),
        ('Cyber-Security', 'Cyber-Security')
    )

    category = models.CharField(max_length=160, null=True, choices=Category, default='Wev-Devs')
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

# to create a comment
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering =['created']