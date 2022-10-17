# -*- coding: utf-8 -*-
from django.shortcuts import render
from cells.models import series, pack, evaluation
from django.http import JsonResponse
# functions
def getSeriesData(data):
    paralels = series.objects.all()
    for s in paralels:
        packs = pack.objects.filter(series=s)
        data['series'][s.number] = 0
        for elemnt in packs:
            if not elemnt.retiret:
                capacyti = evaluation.objects.filter(pack_id=elemnt).last().capacyti
                data['series'][s.number] += capacyti


# views here.
def series_capacyti(request):
    data = {'series': {}, 'grafNames': [], 'grafValues': []}
    getSeriesData(data)
    for k, v in data['series'].items():
        data['grafNames'].append(("S"+str(k)))
        data['grafValues'].append(v)
    return render(request=request, template_name='dashboard.html', context=data)

def series_capacyti_json(request):
    data = {'series': {}}
    getSeriesData(data)
    return JsonResponse(data)

