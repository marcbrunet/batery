from django.shortcuts import render
from cells.models import series, pack, evaluation
from django.http import JsonResponse
# Create your views here.


def series_capacyti(request):
    data = {'series': {}}
    paralels = series.objects.all()
    for s in paralels:
        packs = pack.objects.filter(series=s)
        data['series'][s.number] = 0
        for elemnt in packs:
            if not elemnt.retiret:
                capacyti = evaluation.objects.filter(pack_id=elemnt).last().capacyti
                data['series'][s.number] += capacyti
    return JsonResponse(data)
