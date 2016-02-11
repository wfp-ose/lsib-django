from django.db import models

class GeographicThesaurusEntry(models.Model):
    """
    Model for LSIB Geographic Thesaurus, which provides a codex for cross-walking
    fips, iso, gaul, etc.
    """
    id = models.IntegerField(unique=True, db_index=True, primary_key=True)
    fips = models.CharField(max_length=2, null=True, blank=True)
    iso_alpha2 = models.CharField(max_length=2, null=True, blank=True)
    iso_alpha3 = models.CharField(max_length=3, null=True, blank=True)
    iso_num = models.IntegerField(null=True, blank=True)
    stanag = models.CharField(max_length=3, null=True, blank=True)
    tld = models.CharField(max_length=3, null=True, blank=True)
    gaul = models.IntegerField(null=True, blank=True)
    dos_short_extended = models.CharField(max_length=255, null=True, blank=True)
    dos_short = models.CharField(max_length=255, null=True, blank=True)
    dos_long = models.CharField(max_length=255, null=True, blank=True)
    capital = models.CharField(max_length=255, null=True, blank=True)
    sovereignty = models.NullBooleanField()
    independent_state = models.NullBooleanField()
    un = models.NullBooleanField()
    relations = models.CharField(max_length=255, null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "%s" % self.dos_short.encode('utf-8')

    class Meta:
        ordering = ("id",)
        verbose_name = 'LSIB Geographic Thesaurus Entry'
        verbose_name_plural = 'LSIB Geographic Thesaurus'
