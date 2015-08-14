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

class Production(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    production_company = models.CharField(max_length=100)

