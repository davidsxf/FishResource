from django.contrib import admin
from .models import Province,City,Area,Town
# Register your models here.
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Town)