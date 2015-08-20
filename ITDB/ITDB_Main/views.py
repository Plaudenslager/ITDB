from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from .models import Theater, Play, People

# Default first page.  Should be the search page.
def index(request):
    return HttpResponse("Hello, world. You're at the ITDB_Main index.  This is where you will be able to search.")

# page for Theaters & theater details.  Will show the details about a theater, and a list of Productions.
def theaters(request):
    all_theaters_by_alpha = Theater.objects.order_by('name')
    context = RequestContext(request, {'all_theaters_by_alpha': all_theaters_by_alpha})
    return render(request, 'ITDB_Main/theaters.html',context)

def theater_detail(request, theater_id):

    theater = get_object_or_404(Theater, pk=theater_id)

    return render(request, 'ITDB_Main/theater_detail.html', {'theater' : theater})

# page for People
def people(request):
    all_people_by_alpha = People.objects.order_by('name')
    context = RequestContext(request, {'all_people_by_alpha': all_people_by_alpha})
    return render(request, 'ITDB_Main/people.html',context)
    #TODO: Fix people view so that names are sorted by last name, rather than full name

# page for Plays
def plays(request):
    all_plays_by_alpha = Play.objects.order_by('title')
    context = RequestContext(request, {'all_plays_by_alpha': all_plays_by_alpha})
    return render(request, 'ITDB_Main/plays.html',context)

def play_detail(request, play_id):

    play = get_object_or_404(Play, pk=play_id)

    return render(request, 'ITDB_Main/play_detail.html', {'play' : play})

# page for Productions
def production(request):
    return HttpResponse("Page showing a single production, with details about theater and play, followed by a list of People")

#TODO: add view for production companies