from django.contrib import admin
from django.shortcuts import reverse

from django.urls import path

from django.utils.html import format_html

# Register your models here.

from .models import Organoleptica

@admin.register(Organoleptica)
class OrganolepticaAdmin(admin.ModelAdmin):

    # añadir un template antes de la tabla de datos
    # change_list_template = 'admin/new.html'


    date_hierarchy = 'fecha'

    search_fields = (
        'fecha',
        'punto_muestreo',
        'presenta_color',
        'presenta_olor',
        'presenta_sabor',
        'particulas_extrañas',
        'responsable',
        'observaciones',
    )

    # change checkbox to radio button
    radio_fields = {
        "presenta_color": admin.HORIZONTAL,
        "presenta_olor": admin.HORIZONTAL,
        "presenta_sabor": admin.HORIZONTAL,
        "particulas_extrañas": admin.HORIZONTAL,
        }
    
    list_display = (
        'fecha',
        'punto_muestreo',
        'presenta_color',
        'presenta_olor',
        'presenta_sabor',
        'particulas_extrañas',
        'acciones',
    )

    

    def acciones(self, obj):
        return format_html(
            '<a class="fas fa-pen edit" href="{}" style="color: #1E1E1E; background: #F9C100; padding: 5px; border-radius: 5px;"></a>&nbsp;'
            '<a class="fas fa-trash-alt delete" href="{}" style="color: white; background: #D23846; padding: 6px; border-radius: 6px;"></a>',
            reverse('admin:organoleptica_organoleptica_change', args=[obj.pk]),
            reverse('admin:organoleptica_organoleptica_delete', args=[obj.pk]),
        )
    
    class Media:
        css = {
            "all": ("css/organoleptica.css",)
        }
        js = ("js/organoleptica.js",)