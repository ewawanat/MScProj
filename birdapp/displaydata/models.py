from django.db import models
from django.db.models.deletion import PROTECT
from enterdata.models import Country, County
from enterdata.models import Species

class DisplayForm(models.Model):
    species_name = models.ForeignKey(Species, on_delete=PROTECT)
    country = models.ForeignKey(Country, on_delete=PROTECT, default='All')
    county = models.ForeignKey(County, on_delete=PROTECT, default='All')
    from_date = models.DateField()
    to_date = models.DateField()
#  birder = models.ForeignKey(User, on_delete=CASCADE, default=None)

    def __str__(self): 
        return self.species_name  #function to return the name of the instance of DisplayForm