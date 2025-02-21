from django.contrib import admin
from dal import autocomplete
from django.db import models
from .models import Desktop, Description, Characteristic, Favorites, Brand, Model, AllCars, Filters
from django import forms
admin.site.register(Desktop)
admin.site.register(Description)
admin.site.register(Characteristic)
admin.site.register(Favorites)

class ModelAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['brand']

class FiltersForm(forms.ModelForm):
    class Meta:
        model = Filters
        fields = '__all__'
        widgets = {
            'model': autocomplete.ModelSelect2(
                url='model-autocomplete',
                forward=('brand',)
            )
        }

class FiltersAdmin(admin.ModelAdmin):
    form = FiltersForm

admin.site.register(Brand)
admin.site.register(Model, ModelAdmin)
admin.site.register(AllCars)
admin.site.register(Filters, FiltersAdmin)
