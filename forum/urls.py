from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('questions/', views.QuestionList.as_view(), name='question'),
    path('<slug:slug>/', views.FullQuestion.as_view(), name='full_question'),
    path('mquestions', login_required(views.UserProfile.as_view()), name='user_profile'),
]