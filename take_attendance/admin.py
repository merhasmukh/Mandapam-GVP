from django.contrib import admin
from .models import PrathanaLocation

@admin.register(PrathanaLocation)
class PrathanaLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'start_time', 'end_time')
    list_filter = ('start_time', 'end_time')
    search_fields = ('name',)

# Register your models here.
