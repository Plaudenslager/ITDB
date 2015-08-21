from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from .models import Theater, Play, People, Production

# Default first page.  Should be the search page.
def index(request):
    return render(request, 'ITDB_Main/index.html')

# page for Theaters & theater details.  Will show the details about a theater, and a list of Productions.
# TODO: Add ability to group by city
# TODO: Add index to jump to particular starting letter
# TODO: Add ability to jump to city
# TODO: Add images of theaters
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

def person_detail(request, person_id):

    person = get_object_or_404(People, pk=person_id)

    return render(request, 'ITDB_Main/person_detail.html', {'person' : person})

# page for Plays
def plays(request):
    all_plays_by_alpha = Play.objects.order_by('title')
    context = RequestContext(request, {'all_plays_by_alpha': all_plays_by_alpha})
    return render(request, 'ITDB_Main/plays.html',context)

def play_detail(request, play_id):

    play = get_object_or_404(Play, pk=play_id)

    return render(request, 'ITDB_Main/play_detail.html', {'play' : play})

# page for Productions
def productions(request):
    all_productions_by_date = Production.objects.order_by('-start_date')
    context = RequestContext(request, {'all_productions_by_date': all_productions_by_date})
    return render(request, 'ITDB_Main/productions.html',context)

def production_detail(request, production_id):

    production = get_object_or_404(Production, pk=production_id)

    return render(request, 'ITDB_Main/production_detail.html', {'production' : production})

#TODO: add view for production companies
#TODO: add a search field to the index.html page (maybe to every page?)