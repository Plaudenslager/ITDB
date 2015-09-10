from django.contrib import admin

from .models import Theater, Play, People, Production, Cast, Crew, Musician, Musical_Number, Production_Company
# Register your models here.

class ProductionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ('play', 'theater', ('start_date', 'end_date'))}),
        ('Details', {'fields': ('prod_company', 'notes'),
                     'classes': ('collapse',)}
         ),
    ]

admin.site.register(Theater)
admin.site.register(Play)
admin.site.register(People)
admin.site.register(Production, ProductionAdmin)
admin.site.register(Cast)
admin.site.register(Crew)
admin.site.register(Musician)
admin.site.register(Musical_Number)
admin.site.register(Production_Company)

# admin.site.register(Theater_pictures)

