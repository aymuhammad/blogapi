from pyexpat import model
from turtle import title
from unicodedata import category
from django.db import models
from django.utils import timezone

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