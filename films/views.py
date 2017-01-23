from django.shortcuts import render
from django.http import HttpResponse
from . models import Films
from django.template import loader, RequestContext

def index(request):
    newest_films = Films.objects.order_by('added_date')[:5]
    #output = ", ".join(q.name for q in newest_films)
    return render(request, 'films/index.html', {'newest_films': newest_films})


def detail(request, film_id):
    film_des = Films.objects.get(pk=film_id)
    return render(request, 'films/detail.html', {'film_des': film_des})