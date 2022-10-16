from django.urls import path

from . import views

urlpatterns = [
    path('', views.series_capacyti, name='capacity'),
]