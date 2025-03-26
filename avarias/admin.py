from django.contrib import admin
from avarias.models import Avaria, Brand

# Register your models here.


class AvariaAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'value','voltagem','nf',)
    search_field = ('model','voltagem')


admin.site.register(Avaria, AvariaAdmin)

class BrandAdmin (admin.ModelAdmin):
    list_display = ('industria',)
    search_fields = ('industria',)
admin.site.register(Brand, BrandAdmin)
