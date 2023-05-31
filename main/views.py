from django.shortcuts import render, redirect
from haversine import haversine
from .models import Traveler, Question, Choice, Survey
import sys, json


def index(request):
    survey = Survey.objects.get(pk=1)
    
    if request.method == 'POST':
        accuracy, satisfaction, influence = request.POST['accuracy'], request.POST['satisfaction'], request.POST['influence']
        survey.accuracy += int(accuracy)
        survey.satisfaction += int(satisfaction)
        survey.influence += int(influence)
        survey.save()
        
    travelers = Traveler.objects.all()
    
    context = {
        'travelers' : travelers,
        'count' : survey.count
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
    survey = Survey.objects.get(pk=1)
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
    survey.count += 1
    survey.save()
    
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
        'traveler_id' : traveler_id,
    }

    return render(request, 'result.html', context=context)

def results(request, traveler_id):
    traveler = Traveler.objects.get(pk=traveler_id)
    context = {
        'traveler' : traveler,
        'traveler_id' : traveler_id,
    }

    return render(request, 'results.html', context=context)


def search(request):
    if request.method == 'POST':
        selected_spots = request.POST.getlist('selected_spot')

    selected_spot = [
        spot.replace('[', '').replace(']', '').split(', ')
        for spot in selected_spots
    ]

    places = {
        spot[2]: list(map(float, [spot[3], spot[4]]))
        for spot in selected_spot
    }

    places['start'] = list(map(float, selected_spot[0][:2]))# 시작 지점 수정 필요
    print(places)
    
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
        'route_js': json.dumps(routes),
        'selected_spots': selected_spots,
    }
    return render(request, 'search.html', context=context)


def types(request):
    traveler = Traveler.objects.all()
    context = {
        'traveler': traveler,
    }
    return render(request, 'types.html', context=context)


def survey(request):
    return render(request, 'survey.html')