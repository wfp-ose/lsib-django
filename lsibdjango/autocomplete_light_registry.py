import autocomplete_light.shortcuts as autocomplete_light

from lsibdjango.models import GeographicThesaurusEntry

class GeographicThesaurusAutocomplete(autocomplete_light.AutocompleteGenericBase):
    search_fields=['^dos_short']
    model=GeographicThesaurusEntry
    attrs={
        'placeholder': 'Other model name ?',
        'data-autocomplete-minimum-characters': 1
    }
    widget_attrs={
        'data-widget-maximum-values': 4,
        'class': 'modern-style'
    }
autocomplete_light.register(GeographicThesaurusAutocomplete)
