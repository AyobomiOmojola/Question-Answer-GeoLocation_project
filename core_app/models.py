from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asker')
    slug = models.SlugField(max_length=264, unique=True, default=uuid.uuid1)
    question_field = models.CharField(max_length=264, blank=False)

class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_user')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_answer')
    answer_field = models.TextField(default=False)

class UpvoteAnswers(models.Model):
    answer = models.OneToOneField(Answers, on_delete=models.CASCADE, related_name='upvote_answer')
    voter = models.ManyToManyField(User, related_name='upvoter')
    date_added = models.DateTimeField(auto_now_add=True, )


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

