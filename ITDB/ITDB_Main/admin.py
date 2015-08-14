from django.contrib import admin

from .models import Theater, Play, People, Production, Cast

admin.site.register(Theater)
admin.site.register(Play)
admin.site.register(People)
admin.site.register(Production)
admin.site.register(Cast)

# Register your models here.

