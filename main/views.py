from django.shortcuts import render
from .models import Traveler, Question, Choice, Spot, Survey

def index(request):
    travelers = Traveler.objects.all()
    
    context = {
        'travelers' : travelers,
    }
    
    return render(request, 'index.html', context=context)

def form(request):
    questions = Question.objects.all()
    
    context = {
        'questions' : questions,
    }
    
    return render(request, 'form.html', context=context)

def result(request):
    # 문항 수
    N = Question.objects.count()
    # 여행자 유형 수
    K = Traveler.objects.count()
    # 성격 유형
    person = ''
    
    print(f'문항 수: {N}, 여행자 유형 수: {K}')
    
    counter = {'E': 0, 'I': 0, 'B': 0, 'R': 0, 'P': 0, 'J':0}
    
    print(f'POST: {request.POST}')
    
    
    for n in range(1, N+1):
        category = request.POST[f'question-{n}'][0]
        counter[category] += 1
        
    # 최고점 여행자 유형
    for c in counter.keys():
        if counter[c] >= 2:
            person += c
    best_traveler = Traveler.objects.get(personality=person)
    best_traveler.count += 1
    best_traveler.save()
    
    context = {
        'traveler' : best_traveler,
        'counter' : counter
    }
    
    return render(request, 'result.html', context=context)