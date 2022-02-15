from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
# from django.http import request
# from django.contrib import messages
from .models import Question
from .forms import CommentForm, QuestionForm
from django.contrib.auth.models import User


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
    def get(self, request, slug, *args, **kwargs):
        """
        x
        """

        queryset = Question.objects.filter(status=1)
        question = get_object_or_404(queryset, slug=slug)
        comments = question.comments.filter(approved=True).order_by('created_on')

        return render(
            request,
            'full_question.html',
            {
                'question': question,
                'comments': comments,
                'commented': False,
                'comment_form': CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        """
        x
        """

        queryset = Question.objects.filter(status=1)
        question = get_object_or_404(queryset, slug=slug)
        comments = question.comments.filter(approved=True).order_by('created_on')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # comment_form.instance.email = request.user.email
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



class UserProfile(View):
    """
    X
    """

    def get(self, request, *args, **kwargs):
        """
        X
        """
    
        mquestions = Question.objects.filter(author=self.request.user).filter(status=1).order_by('-created_on')
    
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
            fraga = question_form.save(commit=False)
            fraga.save()

        else:
            # print(' not saving ')
            question_form = QuestionForm()
            
        return render(
            request,
            'add_question.html',
            {
                'question_form': QuestionForm()
            }
        )    


    
class EditQuestion(View):
    """ 
    X
    """
    
    def get(self, request, slug, *args, **kwargs):
        """
        x
        """
        queryset = Question.objects.filter(status=1)
        rest = get_object_or_404(queryset, slug=slug)
        editform = QuestionForm(instance=rest)
        
        return render(
            request,
            'edit_question.html',
            {
                'editform': editform,
                'edit_question_form': QuestionForm(instance=rest)
            }        
        )


    def post(self, request, slug, *args, **kwargs):
        """
        x
        """
        queryset = Question.objects.filter(status=1)
        rest = get_object_or_404(queryset, slug=slug)
        edit_question_form = QuestionForm(data=request.POST, instance=rest)

        if edit_question_form.is_valid():
            edit_question_form.instance.author = request.user
            wfraga = edit_question_form.save(commit=False)
            wfraga.save()

        else:
            # print(' not saving ')
            edit_question_form = QuestionForm()
            
        # messages.success(request, 'Updated')
        return redirect('/user_profile')

# def delete_question(request, slug, *args, **kwargs):
  #   """ 
   #  X
    # """
    # queryset = Question.objects.filter(status=1)
    # tes = get_object_or_404(queryset, slug=slug)
    # tes.delete()
    # return redirect('/user_profile')

