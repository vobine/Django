from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Question

# Create your views here.
def index (request):
    """Home page!"""
    qList = Question.objects.order_by ('-pub_date')[:5]
    template = loader.get_template ("polls/index.html")
    context = RequestContext (request,
                              {'qList': qList,} )
    return HttpResponse (template.render (context))

def detail (request, question_id):
    return HttpResponse (
        "You are looking at question {0:s}.".format (
            question_id))

def results (request, question_id):
    return HttpResponse (
        "You are looking at the results of question {0:s}.".format (
            question_id))

def vote (request, question_id):
    return HttpResponse (
        "You are voting on question {0:s}.".format (
            question_id))
