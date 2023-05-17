from django.shortcuts import render
from haversine import haversine
from .models import Traveler, Question, Choice, Spot, Survey
import sys, json

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
    print(context)
    return render(request, 'result.html', context=context)


def search(request):
    places = {
        'start': [35.2849, 129.0954],
        '해운대': [35.1587, 129.1604],
        '씨라이프': [35.1594 ,129.1610],
        '더베이': [35.1566, 129.152],
        '남포동': [35.0975, 129.0304],
        '센텀시티': [35.1708, 129.1287]
    }
    
    regions = list(places.keys())
    NUM = len(regions)
    regions.remove('start')
    departure = 'start'
    sequence = NUM - len(regions)
    distance = sys.maxsize
    lat, lng = places['start'][0], places['start'][1]
    routes = {'start': {'sequence': sequence,
                        'lat': str(lat), 
                        'lng': str(lng)}
    }

    while len(regions) != 0:       
        for region in regions:
            temp = haversine(places[departure],
                            places[region],
                            unit='km')
            if distance > temp:
                distance = temp
                ans = region
                
        departure = ans
        regions.remove(ans)
        sequence = NUM - len(regions)
        distance = sys.maxsize
        lat, lng = places[ans][0], places[ans][1]
        routes[ans] = {'sequence': sequence,
                       'lat': str(lat), 
                       'lng': str(lng)}
        
    context = {
        'routes' : routes,
        'route_js': json.dumps(routes)
    }
    print(context)
    return render(request, 'search.html', context=context)