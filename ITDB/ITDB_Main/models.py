from django.db import models

# Create your models here.
class Theater(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state_or_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Play(models.Model):
    title = models.CharField(max_length=100)
    year_written = models.IntegerField()

class People(models.Model):
    name = models.CharField(max_length=40)
    short_bio = models.TextField()

class Production(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    production_company = models.CharField(max_length=100)
    play = models.ForeignKey(Play)
    theater = models.ForeignKey(Theater)

class Cast(models.Model):
    person = models.ForeignKey(People)
    character = models.CharField(max_length=40)
    production = models.ForeignKey(Production)
    billed_as = models.CharField(max_length = 40)