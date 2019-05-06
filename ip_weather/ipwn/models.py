from django.db import models

# Create your models here.

class Ip(models.Model):
    address = models.CharField(max_length=39) #ipv6
    lat = models.CharField(max_length=20)
    long = models.CharField(max_length=20)
    city = models.CharField(max_length=45)
    state_prov = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    country_code = models.CharField(max_length=2)
    def __str__(self):
        return self.address
    class Meta:
        verbose_name = 'IP Address'
        verbose_name_plural = 'IP Addresses'


class City(models.Model):
    name = models.CharField(max_length=45)
    country_code = models.CharField(max_length=2)
    weather_temperature= models.DecimalField(..., max_digits=5, decimal_places=2)
    weather_description = models.CharField(max_length=150)
    weather_icon = models.CharField(max_length=15)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'cities'


class Headline(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    source = models.CharField(max_length=150)
    def __str__(self):
        return self.id
    class Meta:
        verbose_name_plural = 'headlines'