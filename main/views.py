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

def result(request):
    # 문항 수
    N = Question.objects.count()
    # 여행자 유형 수
    K = Traveler.objects.count()
    
    print(f'문항 수: {N}, 여행자 유형 수: {K}')
    
    counter = [0] * (K+1)
    
    print(f'POST: {request.POST}')
    
    for n in range(1, N+1):
        traveler_id = int(request.POST[f'question-{n}'][0])
        counter[traveler_id] += 1
        
    # 최고점 여행자 유형
    best_traveler_cnt = max(range(1, K+1), key=lambda id : counter[id])
    best_traveler = Traveler.objects.get(pk=best_traveler_cnt)
    best_traveler.count += 1
    best_traveler.save()
    
    context = {
        'traveler' : best_traveler,
        'counter' : counter
    }
    
    return render(request, 'result.html', context)