from turtle import update
from django.contrib import admin
from .models import Post, Tag

from .models import *

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'update_on')
    list_filter = ('tags', 'created_on', 'updated_on')
    search_fields = ('title')
    prepopulated_fields = {'slug': ('title', )}  # this create the slug field from the title field
    autocomplete_fields = ('tags', )

# Register your models here.
admin.site.register(Post, PostAdmin)
# admin.site.register(Comment)

# TagAdmin must define "search_fields", because it's referenced by PostAdmin.autocomplete_fields.
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name', )

admin.site.register(Tag, TagAdmin)