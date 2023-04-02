from django.db import models

#Create your models here.

class City(models.Model):
    ID = models.IntegerField(primary_key=True, auto_created=True)
    Name = models.CharField(max_length=35, default='')
    CountryCode = models.ForeignKey('Country', on_delete=models.CASCADE)
    District = models.CharField(max_length=20, default='')
    Population = models.IntegerField(default=0)
    #Country = models.ForeignKey('Country', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'city'

class Country(models.Model):
    Code = models.CharField(max_length=3, primary_key=True)
    Name = models.CharField(max_length=52)
    CONTINENTS = [
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('Africa', 'Africa'),
        ('Oceania', 'Oceania'),
        ('Antarctica', 'Antarctica'),
        ('South America', 'South America'),
    ]
    Continent = models.CharField(max_length=13, choices=CONTINENTS)
    Region = models.CharField(max_length=26)
    SurfaceArea = models.FloatField(default=0.00)
    IndepYear = models.SmallIntegerField(null=True)
    Population = models.IntegerField(default=0)
    LifeExpectancy = models.FloatField(null=True)
    GNP = models.FloatField(null=True)
    GNPOld = models.FloatField(null=True)
    LocalName = models.CharField(max_length=45)
    GovernmentForm = models.CharField(max_length=45)
    HeadOfState = models.CharField(max_length=60, null=True)
    Capital = models.IntegerField(null=True)
    Code2 = models.CharField(max_length=2)
    
    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'country'

class CountryLanguage(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    CountryCode = models.ForeignKey('Country', on_delete=models.CASCADE)
    Language = models.CharField(max_length=30, default='')
    IsOfficial = models.CharField(max_length=3)
    Percentage = models.FloatField(default=0.0)
   
    class Meta:
        db_table = 'countrylanguage'
        
    
