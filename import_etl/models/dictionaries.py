from common.models import dictionaries
from ..managers import BasicLookupDictionaryManager


class DateDictionary(dictionaries.DateDictionary):
    objects = BasicLookupDictionaryManager()


class AreaCodesDictionary(dictionaries.AreaCodesDictionary):
    objects = BasicLookupDictionaryManager()


class PropertyTypesDictionary(dictionaries.PropertyTypesDictionary):
    objects = BasicLookupDictionaryManager()


class DurationTypesDictionary(dictionaries.DurationTypesDictionary):
    objects = BasicLookupDictionaryManager()


class NewPropertyTypesDictionary(dictionaries.NewPropertyTypesDictionary):
    objects = BasicLookupDictionaryManager()


