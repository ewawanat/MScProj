from django.contrib import admin
from .models import Country, County, Species

admin.site.register(Species) #registering the species model on the admin site
admin.site.register(Country) 
admin.site.register(County) 