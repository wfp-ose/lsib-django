from django.contrib import admin

from lsibdjango.models import GeographicThesaurusEntry

class GeographicThesaurusEntryAdmin(admin.ModelAdmin):
    model = GeographicThesaurusEntry
    list_display_links = ('dos_short',)
    list_display = ('id', 'dos_short', 'fips', 'iso_alpha2', 'iso_alpha3',)

admin.site.register(GeographicThesaurusEntry, GeographicThesaurusEntryAdmin)
