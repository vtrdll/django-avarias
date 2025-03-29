from django.contrib import admin
from avarias.models import Avaria, Brand,ImagemReferencia

# Register your models here.



class ImagemReferenciaInline(admin.TabularInline):
    model = ImagemReferencia
    extra = 3 # Número de formulários extras

admin.site.register(ImagemReferencia)

class AvariaAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'valor','voltagem','nota_fiscal',)
    search_field = ('modelo','voltagem')
    inlines = [ImagemReferenciaInline]

admin.site.register(Avaria, AvariaAdmin)

class BrandAdmin (admin.ModelAdmin):
    list_display = ('industria',)
    search_fields = ('industria',)
admin.site.register(Brand, BrandAdmin)

