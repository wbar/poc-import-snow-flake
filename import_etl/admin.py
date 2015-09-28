from django.contrib import admin
from . import models


@admin.register(models.AreaCodesDictionary)
@admin.register(models.DurationTypesDictionary)
@admin.register(models.NewPropertyTypesDictionary)
@admin.register(models.PropertyTypesDictionary)
class SimpleDictionaryAdmin(admin.ModelAdmin):
    fields = ('src_id', 'name')
    readonly_fields = ('src_id',)
    list_display = fields
    list_display_links = fields

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.DateDictionary)
class DateDictionaryAdmin(admin.ModelAdmin):
    fields = ('src_id', 'year', 'month', 'day_of_the_month', 'quarter_of_the_year', 'half_of_the_year')
    readonly_fields = fields
    list_display = fields

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.SaleFacts)
class SalesFactAdmin(admin.ModelAdmin):
    fields = ('transaction_uid', 'date_of_transfer', 'price',
              'area_code', 'property_type', 'new_property', 'duration')
    readonly_fields = ('transaction_uid',)
    list_display = fields
    list_display_links = fields


@admin.register(models.SaleFactsBad)
class SalesBadAdmin(admin.ModelAdmin):
    fields = ('when', 'row', 'exc')
    readonly_fields = fields
    list_display = fields
    list_display_links = fields

