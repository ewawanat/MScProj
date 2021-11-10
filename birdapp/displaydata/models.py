from django.db import models
from django.db.models.deletion import PROTECT
from enterdata.models import Geography
from enterdata.models import Species

class DisplayForm(models.Model):
    species_name = models.ForeignKey(Species, on_delete=PROTECT)
    location = models.ForeignKey(Geography, on_delete=PROTECT)
    from_date = models.DateField()
    to_date = models.DateField()
#  birder = models.ForeignKey(User, on_delete=CASCADE, default=None)

    def __str__(self): 
        return self.name  #function to return the name of the instance of DisplayForm