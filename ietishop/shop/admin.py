from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Tag)
admin.site.register(Producte)
admin.site.register(Compra)
admin.site.register(Cistella)
admin.site.register(DetallCompra)

class ProducteInline(admin.TabularInline):
    model = Producte
    readonly_fields = ["descripcio"]


class CategoriaInLine(admin.TabularInline):
    model = Categoria
    extra = 0
    exclude = ("descripcio",)


class CompraInLine(admin.TabularInline):
    model = Compra
    extra = 0


class DetallCompraInLine(admin.TabularInline):
    model = DetallCompra
    extra = 0


class CistellaAdmin(admin.ModelAdmin):
    filter_horizontal = ('Productes',)


class DetallCompraAdmin(admin.ModelAdmin):
    inlines = [DetallCompraInLine, ProducteInline]


class CompraAdmin(admin.ModelAdmin):
    inlines = [CompraInLine, DetallCompraInLine]


class CategoriaAdmin(admin.ModelAdmin):
    inlines = [CategoriaInLine, ProducteInline]
    list_display = ["nom", "parent"]


admin.site.register(Categoria, CategoriaAdmin)
