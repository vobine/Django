from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Question, Choice


# Create your views here.
class IndexView (generic.ListView):
    """Home page!"""
    template_name = 'polls/index.html'
    context_object_name = 'qList'

    def get_queryset (self):
        """Return the last five published questions."""
        return Question.objects.order_by ('-pub_date')[:5]

class DetailView (generic.DetailView):
    """Show one question in detail."""
    model = Question
    template_name = 'polls/detail.html'

class ResultsView (generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

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
