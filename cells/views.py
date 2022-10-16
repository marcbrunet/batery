from django.shortcuts import render
from cells.models import series, pack
# Create your views here.
from django.http import JsonResponse


def series_capacyti(request):
    paralels = series.objects.all()
    data = {'series': {}}
    for s in paralels:
        packs = pack.objects.filter(series=s)
        capacyti = 0
        for elemnt in packs:
            capacyti += elemnt.capacity
        data['series'][s.number] = capacyti
    return JsonResponse(data)
