from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT

class Geography(models.Model):
    country = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50, blank = True)

    class Meta: 
        ordering = ['county']

    def __str__(self): 
        return self.county + ", " + self.country  #function to return the county

class Species(models.Model):
    name = models.CharField(max_length=30, default= 'Choose the bird here')
    
    class Meta: 
        ordering = ['name']

    def __str__(self): 
        return self.name

class Sighting(models.Model):
    species_name = models.ForeignKey(Species, on_delete=PROTECT)
    date_seen = models.DateField(blank = True)
    photo = models.ImageField(default ='default.png', blank = True)
    location = models.ForeignKey(Geography, on_delete = PROTECT)
    # sound_file = models.FileField(upload_to=/'sounds/')
    # class Meta:
    # db_table='Audio_store'
    # maybe later add user 
    birder = models.ForeignKey(User, on_delete = CASCADE, default=None, blank= True)

    def __str__(self): 
        return self.species_name  #function to return the name of the instance of Species