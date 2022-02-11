from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('questions/', views.QuestionList.as_view(), name='question'),
    path('<slug:slug>/', views.FullQuestion.as_view(), name='full_question'),
]