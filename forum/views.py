from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Question
from .forms import CommentForm


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

        


