from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list,}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def result(request, question_id):
    response = "You are looking at the results of %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are Voting for %s." % question_id)