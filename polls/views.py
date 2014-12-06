from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from polls.models import Question

# Create your views here.
def index (request):
    """Home page!"""
    qList = Question.objects.order_by ('-pub_date')[:5]
    context = {'qList': qList, }
    return render (request, "polls/index.html", context)

def detail (request, question_id):
    """Show one question in detail."""
    question = get_object_or_404 (Question, pk=question_id)
    return render (request,
                   'polls/detail.html',
                   {'question': question, } )

def results (request, question_id):
    return HttpResponse (
        "You are looking at the results of question {0:s}.".format (
            question_id))

def vote (request, question_id):
    return HttpResponse (
        "You are voting on question {0:s}.".format (
            question_id))
