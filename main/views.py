from django.shortcuts import render, redirect
from haversine import haversine
from .models import Traveler, Question, Choice, Survey
import sys, json

def index(request):
    travelers = Traveler.objects.all()
    count = 0
    
    for traveler in travelers:
        count += traveler.count
    
    context = {
        'travelers' : travelers,
        'count' : count
    }
    
    return render(request, 'index.html', context=context)

def form(request):
    questions = Question.objects.all()
    context = {
        'questions' : questions
    }
    
    return render(request, 'form.html', context=context)

def submit(request):
    # 문항 수
    N = Question.objects.count()
    # 여행자 유형 수
    travelers = Traveler.objects.all()
    # 성격 유형
    person = ''
    
    counter = {'E': 0, 'I': 0, 'B': 0, 'R': 0, 'P': 0, 'J':0}
    
    print(f'POST: {request.POST}')

    for n in range(1, N+1):
        category = request.POST[f'question-{n}'][0]
        counter[category] += 1
        
    # 최고점 여행자 유형
    for c in counter.keys():
        if counter[c] >= 2:
            person += c

    for traveler in travelers:
        if traveler.data["personality"] == person:
            best_traveler = traveler
    best_traveler.count += 1
    best_traveler.save()

    context = {
        'traveler' : best_traveler,
        'counter' : counter
    }
    print(context)
    # print(best_traveler.pk)
    return redirect(f'/result/{best_traveler.pk}')


def result(request, traveler_id):
    traveler = Traveler.objects.get(pk=traveler_id)
    context = {
        'traveler' : traveler,
    }
    
    return render(request, 'result.html', context=context)


def search(request):
    places = {
        'start': [34.5709, 126.6079],
        '전망대': [34.2961, 126.5246],
        '미황사': [34.3829, 126.5774],
        '대흥사': [34.4764, 126.6168],
        '해창주조장': [34.5177, 126.5386],
        '해남공룡박물관': [34.5897, 126.4375]
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
        'routes': routes,
        'route_js': json.dumps(routes)
    }
    """
    routes = {
               'start': {'sequence': 1, 
                          'lat': 34.5709, 
                          'lng': 126.6079}, 
                '해남공룡박물관': {'sequence': 2, 
                                 'lat': 34.5897, 
                                 'lng': 126.4375},
                '해창주조장': {'sequence': 3, 
                             'lat': 34.5177,
                             'lng': 126.5386 },
                '대흥사': {'sequence': 4, 
                          'lat': 34.4764, 
                          'lng': 126.6168}, 
                '미흥사': {'sequence': 5, 
                          'lat': 34.3829, 
                          'lng': 126.5774}, 
                '전망대': {'sequence': 6, 
                          'lat': 34.2961, 
                          'lng': 126.5246}
            }
    """
    return render(request, 'search.html', context=context)
    print(context)


def types(request):
    traveler = Traveler.objects.all()
    context = {
        'traveler' : traveler,
    }
    return render(request, 'types.html', context=context)
<<<<<<< HEAD

def survey(request):
    return render(request, 'survey.html')
=======
>>>>>>> 109429f62d0aeb9370b3793cce0fc832e448b2a6
