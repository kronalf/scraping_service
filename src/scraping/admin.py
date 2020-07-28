from django.contrib import admin
from .models import City, Language, Jobs_list
# Register your models here.

admin.site.register(City)
admin.site.register(Language)
admin.site.register(Jobs_list)