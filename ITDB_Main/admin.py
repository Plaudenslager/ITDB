from django.contrib import admin

from .models import Theater, Play, People, Production, Cast, Crew, Musician, Musical_Number, Production_Company
# Register your models here.


class CastInline(admin.StackedInline):
    fieldsets = [
        (None,                  {'fields': (('character', 'person'),)}),
        ('Optional Details',    {'fields': ('billed_as', ('is_understudy', 'is_alternating'), ('start_year', 'end_year')),
                                 'classes': ('collapse')}
         )
    ]
    model = Cast
    extra = 1

class ProductionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ('play', 'theater', ('start_date', 'end_date'))}),
        ('Details', {'fields': ('prod_company', 'notes'),
                     'classes': ('collapse',)}
         ),
    ]
    inlines = [CastInline]
    list_display = ('play', 'theater', 'start_date')




admin.site.register(Theater)
admin.site.register(Play)
admin.site.register(People)
admin.site.register(Production, ProductionAdmin)
# admin.site.register(Cast)
admin.site.register(Crew)
admin.site.register(Musician)
admin.site.register(Musical_Number)
admin.site.register(Production_Company)

# admin.site.register(Theater_pictures)

