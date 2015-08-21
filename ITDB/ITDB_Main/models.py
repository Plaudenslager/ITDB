from django.db import models

# Create your models here.
class Theater(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=40)
    state_or_province = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50)
    def __unicode__(self):
        return "{0}: {1}, {2}".format(self.name, self.city, self.state_or_province)

class Play(models.Model):
    title = models.CharField(max_length=100)
    year_written = models.IntegerField(blank=True)
    synopsis = models.TextField(blank=True)
    def __unicode__(self):
        return "{0} ({1})".format(self.title, self.year_written)

class People(models.Model):
    name = models.CharField(max_length=40)
    short_bio = models.TextField(blank=True)
    def __unicode__(self):
        return self.name

# A production is defined as a Play that ran at a particular Theater between given Dates
class Production(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    production_company = models.CharField(max_length=100)
    play = models.ForeignKey(Play)
    theater = models.ForeignKey(Theater)
    notes = models.TextField(blank=True)
    def __unicode__(self):
        return "{0} at {1} ({2}) from {3} to {4}".format(self.play.title, self.theater.name, self.theater.city, self.start_date, self.end_date)

# A cast is defined as the list of People playing characters in a particular Production
class Cast(models.Model):
    person = models.ForeignKey(People)
    character = models.CharField(max_length=40)
    production = models.ForeignKey(Production)
    billed_as = models.CharField(max_length = 40, blank=True)

# A crew is defined as the list of off-stage People working on a particular Production
class Crew(models.Model):
    person = models.ForeignKey(People)
    job = models.CharField(max_length=40)
    production = models.ForeignKey(Production)
    is_director = models.BooleanField(default=False)
    is_writer = models.BooleanField(default=False)
    is_producer = models.BooleanField(default=False)

#TODO: Add class for production companies