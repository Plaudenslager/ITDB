from django.db import models

# Create your models here.
class Theater(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state_or_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    def __unicode__(self):
        return "{0}: {1}, {2}".format(self.name, self.city, self.state)

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

class Production(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    production_company = models.CharField(max_length=100)
    play = models.ForeignKey(Play)
    theater = models.ForeignKey(Theater)
    def __unicode__(self):
        return "{0}, {1} ({2} - {3})".format(Play(self.play), Theater(self.theater), self.start_date, self.end_date)

class Cast(models.Model):
    person = models.ForeignKey(People)
    character = models.CharField(max_length=40)
    production = models.ForeignKey(Production)
    billed_as = models.CharField(max_length = 40)