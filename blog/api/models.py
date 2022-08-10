from django.db import models
from django.utils import timezone
from .forms import CommentForm

class Post(models.Model):

    #adding categories for the post
    Category=(
        ('Web-Dev', 'Web-Dev'),
        ('Machine Leanring', 'Machine Learning'),
        ('Artificial Intelegent', 'Artificial Intelegent'),
        ('Cyber-Security', 'Cyber-Security')
    )

    category = models.CharField(max_length=160, null=True, choices=Category, default='Wev-Devs')
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


# to create a comment
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    # email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)