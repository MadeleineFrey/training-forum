from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Question
from .forms import CommentForm, QuestionForm
from django.contrib.auth.models import User


class QuestionList(generic.ListView):
    """
    X
    """

    model = Question
    queryset = Question.objects.filter(status=1).order_by('-created_on')
    template_name = 'questions.html'
    paginate_by = 6


class HomePage(View):
    """
    x
    """

    def get(self, request):
        """
        x
        """

        return render(
            request,
            'index.html'
            )


class FullQuestion(View):
    """
    x
    """
    def get(self, request, id, *args, **kwargs):
        """
        x
        """

        queryset = Question.objects.filter(status=1)
        question = get_object_or_404(queryset, id=id)
        comments = question.comments.order_by('created_on')
        liked = False
        if question.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'full_question.html',
            {
                'question': question,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            }
        )

    def post(self, request, id, *args, **kwargs):
        """
        x
        """

        queryset = Question.objects.filter(status=1)
        question = get_object_or_404(queryset, id=id)
        comments = question.comments.order_by('created_on')
        if question.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.username = request.user
            comment = comment_form.save(commit=False)
            comment.question = question
            comment.save()

        else:
            comment_form = CommentForm()

        return render(
            request,
            'full_question.html',
            {
                'question': question,
                'comments': comments,
                'commented': True,
                'comment_form': CommentForm()
            }
        )


class QuestionLike(View):
    """
    X
    """

    def post(self, request, id, *args, **kwargs):
        """
        X
        """

        question = get_object_or_404(Question, id=id)
        if question.likes.filter(id=self.request.user.id).exists():
            question.likes.remove(request.user)
        else:
            question.likes.add(request.user)

        return HttpResponseRedirect(reverse('full_question', args=[id]))


class UserProfile(View):
    """
    X
    """

    def get(self, request, *args, **kwargs):
        """
        X
        """
        if request.user.is_superuser:
            mquestions = Question.objects.filter(status=1) \
                 .order_by('-created_on')
        else:
            mquestions = Question.objects.filter(author=self.request.user) \
                .filter(status=1).order_by('-created_on')

        return render(
            request,
            'user_profile.html',
            {
                'mquestions': mquestions
            }
        )


class AddQuestion(View):
    """
    x
    """
    def get(self, request, *args, **kwargs):
        """
        x
        """
        return render(
            request,
            'add_question.html',
            {
                'question_form': QuestionForm()
            }
        )

    def post(self, request, *args, **kwargs):
        """
        x
        """

        question_form = QuestionForm(data=request.POST)

        if question_form.is_valid():
            question_form.instance.author = request.user
            ques = question_form.save(commit=False)
            ques.save()

        else:

            question_form = QuestionForm()

        return redirect('/user_profile')


class EditQuestion(View):
    """
    X
    """

    def get(self, request, id, *args, **kwargs):
        """
        x
        """
        queryset = Question.objects.filter(status=1)
        rest = get_object_or_404(queryset, id=id)
        editform = QuestionForm(instance=rest)

        return render(
            request,
            'edit_question.html',
            {
                'editform': editform,
                'edit_question_form': QuestionForm(instance=rest)
            }
        )

    def post(self, request, id, *args, **kwargs):
        """
        x
        """
        queryset = Question.objects.filter(status=1)
        rest = get_object_or_404(queryset, id=id)
        edit_question_form = QuestionForm(data=request.POST, instance=rest)
        if request.user.is_superuser:

            queryset = Question.objects.filter(status=1)
            rest = get_object_or_404(queryset, id=id)

            if edit_question_form.is_valid():
                wfraga = edit_question_form.save(commit=False)
                wfraga.save()
            else:
                edit_question_form = QuestionForm()

        else:
            queryset = Question.objects.filter(status=1)
            rest = get_object_or_404(queryset, author=request.user, id=id)

            if edit_question_form.is_valid():

                edit_question_form.instance.author = request.user
                eques = edit_question_form.save(commit=False)
                eques.save()

            else:
                edit_question_form = QuestionForm()

        return redirect('/user_profile')


def delete_question(request, id):
    """
    X
    """
    if request.user.is_superuser:
        item = get_object_or_404(Question, id=id)
    else:
        item = get_object_or_404(Question, id=id, author=request.user)

    item.delete()

    return redirect('/user_profile')
