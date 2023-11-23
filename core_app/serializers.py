from rest_framework import serializers
from .models import  Questions, Answers, UpvoteAnswers, Comments

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['user','question_field','slug']
        extra_kwargs = {
        "user" : {
            "read_only" : True,
        },
        "slug" : {
            "read_only" : True,
        }
    }


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['user','answer_field']
        extra_kwargs = {
        "user" : {
            "read_only" : True,
        }
    }

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpvoteAnswers
        fields = ['answer','voter']
        extra_kwargs = {
        "answer" : {
            "read_only" : True,
        },
        "voter" : {
            "read_only" : True,
        }
    }

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['user','comment']