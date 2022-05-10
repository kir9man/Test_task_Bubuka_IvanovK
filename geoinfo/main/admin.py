from django.contrib import admin

from .models import *


class CityinfoAdmin(admin.ModelAdmin):
    list_display = ('cont', 'city', 'country', 'population')
    list_display_links = ('city', )
    search_fields = ('city', )
    list_filter = ('cont', )


class ContinentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cont_name', 'slug_name', 'content')
    list_display_links = ('cont_name', )
    list_filter = ('cont_name', )


admin.site.register(Cityinfo, CityinfoAdmin)
admin.site.register(Continents, ContinentsAdmin)
