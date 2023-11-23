from rest_framework.decorators import APIView 
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSerializer, AnswersSerializer, UpvoteSerializer
from .models import Questions, Answers, UpvoteAnswers

# Create your views here.
class CreateQuestion(APIView):
    def post(self, request:Request):
        data = request.data
        serializers = QuestionSerializer(data=data)

        if serializers.is_valid():
            serializers.save(user = self.request.user)

            response = {
                "MESSAGE":"Question Created!!!",
                "YOUR_QUESTION":serializers.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def get(self, request:Request):
        all_questions = Questions.objects.all()
        serializer = QuestionSerializer(instance=all_questions, many=True)
        response = {
            "MESSAGE": "THESE ARE THE LIST OF ALL QUESTIONS",
            "QUESTIONS": serializer.data
        }
        return Response(data = response, status = status.HTTP_200_OK)


class AnswerQuestion(APIView):
    def post(self, request:Request, question_slug):
        questions = Questions.objects.get(slug=question_slug)
        data = request.data
        serializers = AnswersSerializer(data=data)

        if serializers.is_valid():
            serializers.save(user=self.request.user, question=questions)

            response = {
                "MESSAGE":"YOU HAVE ANSWERED THIS QUESTION!!!",
                "YOUR_ANSWER":serializers.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class UpvoteAnswer(APIView):
    def get(self, request:Request, answer_pk):
        answers = Answers.objects.get(pk = answer_pk)
        upvote = UpvoteAnswers(answer = answers)
        upvote.save()
        upvote.voter.add(request.user)
        uppvote = UpvoteAnswers.objects.get(answer=answers)
        serializer = UpvoteSerializer(instance=uppvote)

        response = {
                    'MESSAGE': 'You just voted for this question',
                    'VOTE':serializer.data
                }

        return Response(data = response, status = status.HTTP_200_OK )


