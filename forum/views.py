from django.shortcuts import render
from django.views import generic
from .models import Question


class QuestionList(generic.ListView):
    "" X ""

    model = Question
    queryset = Question.objects.filter(ststus=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6