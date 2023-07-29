from django.urls import path
from .views import SignUpPage_view, LogInPage_view, QuoraPageView, AskQuestion, Questions, AnswerView, LikeView

urlpatterns = [

    path('', SignUpPage_view, name='signup'),
    path('login/', LogInPage_view, name='login'),
    path('quora_page/', QuoraPageView.as_view(), name='page'),
    path('askQuestion/', AskQuestion.as_view(), name='askQue'),
    path('question/<int:pk>', Questions.as_view(), name='question'),
    path('question/<int:pk>/Answer/', AnswerView.as_view(), name='answer'),
    path('like/<int:pk>', LikeView, name='like_post')

]