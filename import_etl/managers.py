from django.db.models import Manager
from django.core.cache import cache as django_cache
import uuid


class BasicLookupDictionaryManager(Manager):
    """
    Simple caching Manager used by dictionaries to improve loading process
    """
    # noinspection PyUnresolvedReferences,PyProtectedMember
    def _get_key_for_value(self, value):
        """
        Method used to calculate 'key' for Redis cache
        :param value:
        :return: 'key' for Redis Cache
        :rtype: str
        """
        return 'dict__%s__%s__%s' % (
            self.model._meta.app_label,
            self.model._meta.db_table,
            value
        )

    def get_id_for_value(self, value):
        """
        Method return dictionary's pk for given value
        :param value: value to look for
        :return: pk of given value
        """
        if value is None or (isinstance(value, (tuple, list, str)) and len(value) == 0):
            return 0
        key = self._get_key_for_value(value)
        result = django_cache.get(key, None)
        if result is None:
            result = self.get(src_id=value).pk
            django_cache.set(key, result)
        return result


class SalesFactManager(Manager):
    def create_from_row(self, row):
        uid = uuid.UUID(row[0])
        result = self.model(transaction_uid=uid)
        result.update_from_row(row)
        result.save(force_insert=True)
        return result

