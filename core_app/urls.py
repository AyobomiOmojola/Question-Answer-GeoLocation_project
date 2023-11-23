from django.urls import path
from . import views

urlpatterns = [
    path("postquestion", views.CreateQuestion.as_view(), name="postquestion"),
    path("answerquestion/<slug:question_slug>", views.AnswerQuestion.as_view(), name="answerquestion"),
    path("upvoteanswer/<int:answer_pk>", views.UpvoteAnswer.as_view(), name="upvoteanswer"),
]