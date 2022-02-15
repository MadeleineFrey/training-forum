from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('questions/', views.QuestionList.as_view(), name='question'),
    path('<int:id>/', views.FullQuestion.as_view(), name='full_question'),
    path('user_profile', login_required(views.UserProfile.as_view()), name='user_profile'),
    path('AddQuestion', login_required(views.AddQuestion.as_view()), name='addquestion'),
    path('edit/<int:id>/', login_required(views.EditQuestion.as_view()), name='edit_question'),
    # path('like/<int:id>', views.QuestionLike.as_view(), name='question_like'),
    path('edit/<int:id>/delete_question/', login_required(views.delete_question), name="delete_question")
]