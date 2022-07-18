from django.contrib import admin

from django.contrib.admin import ModelAdmin

from .models import Airplane


class AirplaneAdmin(ModelAdmin):
    list_display = ('airplane_id', 'fuel_tank', 'consumption', 'minutes_to_fly',)
    readonly_fields = ('fuel_tank', 'consumption', 'minutes_to_fly',)


admin.site.register(Airplane, AirplaneAdmin)
