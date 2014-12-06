from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index (request):
    """Home page!"""
    return HttpResponse ("Hello, world, you are at the polls.")

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
