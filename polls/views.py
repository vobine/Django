from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from polls.models import Question, Choice


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
    question = get_object_or_404 (Question, pk=question_id)
    return render (request,
                   'polls/results.html',
                   { 'question' : question, } )

def vote (request, question_id):
    p = get_object_or_404 (Question, pk=question_id)
    try:
        selected = p.choice_set.get (pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render (request,
                       'polls/detail.html',
                       { 'question' : p,
                         'error_message': 'You didn\'t select a choice.',
                     } )
    else:
        selected.votes += 1
        selected.save ()
        return HttpResponseRedirect (reverse ('polls:results',
                                              args=(p.id, )))
