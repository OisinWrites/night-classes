from django.contrib import admin
from .models import NightClass
from django.utils.html import format_html

@admin.register(NightClass)
class NightClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'formatted_time', 'formatted_start_date', 'fee', 'sold_out')
    search_fields = ('name', 'description', 'optional_tag')
    list_filter = ('sold_out',)
    
    def formatted_time(self, obj):
        return obj.time
    formatted_time.short_description = 'Time'

    def formatted_start_date(self, obj):
        return obj.start_date.strftime('%A %dth %B')
    formatted_start_date.short_description = 'Start Date'
