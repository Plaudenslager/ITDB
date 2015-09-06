from django.contrib import admin

from .models import Theater, Play, People, Production, Cast, Crew, Musician, Musical_Numbers
# Register your models here.

admin.site.register(Theater)
admin.site.register(Play)
admin.site.register(People)
admin.site.register(Production)
admin.site.register(Cast)
admin.site.register(Crew)
admin.site.register(Musician)
admin.site.register(Musical_Numbers)
# admin.site.register(Theater_pictures)

