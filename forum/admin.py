from django.contrib import admin
from .models import Question
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Question)
class QuestionAdmin(SummernoteModelAdmin):

    summernote_fields = ('body')

