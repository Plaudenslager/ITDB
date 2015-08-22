from django.db import models
import datetime

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
        return self.title

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
    def display_year(self):
        start = self.start_date.year
        end = self.end_date.year
        if end == start:
            return "{0}".format(start)
        else:
            return "{0} - {1}".format(start, end)
    def __unicode__(self):
        return "{0} at The {1} ({2}) : {3}".format(self.play.title, self.theater.name, self.theater.city, self.start_date.year)

# A cast is defined as the list of People playing characters in a particular Production
class Cast(models.Model):
    person = models.ForeignKey(People)
    character = models.CharField(max_length=40)
    production = models.ForeignKey(Production)
    billed_as = models.CharField(max_length = 40, blank=True)
    def __unicode__(self):
        return "{0} in {1} at The {2} ({3}), played by {4}".format(self.character, self.production.play.title, self.production.theater.name, self.production.theater.city, self.person)

# A crew is defined as the list of off-stage People working on a particular Production
class Crew(models.Model):
    person = models.ForeignKey(People)
    job = models.CharField(max_length=40)
    production = models.ForeignKey(Production)
    is_director = models.BooleanField(default=False)
    is_writer = models.BooleanField(default=False)
    is_producer = models.BooleanField(default=False)

class Theater_pictures(models.Model):
    image = models.ImageField()
    theater = models.ForeignKey(Theater)

# kinds of photos:
    # headshots (person)
    # scenes (several persons)
    # theaters
    # playbills

# each person, theater, play, or production can have multiple pictures, but one primary picture
# people will use headshots and scenes
# plays will use ?
# productions will use scenes and playbills
# theaters will use only theater pictures

# Want to target images at average of 20KB each


#TODO: Add class for production companies