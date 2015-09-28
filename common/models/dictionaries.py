from django.db import models


class BasicDictionary(models.Model):
    """
    Basic Abstract Dictionary
    """
    class Meta:
        abstract = True


class DateDictionary(models.Model):
    """
    Standard Date dictionary in a field of snow-flake pattern
    """
    src_id = models.DateField('Date')
    year = models.PositiveSmallIntegerField('Year')
    month = models.PositiveSmallIntegerField('Month')
    day_of_the_month = models.PositiveSmallIntegerField('Day of the month')
    quarter_of_the_year = models.PositiveSmallIntegerField('Quarter of the month')
    half_of_the_year = models.PositiveSmallIntegerField('Half of the year')

    def __str__(self):
        return '%d.%02d.%02d' % (self.year, self.month, self.day_of_the_month)

    class Meta:
        abstract = True


class AreaCodesDictionary(BasicDictionary):
    """
    Dictionary with UK area codes
    """
    src_id = models.CharField(max_length=4, unique=True)

    @property
    def name(self):
        return '%s' % self.src_id

    def __str__(self):
        return '%s' % self.name

    class Meta:
        abstract = True
        verbose_name = 'Area Code'
        verbose_name_plural = 'Area Codes'


class SingleCharWithNameDictionary(BasicDictionary):
    """
    Abstract dictionary for values with name and single char representation
    """
    src_id = models.CharField(max_length=1, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        abstract = True


class PropertyTypesDictionary(SingleCharWithNameDictionary):
    """
    Property Types Dictionary
    """
    class Meta:
        verbose_name = 'Property type'
        verbose_name_plural = 'Property types'
        abstract = True


class DurationTypesDictionary(SingleCharWithNameDictionary):
    """
    Durations Dictionary
    """
    class Meta:
        verbose_name = 'Duration type'
        verbose_name_plural = 'Duration types'
        abstract = True


class NewPropertyTypesDictionary(SingleCharWithNameDictionary):
    """
    New Properties Dictionary
    """
    class Meta:
        verbose_name = 'New property type'
        verbose_name_plural = 'New property types'
        abstract = True


