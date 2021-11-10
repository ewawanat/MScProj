from django.contrib import admin
from .models import Species, Geography

admin.site.register(Species) #registering the species model on the admin site
admin.site.register(Geography) 