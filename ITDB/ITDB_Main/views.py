from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Theater

# Default first page.  Should be the search page.
def index(request):
    return HttpResponse("Hello, world. You're at the ITDB_Main index.")

# page for Theaters & theater details.  Will show the details about a theater, and a list of Productions.
def theaters(request):
    all_theaters_by_alpha = Theater.objects.order_by('name')
    template = loader.get_template("ITDB_Main/index.html")
    context = RequestContext(request, {'all_theaters_by_alpha': all_theaters_by_alpha})
    return HttpResponse(template.render(context))

def theater_detail(request, theater_id):
    return HttpResponse("You are looking at theater %s." %theater_id)

# page for People
def person(request):
    return HttpResponse("Page showing a single person - e.g. actor, director, writer, followed by a list of Productions")

# page for Plays
def play(request):
    return HttpResponse("Page showing a single play, followed by a list of Productions")

# page for Productions
def production(request):
    return HttpResponse("Page showing a single production, with details about theater and play, followed by a list of People")