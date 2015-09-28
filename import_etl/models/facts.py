from django.db import models
from common.models import facts
from . import dictionaries
from ..managers import SalesFactManager
import datetime


class SaleFacts(facts.SaleFacts):
    objects = SalesFactManager()

    def update_from_row(self, row):
        """
        Method updates value on fact based on data from input row
        :param row: ['{43F2E19F-B8BE-4121-9AAD-00007F375F68}', '240500', '2015-06-19 00:00', 'BS3 5NN', 'T', 'N', 'F',
                     '72', '', 'AYLESBURY CRESCENT', '', 'BRISTOL', 'CITY OF BRISTOL', 'CITY OF BRISTOL', 'A']
        :return: updated instance
        """
        _, price, date, postal, property_type, new_property, duration = row[:7]
        price = int(price)
        date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M').date()
        date = dictionaries.DateDictionary.objects.get_id_for_value(date)
        postal = dictionaries.AreaCodesDictionary.objects.get_id_for_value(postal.split()[0])
        property_type = dictionaries.PropertyTypesDictionary.objects.get_id_for_value(property_type)
        new_property = dictionaries.NewPropertyTypesDictionary.objects.get_id_for_value(new_property)
        duration = dictionaries.DurationTypesDictionary.objects.get_id_for_value(duration)

        self.price = price
        self.date_of_transfer_id = date
        self.area_code_id = postal
        self.property_type_id = property_type
        self.new_property_id = new_property
        self.duration_id = duration


class SaleFactsBad(models.Model):
    when = models.DateTimeField(auto_now_add=True)
    row = models.TextField()
    exc = models.TextField(null=True, blank=True)
