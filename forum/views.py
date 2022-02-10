from django.shortcuts import render
from django.views import generic, View
from .models import Question


class QuestionList(generic.ListView):
    """ X """

    model = Question
    queryset = Question.objects.filter(status=1).order_by('-created_on')
    template_name = 'questions.html'
    paginate_by = 6


class HomePage(View):
    """
    x
    """

    def get(self, request):
        return render(
            request,
            'index.html'
            )