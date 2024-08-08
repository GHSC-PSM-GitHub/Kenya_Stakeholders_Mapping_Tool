from django.contrib import admin

# Register your models here.

from . models import Record, Functionalarea, Rolename

admin.site.register(Record)
admin.site.register(Functionalarea)
admin.site.register(Rolename)

