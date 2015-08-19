from django.db import models

# Create your models here.
class Theater(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state_or_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    def __unicode__(self):
        return "{0}: {1}, {2}".format(self.name, self.city, self.state_or_province)

class Play(models.Model):
    title = models.CharField(max_length=100)
    year_written = models.IntegerField()
    def __unicode__(self):
        return "{0} ({1})".format(self.title, self.year_written)

class People(models.Model):
    name = models.CharField(max_length=40)
    short_bio = models.TextField()
    def __unicode__(self):
        return self.name

# A production is defined as a Play that ran at a particular Theater between given Dates
class Production(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    production_company = models.CharField(max_length=100)
    play = models.ForeignKey(Play)
    theater = models.ForeignKey(Theater)
    def __unicode__(self):
        return "{0}, {1} - {2} :{3} - {4}".format(self.play.title, self.theater.name, self.theater.city, self.start_date, self.end_date)

# A cast is defined as the list of People involved in a particular Production
class Cast(models.Model):
    person = models.ForeignKey(People)
    character = models.CharField(max_length=40)
    production = models.ForeignKey(Production)
    billed_as = models.CharField(max_length = 40)
    #TODO: Create a unicode function for Cast object