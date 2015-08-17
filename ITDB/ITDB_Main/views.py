from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import Theater

# Default first page.  Should be the search page.
def index(request):
    return HttpResponse("Hello, world. You're at the ITDB_Main index.  This is where you will be able to search.")

# page for Theaters & theater details.  Will show the details about a theater, and a list of Productions.
def theaters(request):
    all_theaters_by_alpha = Theater.objects.order_by('name')
    context = RequestContext(request, {'all_theaters_by_alpha': all_theaters_by_alpha})
    return render(request, 'ITDB_Main/theaters.html',context)

def theater_detail(request, theater_id):
    try:
        theater = Theater.objects.get(pk=theater_id)
    except Theater.DoesNotExist:
        raise Http404("Theater does not exist")

    return render(request, 'ITDB_Main/theater_detail.html', {'theater' : theater})

# page for People
def person(request):
    return HttpResponse("Page showing a single person - e.g. actor, director, writer, followed by a list of Productions")

# page for Plays
def play(request):
    return HttpResponse("Page showing a single play, followed by a list of Productions")

# page for Productions
def production(request):
    return HttpResponse("Page showing a single production, with details about theater and play, followed by a list of People")