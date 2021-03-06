from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    tempalte = loader.get_template('polls/index.html')
    context = RequestContext(request, \
        { 'latest_question_list': latest_question_list, })
    return HttpResponse(tempalte.render(context))
    #return HttpResponse("Hello, world. You're at the poll index.)

def detail(request, question_id):
    quesiton = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'quesiton': quesiton})
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the result of the question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
