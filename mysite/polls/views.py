from django.shortcuts import HttpResponse, get_object_or_404, get_list_or_404
from . models import Question, Choice

def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    result = "<br>".join([q.question_text for q in latest_questions])
    return HttpResponse(result)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(f"You're looking at question {question_id}: {question.first()}")
    
def results(request, question_id):
    response = "You're looking at the results of %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question % s", question_id)