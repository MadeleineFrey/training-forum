from django.contrib import admin
from .models import Question, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Question)
class QuestionAdmin(SummernoteModelAdmin):
    """ X """

    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    # prepopulated_fields = {'': ('title',)}
    summernote_fields = ('body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ X """
    list_display = ('username', 'message', 'question', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    # username_username???????
    search_fields = ('username_username', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)