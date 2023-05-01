from django.shortcuts import render
from .models import Result, Question, Choice, Spot, Survey

def index(request):
    results = Result.objects.all()
    
    context = {
        'results' : results,
    }
    
    return render(request, 'index.html', context=context)

def form(request):
    questions = Question.objects.all()
    
    context = {
        'questions' : questions,
    }
    
    return render(request, 'form.html', context=context)