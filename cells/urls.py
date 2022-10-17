from django.urls import path

from . import views

urlpatterns = [
    path('json', views.series_capacyti_json, name='capacity'),
    path('', views.series_capacyti, name='capacity'),
]